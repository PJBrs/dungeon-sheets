import re
from pypdf import PdfWriter
from pypdf.generic import DictionaryObject, NameObject, ArrayObject, IndirectObject, StreamObject, TextStringObject, NumberObject
from pypdf.constants import AnnotationFlag
from pdfminer.pdffont import PDFType1Font
from pdfminer.pdfinterp import PDFResourceManager

class CustomPdfWriter(PdfWriter):

    font_name_map = {
        # Map common font names/abbreviations to their canonical PostScript names
        "/Cour": "Courier",
        "/Courier": "Courier",
        "/CoBo": "Courier-Bold",
        "/Courier-Bold": "Courier-Bold",
        "/CoOb": "Courier-Oblique",
        "/Courier-Oblique": "Courier-Oblique",
        "/CoBO": "Courier-BoldOblique",
        "/Courier-BoldOblique": "Courier-BoldOblique",
        "/Helv": "Helvetica",
        "/Helvetica": "Helvetica",
        "/HeBo": "Helvetica-Bold",
        "/Helvetica-Bold": "Helvetica-Bold",
        "/HeOb": "Helvetica-Oblique",
        "/Helvetica-Oblique": "Helvetica-Oblique",
        "/HeBO": "Helvetica-BoldOblique",
        "/Helvetica-BoldOblique": "Helvetica-BoldOblique",
        "/TiRo": "Times-Roman",
        "/Times": "Times-Roman",
        "/Times-Roman": "Times-Roman",
        "/TiBo": "Times-Bold",
        "/Times-Bold": "Times-Bold",
        "/TiIt": "Times-Italic",
        "/Times-Italic": "Times-Italic",
        "/TiBI": "Times-BoldItalic",
        "/Times-BoldItalic": "Times-BoldItalic",
        "/Sym": "Symbol",
        "/Symbol": "Symbol",
        "/ZaDb": "ZapfDingbats",
        "/ZapfDingbats": "ZapfDingbats",
    }

    def extract_formatting_from_annotation(self, annotation):
        """
        Tries to extract as much specific formatting from an
        annotation as possible, such as:

        - Alignment       - V
        - Font name       - V
        - Font size       - V
        - Font colour
        - Line distance
        - ...

        I wonder whether it should also extract just the rest of the annotation...

        Returns a dictionary.

        """
        formatting = {}

        # First try to get information from the default appearance stream.
        # This holds a required normal appearance stream and _can_ hold
        # additional appearance streams associated with mouse rollover
        # and click, but these need not be used for flattening.
        if "/AP" in annotation:
            ap_dict = annotation["/AP"]
            normal_appearance_stream_ref = ap_dict["/N"]
            if isinstance(normal_appearance_stream_ref, IndirectObject):
                normal_appearance_stream = normal_appearance_stream_ref.get_object()
            else:
                normal_appearance_stream = normal_appearance_stream_ref

            if isinstance(normal_appearance_stream, StreamObject):
                content_stream_data = normal_appearance_stream.get_data()

                # Match font name and size. The subgroup is necessary because sometimes font
                # sizes are in integers and sometimes in floats, and in rare cases an integer
                # is followed by a period.
                font_ops = re.search(rb'(/[^/\s]+)\s*(\d+(\.\d+)?)\s*Tf', content_stream_data)
                formatting["font_name"] = NameObject(font_ops.groups()[0].decode())
                formatting["font_size"] = float(font_ops.groups()[1].decode())

        elif "/DA" in annotation: # /DA is required for text streams, but still not always set
            da = annotation["/DA"]
            font_ops = re.search(r'(/[^/\s]+)\s*(\d+(\.\d+)?)\s*Tf', da)
            formatting["font_name"] = NameObject(font_ops.groups()[0])
            formatting["font_size"] = float(font_ops.groups()[1])
        else: # Default options
            formatting["font_name"] = NameObject("/Helvetica")
            formatting["font_size"] = float(12.0)

        if "/Q" in annotation:
            formatting["alignment"] = annotation["/Q"] # This is a NumberObject
        else:
            formatting["alignment"] = NumberObject(0)

        return formatting


    def base14_font_object(self, font):
        """
        Creates a font object for one of the base 14 pdf fonts.
        Takes a NameObject.
        """
        if font in self.font_name_map.keys():
            fontname = NameObject("/" + self.font_name_map[font])
        else:
            fontname = font

        standard_font_obj = DictionaryObject({
            NameObject("/Type"): NameObject("/Font"),
            NameObject("/Subtype"): NameObject("/Type1"),
            NameObject("/Name"): font,
            NameObject("/BaseFont"): fontname,
            NameObject("/Encoding"): NameObject("/WinAnsiEncoding") # Should not be necessary
        })

        return standard_font_obj


    def calculate_text_width(self, font_name, font_size, text):
        """
        Calculates the display width of a given text string in PDF user space units
        by instantiating a PDFType1Font object from pdfminer.six for Base 14 fonts.
        """
        canonical_font_name = self.font_name_map.get(font_name)

        if not canonical_font_name:
            print(f"Warning: Unknown Base 14 font name '{font_name}'. Cannot accurately calculate text width. Using rough estimate.")
            return len(text) * font_size * 0.6

        # Instantiate a dummy PDFResourceManager
        rsrcmgr = PDFResourceManager()

        # Create a minimal font specification dictionary for PDFType1Font
        # PDFType1Font will use 'BaseFont' to look up widths internally.
        font_spec = {
            'Type': NameObject("/Font"),
            'Subtype': NameObject("/Type1"),
            'BaseFont': NameObject(canonical_font_name),
            'Encoding': NameObject("/WinAnsiEncoding"), # Most common for Base 14 fonts
            # We don't need to explicitly add 'Widths' here; PDFType1Font retrieves them internally
        }

        pdffont_obj = None
        try:
            pdffont_obj = PDFType1Font(rsrcmgr, font_spec)
        except Exception as e:
            print(f"Error creating PDFType1Font object for '{canonical_font_name}': {e}. Falling back to rough estimate.")
            return len(text) * font_size * 0.6

        total_font_units_width = 0
        default_width_fallback = 500 # A general fallback if get_width has issues

        for char in text:
            # PDFFont.get_width() returns the width in font units (typically 1000 per em)
            char_width = pdffont_obj.widths[char]
            if char_width is None:
                char_width = pdffont_obj.default_width if hasattr(pdffont_obj, 'default_width') else default_width_fallback

            total_font_units_width += char_width

        text_width_in_points = (total_font_units_width * font_size) / 1000.0
        return text_width_in_points


    def wrap_text(
        self: PdfWriter,
        font_name: str,
        font_size: float,
        field_width: float,
        field_height: float,
        text: str,
        min_font_size: float = 4.0,       # Minimum font size to attempt
        font_size_step: float = 0.5       # How much to decrease font size by each step
    ):
        """
        Takes a piece of text and adds newlines to wrap it
        into a rect of given size, given font_name and
        font_size. Recursively reduces font_size if text exceeds field_height.
        Returns (wrapped_lines, font_size).
        """
        orig_text = text
        text = re.sub(r"\r", "\n", text)

        if field_width <= 0 or field_height <= 0 or font_size <= 0:
            print(f"Warning: Field dimensions or font size invalid ({field_width}, {field_height}, {font_size}). Returning empty lines.")
            return [], font_size

        wrapped_lines = []
        current_line_words = []
        current_line_width = 0

        paragraphs = text.split('\n')

        for paragraph in paragraphs:
            if not paragraph.strip():
                wrapped_lines.append("")
                continue

            words = paragraph.split(' ')
            for i, word in enumerate(words):
                word_width = self.calculate_text_width(font_name, font_size, word)
                space_width = self.calculate_text_width(font_name, font_size, " ") if i > 0 else 0

                test_width = current_line_width + space_width + word_width

                if test_width > field_width and current_line_words:
                    wrapped_lines.append(" ".join(current_line_words))
                    current_line_words = [word]
                    current_line_width = word_width
                elif not current_line_words and word_width > field_width:
                    wrapped_lines.append(word)
                    current_line_words = []
                    current_line_width = 0
                else:
                    if current_line_words:
                        current_line_width += space_width
                    current_line_words.append(word)
                    current_line_width += word_width

            if current_line_words:
                wrapped_lines.append(" ".join(current_line_words))
                current_line_words = []
                current_line_width = 0

        line_height_estimate = font_size * 1.2 # TODO: Add real line spacing here.
        estimated_total_height = len(wrapped_lines) * line_height_estimate

        if estimated_total_height > field_height:
            new_font_size = font_size - font_size_step
            if new_font_size >= min_font_size:
                # Text overflows height; Retry with smaller font size.
                return self.wrap_text(font_name, new_font_size, field_width, field_height, orig_text, min_font_size, font_size_step)
            else:
                # Font size lower than set minimum font size, give up.
                return wrapped_lines, font_size
        else:
            return wrapped_lines, font_size


    def merge_content_streams(self, existing_content, new_content_data):
        """
        Combines existing content stream(s) with new content (as bytes),
        and returns a new single StreamObject.
        """
        merged_data = b""

        # First deal with the case where existing_content is an IndirectObject
        if isinstance(existing_content, IndirectObject):
            existing_content = existing_content.get_object()

        if isinstance(existing_content, ArrayObject):
            for obj in existing_content:
                stream = obj.get_object()
                if isinstance(stream, StreamObject):
                    merged_data += stream.get_data() + b"\n"
        elif isinstance(existing_content, StreamObject):
            merged_data += existing_content.get_data() + b"\n"

        merged_data += new_content_data

        new_stream = StreamObject()
        new_stream._data = merged_data
        return self._add_object(new_stream)


    def add_text_field_value(self, page, annotation, rect):
        """
        Adds the value of a text field to the page content. Returns
        True if successful, and False otherwise.
        """
        field_value = annotation.get("/V", "") # Get the text value
        field_name = annotation.get("/T", "Unnamed Field")
        x_min, y_min, x_max, y_max = [float(f) for f in rect]

        font_name, font_size, alignment = self.extract_formatting_from_annotation(annotation).values()

        # Add font if not already there, but only if it's one of the base 14 ones
        # Need to check if the font dictionary itself exists before checking its contents
        if "/Resources" not in page:
            page[NameObject("/Resources")] = DictionaryObject()
        if "/Font" not in page["/Resources"]:
            page["/Resources"][NameObject("/Font")] = DictionaryObject()
        if font_name not in page["/Resources"]["/Font"]:
            if self.font_name_map.get(font_name):
                # Ensure the font object is added to the writer and its indirect reference is used
                font_obj = self.base14_font_object(font_name)
                font_ref = self._add_object(font_obj) # Add font object as an indirect object
                page["/Resources"]["/Font"][font_name] = font_ref
            else:
                print(f"  - Font '{font_name}' is missing and not a recognized Base 14 font. Trouble ahead...")

        # Check if there's any content to flatten.
        if field_value and isinstance(field_value, str) and field_value.strip():
            # Approximate text size and position
            field_width = x_max - x_min
            field_height = y_max - y_min

            lines, final_font_size = self.wrap_text(
                font_name,
                font_size,
                field_width,
                field_height,
                field_value
            )

            # Positioning based on alignment
            text_x = x_min
            text_y_start = y_max - final_font_size # Top of the first line

            text_commands = b"q\n" # Save graphics state
            text_commands += b"BT\n" # Begin Text Object
            text_commands += b"0 g\n" # Set fill color to black (grayscale) TODO: get colour from annotation appearance
            text_commands += f"{font_name} {final_font_size} Tf \n".encode('ascii')

            for i, line in enumerate(lines):
                current_text_x = x_min # Default to left alignment
                if alignment == 1: # Center
                    line_text_width = self.calculate_text_width(font_name, final_font_size, line)
                    current_text_x = x_min + (field_width - line_text_width) / 2
                elif alignment == 2: # Right
                    line_text_width = self.calculate_text_width(font_name, final_font_size, line)
                    current_text_x = x_max - line_text_width

                # Calculate current line's Y position
                current_text_y = text_y_start - (i * final_font_size * 1.2) # TODO: Get real line spacing and add it here...

                text_commands += (f"1 0 0 1 {current_text_x} {current_text_y} Tm \n".encode("ascii")) # Set Text Matrix (absolute position)
                text_commands += b"(" + line.encode('pdfdoc') + b") Tj\n" # Show text (encoded for PDF)

            text_commands += b"ET\n" # End Text Object
            text_commands += b"Q\n" # Restore graphics state

            # Create a StreamObject to hold the appearance stream
            appearance_stream_obj = StreamObject()
            appearance_stream_obj._data = text_commands
            appearance_stream_obj.update({
                NameObject("/Type"): NameObject("/XObject"),
                NameObject("/Subtype"): NameObject("/Form"),
                NameObject("/BBox"): rect,
                NameObject("/Resources"): DictionaryObject({
                    NameObject("/Font"): DictionaryObject({
                        NameObject(font_name): page["/Resources"]["/Font"][NameObject(font_name)], # Reference the font added to the page
                    }),
                    # /ProcSet is often found but not strictly necessary for simple text,
                    # but can be added if needed: NameObject("/ProcSet"): ArrayObject([NameObject("/PDF"), NameObject("/Text")])
                })
            })

            # IMPORTANT: Add the appearance stream as an indirect object to the PDF writer
            # and then use its indirect reference in the page content.
            appearance_stream_ref = self._add_object(appearance_stream_obj)

            new_content_ref = self.merge_content_streams(page.get("/Contents"), appearance_stream_obj.get_data())
            page[NameObject("/Contents")] = new_content_ref

            return True

        # No need to add or flatten text annotations that have no conten.
        return True

    def _get_button_appearance_stream(self, appearance_dict, current_state_name, field_type, field_flags_int):
        """
        Helper to robustly find the correct appearance stream for a button state
        within a given appearance dictionary (e.g., /N or /D).
        """
        # If appearance_dict is a direct stream reference, return it.
        if isinstance(appearance_dict, (IndirectObject, StreamObject)):
            return appearance_dict

        # If it's not a dictionary, or empty, nothing to do.
        if not isinstance(appearance_dict, DictionaryObject) or not appearance_dict:
            return None

        # Prioritize the current state name (from /V or /AS).
        # This is for checkboxes and radio buttons primarily.
        if current_state_name and current_state_name in appearance_dict:
            return appearance_dict.get(current_state_name)

        # For push buttons, they often don't have explicit states like /On or /Off in /N
        # but just a single default appearance.
        # Check if it's a push button (bit 16 set) and no specific state was found.
        is_push_button = (field_flags_int & (1 << 16)) != 0
        if field_type == "/Btn" and is_push_button:
            # For a push button, typically there's only one appearance stream in /N,
            # or it might be keyed as /Off or /Normal. Let's try to get a reasonable default.
            if NameObject("/Normal") in appearance_dict:
                return appearance_dict.get(NameObject("/Normal"))
            if NameObject("/Off") in appearance_dict:
                return appearance_dict.get(NameObject("/Off"))
            # If still not found, just take the first entry if available (common for simple push buttons)
            if appearance_dict:
                return list(appearance_dict.values())[0]

        # For other button types (checkboxes, radio buttons) if the current state was NOT found,
        # we should NOT fall back to other states like /On or /Yes implicitly.
        # If the requested state (e.g., /Off) was explicitly defined but not found in the dictionary,
        # it means the PDF is malformed or we don't have the specific appearance for the desired state.
        print(f"        - No specific appearance found for current state {current_state_name} and no generic fallback applies.")
        return None # Return None if the specific state requested is not found.


    def add_button_field_value(self, page, annotation, rect):
        """
        Flattens the appearance of a button field to the page content.
        This function handles various button types (push buttons, checkboxes, radio buttons)
        by embedding their current appearance stream directly onto the page's content.
        Returns True if successful, and False otherwise.
        """
        field_name = annotation.get("/T", "Unnamed Button Field")
        x_min, y_min, x_max, y_max = [float(f) for f in rect]
        width = x_max - x_min
        height = y_max - y_min

        ap_dict = annotation.get("/AP")
        if not ap_dict:
            print(f"      - WARNING: Button field '{field_name}' has no /AP dictionary. Skipping flattening.")
            return False

        current_state_name = None
        field_type = annotation.get("/FT")
        field_flags = annotation.get("/Ff", NumberObject(0))
        field_flags_int = int(field_flags) # Ensure integer conversion for flags

        if field_type == "/Btn":
            # Corrected bitwise checks for Radio and Pushbutton flags
            is_radio_button = (field_flags_int & (1 << 15)) != 0
            is_push_button = (field_flags_int & (1 << 16)) != 0

            if is_radio_button:
                current_state_name = annotation.get("/V", NameObject("/Off"))
            elif not is_push_button: # Checkbox
                current_state_name = annotation.get("/AS", NameObject("/Off"))

            if not is_push_button and current_state_name == NameObject("/Off"):
                print(f"      - Button '{field_name}' is a checkbox/radio button in /Off state. Skipping drawing to make invisible.")
                return True

        # Try to get appearance from Normal state first
        appearance_stream_ref = self._get_button_appearance_stream(
            ap_dict.get("/N"), current_state_name, field_type, field_flags_int
        )

        # If not found in Normal, try Down state (if available, mostly for push buttons but can apply to others)
        if not appearance_stream_ref and ap_dict.get("/D"):
            print(f"      - No appearance found in /N. Checking /D dictionary for button '{field_name}'.")
            appearance_stream_ref = self._get_button_appearance_stream(
                ap_dict.get("/D"), current_state_name, field_type, field_flags_int
            )

        if not appearance_stream_ref:
            print(f"      - WARNING: Could not find any suitable appearance stream for button '{field_name}'. Skipping flattening.")
            return False

        # Resolve the actual StreamObject that represents the appearance
        appearance_stream_obj = appearance_stream_ref.get_object()

        if not isinstance(appearance_stream_obj, StreamObject):
            print(f"      - WARNING: Resolved appearance object for button '{field_name}' is not a StreamObject ({type(appearance_stream_obj)}). Skipping flattening.")
            return False

        # Ensure the appearance stream is correctly identified as a Form XObject
        if appearance_stream_obj.get("/Subtype") != "/Form":
            print(f"      - WARNING: Appearance stream for button '{field_name}' is not a Form XObject ({appearance_stream_obj.get('/Subtype')}). Skipping flattening.")
            return False

        # Prepare XObject resource dictionary on the page
        if "/Resources" not in page:
            page[NameObject("/Resources")] = DictionaryObject()
        if "/XObject" not in page["/Resources"]:
            page[NameObject("/Resources")][NameObject("/XObject")] = DictionaryObject()

        # Always add the resolved stream object to the writer to get a new IndirectObject.
        # This ensures we have a valid IndirectObject managed by *this* writer.
        xobject_ref = self._add_object(appearance_stream_obj)


        # Create a name for the XObject TODO Is this sufficiently unique?
        # Sanitize the original field name to be a valid PDF name part (alphanumeric, underscore, hyphen)
        # Replacing spaces with underscores, then removing any other non-alphanumeric/non-underscore/non-hyphen
        sanitized_name = field_name.replace(" ", "_")
        sanitized_name = re.sub(r'[^a-zA-Z0-9_-]', '', sanitized_name)
        xobject_name = NameObject(f"/Fm_{sanitized_name}")

        if xobject_name not in page["/Resources"]["/XObject"]:
            page["/Resources"]["/XObject"][xobject_name] = xobject_ref
        else:
            print(f"      - XObject '{xobject_name}' already added to page resources. This might be an issue.")


        # Get the bounding box of the appearance stream itself
        ap_bbox = appearance_stream_obj.get("/BBox")

        if not ap_bbox or len(ap_bbox) != 4:
            print(f"      - WARNING: Appearance stream for button '{field_name}' has no valid /BBox. Assuming it draws to fill the annotation Rect.")
            # If no BBox, assume the XObject's content is defined to directly fit the annotation rect.
            ap_x_min, ap_y_min, ap_x_max, ap_y_max = 0, 0, width, height
        else:
            ap_x_min, ap_y_min, ap_x_max, ap_y_max = [float(f) for f in ap_bbox]

        # Calculate scale and translation to fit the appearance stream's BBox into the annotation's Rect
        ap_content_width = ap_x_max - ap_x_min
        ap_content_height = ap_y_max - ap_y_min

        # Avoid division by zero
        scale_x = width / ap_content_width if ap_content_width != 0 else 1.0
        scale_y = height / ap_content_height if ap_content_height != 0 else 1.0

        # Transformation matrix (a b c d e f) for 'a b c d e f cm'
        # This matrix scales and translates the XObject from its internal coordinate system
        # (where its BBox is defined relative to its origin) to the target annotation rectangle.
        a = scale_x
        b = 0.0
        c = 0.0
        d = scale_y
        e = x_min - (ap_x_min * scale_x)  # Translate XObject's scaled origin to annotation's X_min
        f = y_min - (ap_y_min * scale_y)  # Translate XObject's scaled origin to annotation's Y_min

        # Construct the PDF content stream commands to draw the XObject
        button_drawing_commands = f"""
q
{a:.4f} {b:.4f} {c:.4f} {d:.4f} {e:.4f} {f:.4f} cm
{xobject_name} Do
Q
""".encode('ascii')

        # Merge these commands into the page's existing content stream
        new_content_ref = self.merge_content_streams(page.get("/Contents"), button_drawing_commands)
        page[NameObject("/Contents")] = new_content_ref

        return True


    def flatten(self, keep_unflattened = True):

        for page_list_idx, page in enumerate(self.pages):

            current_page_annots_to_keep = ArrayObject()

            if "/Annots" in page:
                num_annots_on_page = len(page["/Annots"])
                print(f"Found {num_annots_on_page} annotations on page {page_list_idx + 1}.")

                for annot_list_idx, annot_ref in enumerate(page["/Annots"]):
                    try:
                        # Resolve the annotation object
                        annotation = annot_ref.get_object()
                        print(f"  - Annotation {annot_list_idx+1}/{num_annots_on_page}")

                        is_form_field_widget = False
                        if annotation.get("/Subtype") == "/Widget":
                            # A widget annotation is a form field if it has /FT, /AP, or /Ff
                            if "/FT" in annotation or "/AP" in annotation or "/Ff" in annotation:
                                is_form_field_widget = True

                        if is_form_field_widget:
                            field_type = annotation.get("/FT")
                            field_name = annotation.get("/T", "Unnamed Field")
                            print(f"    - DETECTED AS FORM FIELD WIDGET. Field Name: '{field_name}'. Type: {field_type}.")

                            rect = annotation.get("/Rect")
                            if not rect:
                                print(f"    - WARNING: Form field widget has NO /Rect (bounding box)! Skipping flattening for this field. Annotation:\n{annotation}")
                                current_page_annots_to_keep.append(annot_ref)
                                continue

                            # Now decide field type and call an associated helper function to deal with the work
                            if field_type == "/Tx": # Text field
                                if not self.add_text_field_value(page, annotation, rect):
                                    current_page_annots_to_keep.append(annot_ref)
                                    continue
                            elif field_type == "/Btn": # Button field
                                if not self.add_button_field_value(page, annotation, rect):
                                    current_page_annots_to_keep.append(annot_ref)
                                    continue
                            else: # For other types of widgets (e.g., /Ch - Choice, /Sig - Signature)
                                # We don't know how to deal with these, so keep them.
                                print(f"    - WARNING: Unhandled form field type '{field_type}'. Skipping flattening for this field. Annotation:\n{annotation}")
                                current_page_annots_to_keep.append(annot_ref)
                                continue
                        else:
                            # Not a recognized form field widget (e.g., Link, Stamp, Highlight, Widget)
                            print(f"    - NOT A RECOGNIZED FORM FIELD WIDGET. Subtype: {annotation.get('/Subtype', 'N/A')}. Skipping flattening for this field. Annotation:\n{annotation}")
                            current_page_annots_to_keep.append(annot_ref)
                            continue

                    except Exception as annot_e:
                        print(f"  - ERROR processing annotation {annot_list_idx+1} (Ref: {annot_ref.indirect_reference}): {annot_e}")
                        import traceback
                        traceback.print_exc(limit=2)
                        current_page_annots_to_keep.append(annot_ref)

            else:
                print("No annotations found on page.")

            # Update annotations list on the new page
            if len(current_page_annots_to_keep) > 0 and keep_unflattened:
                page[NameObject("/Annots")] = current_page_annots_to_keep
            else:
                # No annotations are left or wanted to keep. Remove the /Annots entry from the page
                if "/Annots" in page:
                    del page[NameObject("/Annots")]
