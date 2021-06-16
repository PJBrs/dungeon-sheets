"""
A collection of monsters from D&D 5e's SRD

This file was autogenerated by https://github.com/stravajiaxen/5e-srd-to-py
"""

from dungeonsheets.monsters.monsters import Monster
from dungeonsheets.stats import Ability


class Dao(Monster):
    """Earth Glide.
      The dao can burrow through nonmagical unworked earth and
      stone. While doing so, the dao doesn't distrub the material it
      moves through.
    Elemental Demise.
      If the dao dies, its body disintegrates into crystalline powder,
      leaving behind only equipment the dao was wearing or carrying.
    Innate Spellcasting.
      The dao's innate spellcasting ability is Charisma (spell save DC
      14, +6 to hit with spell attacks). It can innately cast the
      following spells, requiring no material components:

      At will: detect evil and good, detect magic, stone shape. 3/day
      each: passwall, move earth, tongues. 1/day each: conjure
      elemental (earth elemental only), gaseous form, invisibility,
      phantasmal killer, plane shift, wall of stone.
    Sure-Footed.
      The dao has advantage on Strength and Dexterity saving throws
      made against effects that would knock it prone.
    Multiattack.
      The dao makes two fist attacks or two maul attacks.
    Fist.
      *Melee weapon attack:* +10 to hit, reach 5ft., one
      target. *Hit:* 15 (2d8 + 6) bludgeoning damage.
    Maul.
      *Melee weapon attack:* +10 to hit, reach 5ft., one
      target. *Hit:* 20 (4d6 + 6) bludgeoning damage. If the target is
      a Huge or smaller creature, it must succeed on a DC 18 Strength
      check or be knocked prone.

    """

    name = "Dao"
    description = "Large elemental, neutral evil"
    challenge_rating = 11
    armor_class = 18
    skills = ""
    saving_throws = "Int +5, Wis +5, Cha +6"
    condition_immunities = "petrified"
    senses = "darkvision 120ft., passive Perception 11"
    languages = "Terran"
    strength = Ability(23)
    dexterity = Ability(12)
    constitution = Ability(24)
    intelligence = Ability(12)
    wisdom = Ability(13)
    charisma = Ability(14)
    speed = 30
    swim_speed = 0
    fly_speed = 30
    climb_speed = 0
    burrow_speed = 30
    hp_max = 187
    hit_dice = "15d10 + 105"


class Darkmantle(Monster):
    """
    **Echolocation**: The darkmantle can't use its blindsight while deafened.

    **False Appearance**: While the darkmantle remains motionless, it is indistinguishable from a cave formation such as a stalactite or stalagmite.

    **Crush**: Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 6 (1d6 + 3) bludgeoning damage, and the darkmantle attaches to the target. If the target is Medium or smaller and the darkmantle has advantage on the attack roll, it attaches by engulfing the target's head, and the target is also blinded and unable to breathe while the darkmantle is attached in this way.
    While attached to the target, the darkmantle can attack no other creature except the target but has advantage on its attack rolls. The darkmantle's speed also becomes 0, it can't benefit from any bonus to its speed, and it moves with the target.
    A creature can detach the darkmantle by making a successful DC 13 Strength check as an action. On its turn, the darkmantle can detach itself from the target by using 5 feet of movement.

    **Darkness Aura**: A 15-foot radius of magical darkness extends out from the darkmantle, moves with it, and spreads around corners. The darkness lasts as long as the darkmantle maintains concentration, up to 10 minutes (as if concentrating on a spell). Darkvision can't penetrate this darkness, and no natural light can illuminate it. If any of the darkness overlaps with an area of light created by a spell of 2nd level or lower, the spell creating the light is dispelled.
    """

    name = "Darkmantle"
    description = "Small monstrosity, unaligned"
    challenge_rating = 0.5
    armor_class = 11
    skills = "Stealth +3"
    senses = "Blindsight 60 ft., Passive Perception 10"
    languages = ""
    strength = Ability(16)
    dexterity = Ability(12)
    constitution = Ability(13)
    intelligence = Ability(2)
    wisdom = Ability(10)
    charisma = Ability(5)
    speed = 10
    swim_speed = 0
    fly_speed = 30
    climb_speed = 0
    hp_max = 22
    hit_dice = "5d6"


