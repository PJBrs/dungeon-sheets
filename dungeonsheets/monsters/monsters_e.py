"""
A collection of monsters from D&D 5e's SRD

This file was autogenerated by https://github.com/stravajiaxen/5e-srd-to-py
"""

from dungeonsheets.monsters.monsters import Monster
from dungeonsheets.stats import Ability



class Eagle(Monster):
    """
    **Keen Sight**: The eagle has advantage on Wisdom (Perception) checks that rely on sight.

    **Talons**: Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.
    """

    name = "Eagle"
    description = "Small beast, unaligned"
    challenge_rating = 0
    armor_class = 12
    skills = "Perception +4"
    senses = "Passive Perception 14"
    languages = ""
    strength = Ability(6)
    dexterity = Ability(15)
    constitution = Ability(10)
    intelligence = Ability(2)
    wisdom = Ability(14)
    charisma = Ability(7)
    speed = 10
    swim_speed = 0
    fly_speed = 60
    climb_speed = 0
    hp_max = 3
    hit_dice = "1d6"


class EarthElemental(Monster):
    """
    **Earth Glide**: The elemental can burrow through nonmagical, unworked earth and stone. While doing so, the elemental doesn't disturb the material it moves through.

    **Siege Monster**: The elemental deals double damage to objects and structures.

    **Multiattack**: The elemental makes two slam attacks.

    **Slam**: Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 14 (2d8 + 5) bludgeoning damage.
    """

    name = "Earth Elemental"
    description = "Large elemental, neutral"
    challenge_rating = 5
    armor_class = 17
    skills = ""
    senses = "Darkvision 60 ft., Tremorsense 60 ft., Passive Perception 10"
    languages = "Terran"
    strength = Ability(20)
    dexterity = Ability(8)
    constitution = Ability(20)
    intelligence = Ability(5)
    wisdom = Ability(10)
    charisma = Ability(5)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 126
    hit_dice = "12d10"


class Efreeti(Monster):
    """
    **Elemental Demise**: If the efreeti dies, its body disintegrates in a flash of fire and puff of smoke, leaving behind only equipment the djinni was wearing or carrying.

    **Innate Spellcasting**: The efreeti's innate spell casting ability is Charisma (spell save DC 15, +7 to hit with spell attacks). It can innately cast the following spells, requiring no material components:

    At will: detect magic
    3/day: enlarge/reduce, tongues
    1/day each: conjure elemental (fire elemental only), gaseous form, invisibility, major image, plane shift, wall of fire

    **Variant: Genie Powers**: Genies have a variety of magical capabilities, including spells. A few have even greater powers that allow them to alter their appearance or the nature of reality.

    Disguises.
    Some genies can veil themselves in illusion to pass as other similarly shaped creatures. Such genies can innately cast the disguise self spell at will, often with a longer duration than is normal for that spell. Mightier genies can cast the true polymorph spell one to three times per day, possibly with a longer duration than normal. Such genies can change only their own shape, but a rare few can use the spell on other creatures and objects as well.
    Wishes.
    The genie power to grant wishes is legendary among mortals. Only the most potent genies, such as those among the nobility, can do so. A particular genie that has this power can grant one to three wishes to a creature that isn't a genie. Once a genie has granted its limit of wishes, it can't grant wishes again for some amount of time (usually 1 year). and cosmic law dictates that the same genie can expend its limit of wishes on a specific creature only once in that creature's existence.
    To be granted a wish, a creature within 60 feet of the genie states a desired effect to it. The genie can then cast the wish spell on the creature's behalf to bring about the effect. Depending on the genie's nature, the genie might try to pervert the intent of the wish by exploiting the wish's poor wording. The perversion of the wording is usually crafted to be to the genie's benefit.

    **Multiattack**: The efreeti makes two scimitar attacks or uses its Hurl Flame twice.

    **Scimitar**: Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage plus 7 (2d6) fire damage.

    **Hurl Flame**: Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 17 (5d6) fire damage.
    """

    name = "Efreeti"
    description = "Large elemental, lawful evil"
    challenge_rating = 11
    armor_class = 17
    skills = ""
    senses = "Darkvision 120 ft., Passive Perception 12"
    languages = "Ignan"
    strength = Ability(22)
    dexterity = Ability(12)
    constitution = Ability(24)
    intelligence = Ability(16)
    wisdom = Ability(15)
    charisma = Ability(16)
    speed = 40
    swim_speed = 0
    fly_speed = 60
    climb_speed = 0
    hp_max = 200
    hit_dice = "16d10"


class Elephant(Monster):
    """
    **Trampling Charge**: If the elephant moves at least 20 ft. straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 12 Strength saving throw or be knocked prone. If the target is prone, the elephant can make one stomp attack against it as a bonus action.

    **Gore**: Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) piercing damage.

    **Stomp**: Melee Weapon Attack: +8 to hit, reach 5 ft., one prone creature. Hit: 22 (3d10 + 6) bludgeoning damage.
    """

    name = "Elephant"
    description = "Huge beast, unaligned"
    challenge_rating = 4
    armor_class = 12
    skills = ""
    senses = "Passive Perception 10"
    languages = ""
    strength = Ability(22)
    dexterity = Ability(9)
    constitution = Ability(17)
    intelligence = Ability(3)
    wisdom = Ability(11)
    charisma = Ability(6)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 76
    hit_dice = "8d12"