class DeathDog(Monster):
    """
    **Two-Headed**: The dog has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, or knocked unconscious.

    **Multiattack**: The dog makes two bite attacks.

    **Bite**: Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage. If the target is a creature, it must succeed on a DC 12 Constitution saving throw against disease or become poisoned until the disease is cured. Every 24 hours that elapse, the creature must repeat the saving throw, reducing its hit point maximum by 5 (1d10) on a failure. This reduction lasts until the disease is cured. The creature dies if the disease reduces its hit point maximum to 0.
    """

    name = "Death Dog"
    description = "Medium monstrosity, neutral evil"
    challenge_rating = 1
    armor_class = 12
    skills = "Perception +5, Stealth +4"
    senses = "Darkvision 120 ft., Passive Perception 15"
    languages = ""
    strength = Ability(15)
    dexterity = Ability(14)
    constitution = Ability(14)
    intelligence = Ability(3)
    wisdom = Ability(13)
    charisma = Ability(6)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 39
    hit_dice = "6d8"


class DeepGnomeSvirfneblin(Monster):
    """
    **Stone Camouflage**: The gnome has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.

    **Gnome Cunning**: The gnome has advantage on Intelligence, Wisdom, and Charisma saving throws against magic.

    **Innate Spellcasting**: The gnome's innate spellcasting ability is Intelligence (spell save DC 11). It can innately cast the following spells, requiring no material components:
    At will: nondetection (self only)
    1/day each: blindness/deafness, blur, disguise self

    **War Pick**: Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage.

    **Poisoned Dart**: Ranged Weapon Attack: +4 to hit, range 30/120 ft., one creature. Hit: 4 (1d4 + 2) piercing damage, and the target must succeed on a DC 12 Constitution saving throw or be poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success
    """

    name = "Deep Gnome (Svirfneblin)"
    description = "Small humanoid, neutral good"
    challenge_rating = 0.5
    armor_class = 15
    skills = "Investigation +3, Perception +2, Stealth +4"
    senses = "Darkvision 120 ft., Passive Perception 12"
    languages = "Gnomish, Terran, Undercommon"
    strength = Ability(15)
    dexterity = Ability(14)
    constitution = Ability(14)
    intelligence = Ability(12)
    wisdom = Ability(10)
    charisma = Ability(9)
    speed = 20
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 16
    hit_dice = "3d6"


DeepGnome = DeepGnomeSvirfneblin


class Deer(Monster):
    """
    **Bite**: Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) piercing damage.
    """

    name = "Deer"
    description = "Medium beast, unaligned"
    challenge_rating = 0
    armor_class = 13
    skills = ""
    senses = "Passive Perception 12"
    languages = ""
    strength = Ability(11)
    dexterity = Ability(16)
    constitution = Ability(11)
    intelligence = Ability(2)
    wisdom = Ability(14)
    charisma = Ability(5)
    speed = 50
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 4
    hit_dice = "1d8"


class Deva(Monster):
    """
    **Angelic Weapons**: The deva's weapon attacks are magical. When the deva hits with any weapon, the weapon deals an extra 4d8 radiant damage (included in the attack).

    **Innate Spellcasting**: The deva's spellcasting ability is Charisma (spell save DC 17). The deva can innately cast the following spells, requiring only verbal components:
    At will: detect evil and good
    1/day each: commune, raise dead

    **Magic Resistance**: The deva has advantage on saving throws against spells and other magical effects.

    **Multiattack**: The deva makes two melee attacks.

    **Mace**: Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) bludgeoning damage plus 18 (4d8) radiant damage.

    **Healing Touch**: The deva touches another creature. The target magically regains 20 (4d8 + 2) hit points and is freed from any curse, disease, poison, blindness, or deafness.

    **Change Shape**: The deva magically polymorphs into a humanoid or beast that has a challenge rating equal to or less than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the deva's choice).
    In a new form, the deva retains its game statistics and ability to speak, but its AC, movement modes, Strength, Dexterity, and special senses are replaced by those of the new form, and it gains any statistics and capabilities (except class features, legendary actions, and lair actions) that the new form has but that it lacks.
    """

    name = "Deva"
    description = "Medium celestial, lawful good"
    challenge_rating = 10
    armor_class = 17
    skills = "Insight +9, Perception +9"
    senses = "Darkvision 120 ft., Passive Perception 19"
    languages = "all, telepathy 120 ft."
    strength = Ability(18)
    dexterity = Ability(18)
    constitution = Ability(18)
    intelligence = Ability(17)
    wisdom = Ability(20)
    charisma = Ability(20)
    speed = 30
    swim_speed = 0
    fly_speed = 90
    climb_speed = 0
    hp_max = 136
    hit_dice = "16d8"


class DireWolf(Monster):
    """
    **Keen Hearing and Smell**: The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.

    **Pack Tactics**: The wolf has advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 ft. of the creature and the ally isn't incapacitated.

    **Bite**: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.
    """

    name = "Dire Wolf"
    description = "Large beast, unaligned"
    challenge_rating = 1
    armor_class = 14
    skills = "Perception +3, Stealth +4"
    senses = "Passive Perception 13"
    languages = ""
    strength = Ability(17)
    dexterity = Ability(15)
    constitution = Ability(15)
    intelligence = Ability(3)
    wisdom = Ability(12)
    charisma = Ability(7)
    speed = 50
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 37
    hit_dice = "5d10"


class Djinni(Monster):
    """
    **Elemental Demise**: If the djinni dies, its body disintegrates into a warm breeze, leaving behind only equipment the djinni was wearing or carrying.

    **Innate Spellcasting**: The djinni's innate spellcasting ability is Charisma (spell save DC 17, +9 to hit with spell attacks). It can innately cast the following spells, requiring no material components:

    At will: detect evil and good, detect magic, thunderwave
    3/day each: create food and water (can create wine instead of water), tongues, wind walk
    1/day each: conjure elemental (air elemental only), creation, gaseous form, invisibility, major image, plane shift

    **Variant: Genie Powers**: Genies have a variety of magical capabilities, including spells. A few have even greater powers that allow them to alter their appearance or the nature of reality.

    Disguises.
    Some genies can veil themselves in illusion to pass as other similarly shaped creatures. Such genies can innately cast the disguise self spell at will, often with a longer duration than is normal for that spell. Mightier genies can cast the true polymorph spell one to three times per day, possibly with a longer duration than normal. Such genies can change only their own shape, but a rare few can use the spell on other creatures and objects as well.
    Wishes.
    The genie power to grant wishes is legendary among mortals. Only the most potent genies, such as those among the nobility, can do so. A particular genie that has this power can grant one to three wishes to a creature that isn't a genie. Once a genie has granted its limit of wishes, it can't grant wishes again for some amount of time (usually 1 year). and cosmic law dictates that the same genie can expend its limit of wishes on a specific creature only once in that creature's existence.
    To be granted a wish, a creature within 60 feet of the genie states a desired effect to it. The genie can then cast the wish spell on the creature's behalf to bring about the effect. Depending on the genie's nature, the genie might try to pervert the intent of the wish by exploiting the wish's poor wording. The perversion of the wording is usually crafted to be to the genie's benefit.

    **Multiattack**: The djinni makes three scimitar attacks.

    **Scimitar**: Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage plus 3 (1d6) lightning or thunder damage (djinni's choice).

    **Create Whirlwind**: A 5-foot-radius, 30-foot-tall cylinder of swirling air magically forms on a point the djinni can see within 120 feet of it. The whirlwind lasts as long as the djinni maintains concentration (as if concentrating on a spell). Any creature but the djinni that enters the whirlwind must succeed on a DC 18 Strength saving throw or be restrained by it. The djinni can move the whirlwind up to 60 feet as an action, and creatures restrained by the whirlwind move with it. The whirlwind ends if the djinni loses sight of it.
    A creature can use its action to free a creature restrained by the whirlwind, including itself, by succeeding on a DC 18 Strength check. If the check succeeds, the creature is no longer restrained and moves to the nearest space outside the whirlwind.
    """

    name = "Djinni"
    description = "Large elemental, chaotic good"
    challenge_rating = 11
    armor_class = 17
    skills = ""
    senses = "Darkvision 120 ft., Passive Perception 13"
    languages = "Auran"
    strength = Ability(21)
    dexterity = Ability(15)
    constitution = Ability(22)
    intelligence = Ability(15)
    wisdom = Ability(16)
    charisma = Ability(20)
    speed = 30
    swim_speed = 0
    fly_speed = 90
    climb_speed = 0
    hp_max = 161
    hit_dice = "14d10"