class Elk(Monster):
    """
    **Charge**: If the elk moves at least 20 ft. straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.

    **Ram**: Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage.

    **Hooves**: Melee Weapon Attack: +5 to hit, reach 5 ft., one prone creature. Hit: 8 (2d4 + 3) bludgeoning damage.
    """

    name = "Elk"
    description = "Large beast, unaligned"
    challenge_rating = 0.25
    armor_class = 10
    skills = ""
    senses = "Passive Perception 10"
    languages = ""
    strength = Ability(16)
    dexterity = Ability(10)
    constitution = Ability(12)
    intelligence = Ability(2)
    wisdom = Ability(10)
    charisma = Ability(6)
    speed = 50
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 13
    hit_dice = "2d10"


class Erinyes(Monster):
    """
    **Hellish Weapons**: The erinyes's weapon attacks are magical and deal an extra 13 (3d8) poison damage on a hit (included in the attacks).

    **Magic Resistance**: The erinyes has advantage on saving throws against spells and other magical effects.

    **Multiattack**: The erinyes makes three attacks

    **Longsword**: Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage, or 9 (1d10 + 4) slashing damage if used with two hands, plus 13 (3d8) poison damage.

    **Longbow**: Ranged Weapon Attack: +7 to hit, range 150/600 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 13 (3d8) poison damage, and the target must succeed on a DC 14 Constitution saving throw or be poisoned. The poison lasts until it is removed by the lesser restoration spell or similar magic.

    **Variant: Rope of Entanglement**: Some erinyes carry a rope of entanglement (detailed in the Dungeon Master's Guide). When such an erinyes uses its Multiattack, the erinyes can use the rope in place of two of the attacks.
    """

    name = "Erinyes"
    description = "Medium fiend, lawful evil"
    challenge_rating = 12
    armor_class = 18
    skills = ""
    senses = "Truesight 120 ft., Passive Perception 12"
    languages = "Infernal, telepathy 120 ft."
    strength = Ability(18)
    dexterity = Ability(16)
    constitution = Ability(18)
    intelligence = Ability(14)
    wisdom = Ability(14)
    charisma = Ability(18)
    speed = 30
    swim_speed = 0
    fly_speed = 60
    climb_speed = 0
    hp_max = 153
    hit_dice = "18d8"


class Ettercap(Monster):
    """
    **Spider Climb**: The ettercap can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.

    **Web Sense**: While in contact with a web, the ettercap knows the exact location of any other creature in contact with the same web.

    **Web Walker**: The ettercap ignores movement restrictions caused by webbing.

    **Multiattack**: The ettercap makes two attacks: one with its bite and one with its claws.

    **Bite**: Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 6 (1d8 + 2) piercing damage plus 4 (1d8) poison damage. The target must succeed on a DC 11 Constitution saving throw or be poisoned for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.

    **Claws**: Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) slashing damage.

    **Web**: Ranged Weapon Attack: +4 to hit, range 30/60 ft., one Large or smaller creature. Hit: The creature is restrained by webbing. As an action, the restrained creature can make a DC 11 Strength check, escaping from the webbing on a success. The effect ends if the webbing is destroyed. The webbing has AC 10, 5 hit points, is vulnerable to fire damage and immune to bludgeoning damage.

    **Variant: Web Garrote**: Melee Weapon Attack: +4 to hit, reach 5 ft., one Medium or Small creature against which the ettercap has advantage on the attack roll. Hit: 4 (1d4 + 2) bludgeoning damage, and the target is grappled (escape DC 12). Until this grapple ends, the target can't breathe, and the ettercap has advantage on attack rolls against it.
    """

    name = "Ettercap"
    description = "Medium monstrosity, neutral evil"
    challenge_rating = 2
    armor_class = 13
    skills = "Perception +3, Stealth +4, Survival +3"
    senses = "Darkvision 60 ft., Passive Perception 13"
    languages = ""
    strength = Ability(14)
    dexterity = Ability(15)
    constitution = Ability(13)
    intelligence = Ability(7)
    wisdom = Ability(12)
    charisma = Ability(8)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 30
    hp_max = 44
    hit_dice = "8d8"


class Ettin(Monster):
    """
    **Two Heads**: The ettin has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, and knocked unconscious.

    **Wakeful**: When one of the ettin's heads is asleep, its other head is awake.

    **Multiattack**: The ettin makes two attacks: one with its battleaxe and one with its morningstar.

    **Battleaxe**: Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) slashing damage.

    **Morningstar**: Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 14 (2d8 + 5) piercing damage.
    """

    name = "Ettin"
    description = "Large giant, chaotic evil"
    challenge_rating = 4
    armor_class = 12
    skills = "Perception +4"
    senses = "Darkvision 60 ft., Passive Perception 14"
    languages = "Giant, Orc"
    strength = Ability(21)
    dexterity = Ability(8)
    constitution = Ability(17)
    intelligence = Ability(6)
    wisdom = Ability(10)
    charisma = Ability(8)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 85
    hit_dice = "10d10"