class Doppelganger(Monster):
    """
    **Shapechanger**: The doppelganger can use its action to polymorph into a Small or Medium humanoid it has seen, or back into its true form. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.

    **Ambusher**: The doppelganger has advantage on attack rolls against any creature it has surprised.

    **Surprise Attack**: If the doppelganger surprises a creature and hits it with an attack during the first round of combat, the target takes an extra 10 (3d6) damage from the attack.

    **Multiattack**: The doppelganger makes two melee attacks.

    **Slam**: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) bludgeoning damage.

    **Read Thoughts**: The doppelganger magically reads the surface thoughts of one creature within 60 ft. of it. The effect can penetrate barriers, but 3 ft. of wood or dirt, 2 ft. of stone, 2 inches of metal, or a thin sheet of lead blocks it. While the target is in range, the doppelganger can continue reading its thoughts, as long as the doppelganger's concentration isn't broken (as if concentrating on a spell). While reading the target's mind, the doppelganger has advantage on Wisdom (Insight) and Charisma (Deception, Intimidation, and Persuasion) checks against the target.
    """

    name = "Doppelganger"
    description = "Medium monstrosity, unaligned"
    challenge_rating = 3
    armor_class = 14
    skills = "Deception +6, Insight +3"
    senses = "Darkvision 60 ft., Passive Perception 11"
    languages = "Common"
    strength = Ability(11)
    dexterity = Ability(18)
    constitution = Ability(14)
    intelligence = Ability(11)
    wisdom = Ability(12)
    charisma = Ability(14)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 52
    hit_dice = "8d8"


class DraftHorse(Monster):
    """
    **Hooves**: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) bludgeoning damage.
    """

    name = "Draft Horse"
    description = "Large beast, unaligned"
    challenge_rating = 0.25
    armor_class = 10
    skills = ""
    senses = "Passive Perception 10"
    languages = ""
    strength = Ability(18)
    dexterity = Ability(10)
    constitution = Ability(12)
    intelligence = Ability(2)
    wisdom = Ability(11)
    charisma = Ability(7)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 19
    hit_dice = "3d10"


class DragonTurtle(Monster):
    """
    **Amphibious**: The dragon turtle can breathe air and water.

    **Multiattack**: The dragon turtle makes three attacks: one with its bite and two with its claws. It can make one tail attack in place of its two claw attacks.

    **Bite**: Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 26 (3d12 + 7) piercing damage.

    **Claw**: Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 16 (2d8 + 7) slashing damage.

    **Tail**: Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 26 (3d12 + 7) bludgeoning damage. If the target is a creature, it must succeed on a DC 20 Strength saving throw or be pushed up to 10 feet away from the dragon turtle and knocked prone.

    **Steam Breath**: The dragon turtle exhales scalding steam in a 60-foot cone. Each creature in that area must make a DC 18 Constitution saving throw, taking 52 (15d6) fire damage on a failed save, or half as much damage on a successful one. Being underwater doesn't grant resistance against this damage.
    """

    name = "Dragon Turtle"
    description = "Gargantuan dragon, neutral"
    challenge_rating = 17
    armor_class = 20
    skills = ""
    senses = "Darkvision 120 ft., Passive Perception 11"
    languages = "Aquan, Draconic"
    strength = Ability(25)
    dexterity = Ability(10)
    constitution = Ability(20)
    intelligence = Ability(10)
    wisdom = Ability(12)
    charisma = Ability(12)
    speed = 20
    swim_speed = 40
    fly_speed = 0
    climb_speed = 0
    hp_max = 341
    hit_dice = "22d20"


class Dretch(Monster):
    """
    **Multiattack**: The dretch makes two attacks: one with its bite and one with its claws.

    **Bite**: Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) piercing damage.

    **Claws**: Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) slashing damage.

    **Fetid Cloud**: A 10-foot radius of disgusting green gas extends out from the dretch. The gas spreads around corners, and its area is lightly obscured. It lasts for 1 minute or until a strong wind disperses it. Any creature that starts its turn in that area must succeed on a DC 11 Constitution saving throw or be poisoned until the start of its next turn. While poisoned in this way, the target can take either an action or a bonus action on its turn, not both, and can't take reactions.
    """

    name = "Dretch"
    description = "Small fiend, chaotic evil"
    challenge_rating = 0.25
    armor_class = 11
    skills = ""
    senses = "Darkvision 60 ft., Passive Perception 9"
    languages = (
        "Abyssal, telepathy 60 ft. (works only with creatures that understand Abyssal)"
    )
    strength = Ability(11)
    dexterity = Ability(11)
    constitution = Ability(12)
    intelligence = Ability(5)
    wisdom = Ability(8)
    charisma = Ability(3)
    speed = 20
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 18
    hit_dice = "4d6"


class Drider(Monster):
    """
    **Fey Ancestry**: The drider has advantage on saving throws against being charmed, and magic can't put the drider to sleep.

    **Innate Spellcasting**: The drider's innate spellcasting ability is Wisdom (spell save DC 13). The drider can innately cast the following spells, requiring no material components:
    At will: dancing lights
    1/day each: darkness, faerie fire

    **Spider Climb**: The drider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.

    **Sunlight Sensitivity**: While in sunlight, the drider has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.

    **Web Walker**: The drider ignores movement restrictions caused by webbing.

    **Multiattack**: The drider makes three attacks, either with its longsword or its longbow. It can replace one of those attacks with a bite attack.

    **Bite**: Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 2 (1d4) piercing damage plus 9 (2d8) poison damage.

    **Longsword**: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands.

    **Longbow**: Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 4 (1d8) poison damage.
    """

    name = "Drider"
    description = "Large monstrosity, chaotic evil"
    challenge_rating = 6
    armor_class = 19
    skills = "Perception +5, Stealth +9"
    senses = "Darkvision 120 ft., Passive Perception 15"
    languages = "Elvish, Undercommon"
    strength = Ability(16)
    dexterity = Ability(16)
    constitution = Ability(18)
    intelligence = Ability(13)
    wisdom = Ability(14)
    charisma = Ability(12)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 30
    hp_max = 123
    hit_dice = "13d10"


class Drow(Monster):
    """
    **Fey Ancestry**: The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.

    **Innate Spellcasting**: The drow's spellcasting ability is Charisma (spell save DC 11). It can innately cast the following spells, requiring no material components:
    At will: dancing lights
    1/day each: darkness, faerie fire

    **Sunlight Sensitivity**: While in sunlight, the drow has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.

    **Shortsword**: Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.

    **Hand Crossbow**: Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 hour. If the saving throw fails by 5 or more, the target is also unconscious while poisoned in this way. The target wakes up if it takes damage or if another creature takes an action to shake it awake.
    """

    name = "Drow"
    description = "Medium humanoid, neutral evil"
    challenge_rating = 0.25
    armor_class = 15
    skills = "Perception +2, Stealth +4"
    senses = "Darkvision 120 ft., Passive Perception 12"
    languages = "Elvish, Undercommon"
    strength = Ability(10)
    dexterity = Ability(14)
    constitution = Ability(10)
    intelligence = Ability(11)
    wisdom = Ability(11)
    charisma = Ability(12)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 13
    hit_dice = "3d8"


class Druid(Monster):
    """
    **Spellcasting**: The druid is a 4th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). It has the following druid spells prepared:

    - Cantrips (at will): druidcraft, produce flame, shillelagh
    - 1st level (4 slots): entangle, longstrider, speak with animals, thunderwave
    - 2nd level (3 slots): animal messenger, barkskin

    **Quarterstaff**: Melee Weapon Attack: +2 to hit (+4 to hit with shillelagh), reach 5 ft., one target. Hit: 3 (1d6) bludgeoning damage, or 6 (1d8 + 2) bludgeoning damage with shillelagh or if wielded with two hands.
    """

    name = "Druid"
    description = "Medium humanoid, any alignment"
    challenge_rating = 2
    armor_class = 11
    skills = "Medicine +4, Nature +3, Perception +4"
    senses = "Passive Perception 14"
    languages = "Druidic plus any two languages"
    strength = Ability(10)
    dexterity = Ability(12)
    constitution = Ability(13)
    intelligence = Ability(12)
    wisdom = Ability(15)
    charisma = Ability(11)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 27
    hit_dice = "5d8"


class Dryad(Monster):
    """
    **Innate Spellcasting**: The dryad's innate spellcasting ability is Charisma (spell save DC 14). The dryad can innately cast the following spells, requiring no material components:

    At will: druidcraft
    3/day each: entangle, goodberry
    1/day each: barkskin, pass without trace, shillelagh

    **Magic Resistance**: The dryad has advantage on saving throws against spells and other magical effects.

    **Speak with Beasts and Plants**: The dryad can communicate with beasts and plants as if they shared a language.

    **Tree Stride**: Once on her turn, the dryad can use 10 ft. of her movement to step magically into one living tree within her reach and emerge from a second living tree within 60 ft. of the first tree, appearing in an unoccupied space within 5 ft. of the second tree. Both trees must be large or bigger.

    **Club**: Melee Weapon Attack: +2 to hit (+6 to hit with shillelagh), reach 5 ft., one target. Hit: 2 (1 d4) bludgeoning damage, or 8 (1d8 + 4) bludgeoning damage with shillelagh.

    **Fey Charm**: The dryad targets one humanoid or beast that she can see within 30 feet of her. If the target can see the dryad, it must succeed on a DC 14 Wisdom saving throw or be magically charmed. The charmed creature regards the dryad as a trusted friend to be heeded and protected. Although the target isn't under the dryad's control, it takes the dryad's requests or actions in the most favorable way it can.
    Each time the dryad or its allies do anything harmful to the target, it can repeat the saving throw, ending the effect on itself on a success. Otherwise, the effect lasts 24 hours or until the dryad dies, is on a different plane of existence from the target, or ends the effect as a bonus action. If a target's saving throw is successful, the target is immune to the dryad's Fey Charm for the next 24 hours.
    The dryad can have no more than one humanoid and up to three beasts charmed at a time.
    """

    name = "Dryad"
    description = "Medium fey, neutral"
    challenge_rating = 1
    armor_class = 11
    skills = "Perception +4, Stealth +5"
    senses = "Darkvision 60 ft., Passive Perception 14"
    languages = "Elvish, Sylvan"
    strength = Ability(10)
    dexterity = Ability(12)
    constitution = Ability(11)
    intelligence = Ability(14)
    wisdom = Ability(15)
    charisma = Ability(18)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 22
    hit_dice = "5d8"


class Duergar(Monster):
    """
    **Duergar Resilience**: The duergar has advantage on saving throws against poison, spells, and illusions, as well as to resist being charmed or paralyzed.

    **Sunlight Sensitivity**: While in sunlight, the duergar has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.

    **Enlarge**: For 1 minute, the duergar magically increases in size, along with anything it is wearing or carrying. While enlarged, the duergar is Large, doubles its damage dice on Strength-based weapon attacks (included in the attacks), and makes Strength checks and Strength saving throws with advantage. If the duergar lacks the room to become Large, it attains the maximum size possible in the space available.

    **War Pick**: Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage, or 11 (2d8 + 2) piercing damage while enlarged.

    **Javelin**: Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 9 (2d6 + 2) piercing damage while enlarged.

    **Invisibility**: The duergar magically turns invisible until it attacks, casts a spell, or uses its Enlarge, or until its concentration is broken, up to 1 hour (as if concentrating on a spell). Any equipment the duergar wears or carries is invisible with it .
    """

    name = "Duergar"
    description = "Medium humanoid, lawful evil"
    challenge_rating = 1
    armor_class = 16
    skills = ""
    senses = "Darkvision 120 ft., Passive Perception 10"
    languages = "Dwarvish, Undercommon"
    strength = Ability(14)
    dexterity = Ability(11)
    constitution = Ability(14)
    intelligence = Ability(11)
    wisdom = Ability(10)
    charisma = Ability(9)
    speed = 25
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 26
    hit_dice = "4d8"


class DustMephit(Monster):
    """
    **Death Burst**: When the mephit dies, it explodes in a burst of dust. Each creature within 5 ft. of it must then succeed on a DC 10 Constitution saving throw or be blinded for 1 minute. A blinded creature can repeat the saving throw on each of its turns, ending the effect on itself on a success.

    **Innate Spellcasting**: The mephit can innately cast sleep, requiring no material components. Its innate spellcasting ability is Charisma.

    **Claws**: Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) slashing damage.

    **Blinding Breath (Recharge 6)**: The mephit exhales a 15-foot cone of blinding dust. Each creature in that area must succeed on a DC 10 Dexterity saving throw or be blinded for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.

    **Variant: Summon Mephits**: The mephit has a 25 percent chance of summoning 1d4 mephits of its kind. A summoned mephit appears in an unoccupied space within 60 feet of its summoner, acts as an ally of its summoner, and can't summon other mephits. It remains for 1 minute, until it or its summoner dies, or until its summoner dismisses it as an action.
    """

    name = "Dust Mephit"
    description = "Small elemental, neutral evil"
    challenge_rating = 0.5
    armor_class = 12
    skills = "Perception +2, Stealth +4"
    senses = "Darkvision 60 ft., Passive Perception 12"
    languages = "Auran, Terran"
    strength = Ability(5)
    dexterity = Ability(14)
    constitution = Ability(10)
    intelligence = Ability(9)
    wisdom = Ability(11)
    charisma = Ability(10)
    speed = 30
    swim_speed = 0
    fly_speed = 30
    climb_speed = 0
    hp_max = 17
    hit_dice = "5d6"
