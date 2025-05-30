from dungeonsheets import spells, weapons
from dungeonsheets.features.features import Feature, FeatureSelector


# Features
class EldritchInvocation(Feature):
    """In your study of occult lore, you have unearthed eldritch invocations,
    fragments of forbidden knowledge that imbue you with an abiding magical
    ability.

    At 2nd level, you gain two eldritch invocations of your choice. Your
    invocation options are detailed at the end of the class description. When
    you gain certain warlock levels, you gain additional invocations of your
    choice, as shown in the Invocations Known column of the Warlock table.

    Additionally, when you gain a level in this class, you can choose one of
    the invocations you know and replace it with another invocation that you
    could learn at that level.

    """

    name = "Eldritch Invocations"
    source = "Warlock"
    at_will_spells = ()

    def cast_spell_at_will(self, spell):
        s = spell()
        s.level = 0
        if "M" in s.components:
            c = list(s.components)
            c.remove("M")
            s.components = tuple(c)
        self.spells_known += (s,)
        self.spells_prepared += (s,)

    def __init__(self, owner):
        super().__init__(owner)
        for s in self.at_will_spells:
            self.cast_spell_at_will(s)


class PactOfTheChain(Feature):
    """You learn the find familiar spell and can cast it as a ritual. The spell
    doesn't count against your number of spells known.

    When you cast the spell, you can choose one of the normal forms for your
    familiar or one of the following special forms: imp, pseudodragon, quasit,
    or sprite. Additionally, when you take the Attack action, you can forgo one
    of your own attacks to allow your familiar to make one attack of its own.

    """

    name = "Pact of the Chain"
    source = "Warlock"
    spells_known = spells_prepared = (spells.FindFamiliar,)


class PactOfTheBlade(Feature):
    """You can use your action to create a pact weapon in your empty hand. You can
    choose the form that this melee weapon takes each time you create it (see
    chapter 5 for weapon options). You are proficient with it while you wield
    it. This weapon counts as magical for the purpose of overcoming resistance
    and immunity to nonmagical attacks and damage.

    Your pact weapon disappears if it is more than 5 feet away from you for 1
    minute or more. It also disappears if you use this feature again, if you
    dismiss the weapon (no action required), or if you die.

    You can transform one magic weapon into your pact weapon by performing a
    special ritual while you hold the weapon. You perform the ritual over the
    course of 1 hour, which can be done during a short rest. You can then
    dismiss the weapon, shunting it into an extradimensional space, and it
    appears whenever you create your pact weapon thereafter. You can't affect
    an artifact or a sentient weapon in this way. The weapon ceases being your
    pact weapon if you die, if you perform the 1-hour ritual on a different
    weapon, or if you use a 1-hour ritual to break your bond to it. The weapon
    appears at your feet if it is in the extradimensional space when the bond
    breaks.

    """

    name = "Pact of the Blade"
    source = "Warlock"


class PactOfTheTome(Feature):
    """Your patron gives you a grimoire called a Book of Shadows. When you gain
    this feature, choose three cantrips from any class's spell list. While the
    book is on your person, you can cast those cantrips at will. They don't
    count against your number of cantrips known.

    If you lose your Book of Shadows, you can perform a 1-hour ceremony to
    receive a replacement from your patron. This ceremony can be performed
    during a short or long rest, and it destroys the previous book. The book
    turns to ash when you die.

    """

    name = "Pact of the Tome"
    source = "Warlock"


class PactOfTheTalisman(Feature):
    """Your patron gives you an amulet, a talisman that can aid the wearer when
    the need is great. When the wearer fails an ability check, they can add a d4
    to the roll, potentially turning the roll into a success. This benefit can be
    used a number of times equal to your proficiency bonus, and all expended uses
    are restored when you finish a long rest. If you lose the talisman, you can
    perform a 1-hour ceremony to receive a replacement from your patron.
    This ceremony can be performed during a short or long rest, and it
    destroys the previous amulet. The talisman turns to ash when you die.

    """

    name = "Pact of the Talisman"
    source = "Warlock"


class PactBoon(FeatureSelector):
    """Select a Pact Boon by choosing in feature_choices:

    pact of the chain

    pact of the blade

    pact of the tome

    pact of the talisman

    """

    options = {
        "chain": PactOfTheChain,
        "pact of the chain": PactOfTheChain,
        "blade": PactOfTheBlade,
        "pact of the blade": PactOfTheBlade,
        "tome": PactOfTheTome,
        "pact of the tome": PactOfTheTome,
        "talisman": PactOfTheTalisman,
        "pact of the talisman": PactOfTheTalisman,
    }
    name = "Pact Boon (Select One)"
    source = "Warlock"


class MysticArcanum(Feature):
    """At 11th level, your patron bestows upon you a magical secret called an
    arcanum. Choose one 6th-level spell from the warlock spell list as this
    arcanum.

    You can cast your arcanum spell once without expending a spell slot. You
    must finish a long rest before you can do so again.

    At higher levels, you gain more warlock spells of your choice that can be
    cast in this way: one 7th-level spell at 13th level, one 8th-level spell at
    15th level, and one 9th-level spell at 17th level. You regain all uses of
    your Mystic Arcanum when you finish a long rest.

    """

    name = "Mystic Arcanum"
    source = "Warlock"


class EldritchMaster(Feature):
    """At 20th level, you can draw on your inner reserve of mystical power while
    entreating your patron to regain expended spell slots. You can spend 1
    minute entreating your patron for aid to regain all your expended spell
    slots from your Pact Magic feature. Once you regain spell slots with this
    feature, you must finish a long rest before you can do so again.

    """

    name = "Eldritch Master"
    source = "Warlock"


class EldritchVersatility(Feature):
    """Whenever you reach a level in this class that grants the Ability Score
    Improvement feature, you can do one of the following, representing a change
    of focus in your occult studies:

    - Replace one cantrip you learned from this class's Pact Magic feature with
      another cantrip from the warlock spell list.
    - Replace the option you chose for the Pact Boon feature with one of that
      feature's other options.
    - If you're 12th level or higher, replace one spell from your Mystic
      Arcanum feature with another warlock spell of the same level.

    If this change makes you ineligible for any of your Eldritch Invocations,
    you must also replace them now, choosing invocations for which you qualify.

    """

    name = "Eldritch Versatility"
    source = "Warlock"

# The Archfey
class FeyPresence(Feature):
    """Starting at 1st level, your patron bestows upon you the ability to project
    the beguiling and fearsome presence of the fey. As an action, you can cause
    each creature in a 10-foot cube originating from you to make a Wisdom
    saving throw against your warlock spell save DC.

    The creatures that fail their saving throws are all charmed or frightened
    by you (your choice) until the end of your next turn. Once you use this
    feature, you can't use it again until you finish a short or long rest.

    """

    name = "Fey Presence"
    source = "Warlock (Archfey Patron)"


class MistyEscape(Feature):
    """Starting at 6th level, you can vanish in a puff of mist in response to
    harm. When you take damage, you can use your reaction to turn invisible and
    teleport up to 60 feet to an unoccupied space you can see. You remain
    invisible until the start of your next turn or until you attack or cast a
    spell. Once you use this feature, you can't use it again until you finish a
    short or long rest.

    """

    name = "Misty Escape"
    source = "Warlock (Archfey Patron)"


class BeguilingDefenses(Feature):
    """Beginning at 10th level, your patron teaches you how to turn the
    mind-affecting magic of your enemies against them. You are immune to being
    charmed, and when another creature attempts to charm you, you can use your
    reaction to attempt to turn the charm back on that creature. The creature
    must succeed on a Wisdom saving throw against your warlock spell save DC or
    be charmed by you for 1 minute or until the creature takes any damage.

    """

    name = "Beguiling Defenses"
    source = "Warlock (Archfey Patron)"


class DarkDelirium(Feature):
    """Starting at 14th level, you can plunge a creature into an illusory
    realm. As an action, choose a creature that you can see within 60 feet of
    you. It must make a Wisdom saving throw against your warlock spell save
    DC. On a failed save, it is charmed or frightened by you (your choice) for
    1 minute or until your concentration is broken (as if you are concentrating
    on a spell).

    This effect ends early if the creature takes any damage. Until this
    illusion ends, the creature thinks it is lost in a misty realm, the
    appearance of which you choose. The creature can see and hear only itself,
    you, and the illusion. You must finish a short or long rest before you can
    use this feature again.

    """

    name = "Dark Delirium"
    source = "Warlock (Archfey Patron)"


# The Fiend Patron
class DarkOnesBlessing(Feature):
    """Starting at 1st level, when you reduce a hostile creature to 0 hit points,
    you gain temporary hit points equal to your Charisma modifier + your
    warlock level (minimum of 1)

    """

    _name = "Dark One's Blessing"
    source = "Warlock (The Fiend Patron)"

    @property
    def name(self):
        level = self.owner.Warlock.level
        mod = self.owner.charisma.modifier
        return self._name + " ({:d} HP)".format(level + mod)


class DarkOnesOwnLuck(Feature):
    """Starting at 6th level, you can call on your patron to alter fate in your
    favor. When you make an ability check or a saving throw, you can use this
    feature to add a d10 to your roll. You can do so after seeing the initial
    roll but before any of the roll's effects occur.

    Once you use this feature, you can't use it again until you finish a short
    or long rest.

    """

    name = "Dark One's Own Luck"
    source = "Warlock (The Fiend Patron)"


class FiendishResilience(Feature):
    """Starting at 10th level, you can choose one damage type when you finish a
    short or long rest. You gain resistance to that damage type until you
    choose a different one with this feature. Damage from magical weapons or
    silver weapons ignores this resistance.

    """

    name = "Fiendish Resilience"
    source = "Warlock (The Fiend Patron)"


class HurlThroughHell(Feature):
    """Starting at 14th level, when you hit a creature with an attack, you can use
    this feature to instantly transport the target through the lower
    planes. The creature disappears and hurtles through a nightmare landscape.

    At the end of your next turn, the target returns to the space it previously
    occupied, or the nearest unoccupied space. If the target is not a fiend, it
    takes 10d10 psychic damage as it reels from its horrific experience.

    Once you use this feature, you can't use it again until you finish a long
    rest.

    """

    name = "Hurl Through Hell"
    source = "Warlock (The Fiend Patron)"


# Great Old One
class AwakenedMind(Feature):
    """Starting at 1st level, your alien knowledge gives you the ability to touch
    the minds of other creatures. You can communicate telepathically with any
    creature you can see within 30 feet of you. You don't need to share a
    language with the creature for it to understand your telepathic utterances,
    but the creature must be able to understand at least one language.

    """

    name = "Awakened Mind"
    source = "Warlock (Great Old One Patron)"


class EntropicWard(Feature):
    """At 6th level, you learn to magically ward yourself against attack and to
    turn an enemy's failed strike into good luck for yourself. When a creature
    makes an attack roll against you, you can use your reaction to impose
    disadvantage on that roll. If the attack misses you, your next attack roll
    against the creature has advantage if you make it before the end of your
    next turn. Once you use this feature, you can't use it again until you
    finish a short or long rest.

    """

    name = "Entropic Ward"
    source = "Warlock (Great Old One Patron)"


class ThoughtShield(Feature):
    """Starting at 10th level, your thoughts can't be read by telepathy or other
    means unless you allow it. You also have resistance to psychic damage, and
    whenever a creature deals psychic damage to you, that creature takes the
    same amount of damage that you do.

    """

    name = "Thought Shield"
    source = "Warlock (Great Old One Patron)"


class CreateThrall(Feature):
    """At 14th level, you gain the ability to infect a humanoid's mind with the
    alien magic of your patron. You can use your action to touch an
    incapacitated humanoid. That creature is then charmed by you until a remove
    curse spell is cast on it, the charmed condition is removed from it, or you
    use this feature again. You can communicate telepathically with the charmed
    creature as long as the two of you are on the same plane of existence.

    """

    name = "Create Thrall"
    source = "Warlock (Great Old One Patron)"


# Undying Patron
class AmongTheDead(Feature):
    """Starting at 1st level, you learn the spare the dying cantrip, which counts
    as a warlock cantrip for you. You also have advantage on saving throws
    against any disease. Additionally, undead have difficulty harming you. If
    an undead targets you directly with an attack or a harmful spell, that
    creature must make a Wisdom saving throw against your spell save DC (an
    undead needn't make the save when it includes you in an area effect, such
    as the explosion of fireball). On a failed save, the creature must choose a
    new target or forfeit targeting someone instead of you, potentially wasting
    the attack or spell. On a successful save, the creature is immune to this
    effect for 24 hours. An undead is also immune to this effect for 24 hours
    if you target it with an attack or a harmful spell.

    """

    name = "Among the Dead"
    source = "Warlock (The Undying Patron)"
    spells_known = spells_prepared = (spells.SpareTheDying,)


class DefyDeath(Feature):
    """Starting at 6th level, you can give yourself vitality when you cheat death
    or when you help someone else cheat it. You can regain hit points equal to
    1d8 + your Constitution modifier (minimum of 1 hit point) when you succeed
    on a death saving throw or when you stabilize a creature with spare the
    dying. Once you use this feature, you can't use it again until you finish a
    long rest.

    """

    name = "Defy Death"
    source = "Warlock (The Undying Patron)"


class UndyingNature(Feature):
    """Beginning at 10th level, you can hold your breath indefinitely, and you
    don't require food, water, or sleep, although you still require rest to
    reduce exhaustion and still benefit from finishing short and long rests. In
    addition, you age at a slower rate. For every 10 years that pass, your body
    ages only 1 year, and you are immune to being magically aged.

    """

    name = "Undying Nature"
    source = "Warlock (The Undying Patron)"


class IndestructibleLife(Feature):
    """When you reach 14th level, you partake of some of the true secrets
    of the Undying. On your turn, you can use a bonus action to regain
    hit points equal to 1d8 + your warlock level. Additionally, if you
    put a severed body part of yours back in place when you use this
    feature, the part reattaches. Once you use this feature, you can't
    use it again until you finish a short or long rest.

    """

    name = "Indestructible Life"
    source = "Warlock (The Undying Patron)"


# The Celestial
class HealingLight(Feature):
    """At 1st level, you gain the ability to channel celestial energy to heal
    wounds. You have a pool of d6s that you spend to fuel this healing. The
    number of dice in the pool equals 1 + your warlock level. As a bonus
    action, you can heal one creature you can see within 60 feet of you,
    spending dice from the pool. The maximum number of dice you can spend at
    once equals your Charisma modifier (minimum of one die). Roll the
    dice you spend, add them together, and restore a number of hit points equal
    to the total. Your pool regains all expended dice when you finish a long
    rest.

    """

    _name = "Healing Light"
    source = "Warlock (The Celestial Patron)"

    @property
    def name(self):
        num = 1 + self.owner.Warlock.level
        return self._name + " ({:d}d6/LR)".format(num)


class WarlockRadiantSoul(Feature):
    """Starting at 6th level, your link to the Celestial allows you to serve as a
    conduit for radiant energy. You have resistance to radiant damage, and when
    you cast a spell that deals radiant or fire damage, you can add your
    Charisma modifier to one radiant or fire damage roll of that spell against
    one of its targets.

    """

    name = "WarlockRadiant Soul"
    source = "Warlock (The Celestial Patron)"


class CelestialResilience(Feature):
    """Starting at 10th level, you gain temporary hit points whenever you finish a
    short or long rest. These temporary hit points equal your warlock level +
    your Charisma modifier. Additionally, choose up to five creatures you can
    see at the end of the rest. Those creatures each gain temporary hit points
    equal to half your warlock level + your Charisma modifier.

    """

    _name = "Celestial Resilience"
    source = "Warlock (The Celestial Patron)"


class SearingVengeance(Feature):
    """Starting at 14th level, the radiant energy you channel allows you to resist
    death. When you have to make a death saving throw at the start of your
    turn, you can instead spring back to your feet with a burst of radiant
    energy. You regain hit points equal to half your hit point maximum, and
    then you stand up if you so choose. Each creature of your choice that is
    within 30 feet of you takes radiant damage equal to 2d8 + your Charisma
    modifier, and it is blinded until the end of the current turn. Once you use
    this feature, you can't use it again until you finish a long rest.

    """

    name = "Searing Vengeance"
    source = "Warlock (The Celestial Patron)"


# Hexblade
class HexbladesCurse(Feature):
    """Starting at 1st level, you gain the ability to place a baleful curse on
    someone. As a bonus action, choose one creature you can see within 30 feet
    of you. The target is cursed for 1 minute. The curse ends early if the
    target dies, you die, or you are incapacitated. Until the curse ends, you
    gain the following benefits:

    - You gain a bonus to damage rolls against the cursed target. The
      bonus equals your proficiency bonus.
    - Any attack roll you make against the cursed target is a critical
      hit on a roll of 19 or 20 on the d20.
    - If the cursed target dies, you regain hit points equal to your
      warlock level + your Charisma modifier (minimum of 1 hit point).

    You can't use this feature again until you finish a short or long rest.

    """

    name = "Hexblades Curse"
    source = "Warlock (Hexblade)"


class HexWarrior(Feature):
    """At 1st level, you acquire the training necessary to effectively arm
    yourself for battle. You gain proficiency with medium armor, shields, and
    martial weapons.

    The influence of your patron also allows you to mystically channel your
    will through a particular weapon. Whenever you finish a long rest, you can
    touch one weapon that you are proficient with and that lacks the two-handed
    property. When you attack with that weapon, you can use your Charisma
    modifier, instead of Strength or Dexterity, for the attack and damage
    rolls. This benefit lasts until you finish a long rest. If you later gain
    the Pact of the Blade feature, this benefit extends to every pact weapon
    you conjure with that feature, no matter the weapon's type.

    """

    name = "Hex Warrior"
    source = "Warlock (Hexblade)"

    def weapon_func(self, weapon: weapons.Weapon, **kwargs):
        """
        Swap the weapon's attack bonus modifier for Charisma if
        it is higher than STR/DEX bonus.
        """
        if weapon.is_finesse:
            abils = {
                "strength": self.owner.strength.modifier,
                "dexterity": self.owner.dexterity.modifier,
                "charisma": self.owner.charisma.modifier,
            }
        else:
            abils = {
                weapon.ability: getattr(self.owner, weapon.ability).modifier,
                "charisma": self.owner.charisma.modifier,
            }
        weapon.ability = max(abils, key=abils.get)


class AccursedSpecter(Feature):
    """Starting at 6th level, you can curse the soul of a person you slay,
    temporarily binding it to your service. When you slay a humanoid, you can
    cause its Spirit to rise from its corpse as a specter, the statistics for
    which are in the Monster Manual. When the specter appears, it gains
    temporary hit points equal to half your warlock level. Roll initiative for
    the specter, which has its own turns. It obeys your verbal commands, and it
    gains a special bonus to its attack rolls equal to your Charisma modifier
    (minimum of +0).

    The specter remains in your service until the end of your next long rest,
    at which point it vanishes to the afterlife.

    Once you bind a specter with this feature, you can't use the feature again
    until you finish a long rest.

    """

    name = "Accursed Specter"
    source = "Warlock (Hexblade)"


class ArmorOfHexes(Feature):
    """At 10th level, your hex grows more powerful. If the target cursed by your
    Hexblade's Curse hits you with an attack roll, you can use your reaction to
    roll a d6. On a 4 or higher, the attack instead misses you, regardless of
    its roll.

    """

    name = "Armor of Hexes"
    source = "Warlock (Hexblade)"


class MasterOfHexes(Feature):
    """Starting at 14th level, you can spread your Hexblade's Curse from a slain
    creature to another creature. When the creature cursed by your Hexblade's
    Curse dies, you can apply the curse to a different creature you can see
    within 30 feet of you, provided you aren't incapacitated. When you apply
    the curse in this way, you don't regain hit points from the death of the
    previously cursed creature.

    """

    name = "Master of Hexes"
    source = "Warlock (Hexblade)"


# The Fathomless Patron
class TentacleOfTheDeeps(Feature):
    """You can magically summon a spectral tentacle that strikes at your foes.
    As a bonus action, you create a 10-foot-long tentacle at a point you can
    see within 60 feet of you. The tentacle lasts for 1 minute or until you
    use this feature to create another tentacle.

    When you create the tentacle, you can make a melee spell attack against one
    creature within 10 feet of it. On a hit, the target takes 1d8 cold damage,
    and its speed is reduced by 10 feet until the start of your next turn.
    When you reach 10th level in this class, the damage increases to 2d8.

    As a bonus action on your turn, you can move the tentacle up to 30 feet and
    repeat the attack. You can summon the tentacle a number of times equal to your
    proficiency bonus, and you regain all expended uses when you finish a long rest.

    """

    name = "Tentacle of the Deeps"
    source = "Warlock (The Fathomless Patron)"


class GiftOfTheSea(Feature):
    """
    You gain a swimming speed of 40 feet, and you can breathe underwater.
    """

    name = "Gift of the Sea"
    source = "Warlock (The Fathomless Patron)"


class OceanicSoul(Feature):
    """You are now even more at home in the depths. You gain resistance to cold
    damage. In addition, when you are fully submerged, any creature that is also
    fully submerged can understand your speech, and you can understand theirs.

    """

    name = "Oceanic Soul"
    source = "Warlock (The Fathomless Patron)"


class GuardianCoil(Feature):
    """Your Tentacle of the Deeps can defend you and others, interposing itself
    between them and harm. When you or a creature you can see takes damage while
    within 10 feet of the tentacle, you can use your reaction to choose one of
    those creatures and reduce the damage to that creature by 1d8. When you reach
    10th level in this class, the damage reduced by the tentacle increases to 2d8.

    """

    name = "Guardian Coil"
    source = "Warlock (The Fathomless Patron)"


class GraspingTentacles(Feature):
    """You learn the spell Evard's black tentacles. It counts as a warlock spell
    for you, but it doesn't count against the number of spells you know.
    You can also cast it once without a spell slot, and you regain the ability
    to do so when you finish a long rest.

    Whenever you cast this spell, your patron's magic bolsters you, granting you a
    number of temporary hit points equal to your warlock level. Moreover, damage
    can't break your concentration on this spell.

    """
    _name = "Grasping Tentacles"
    source = "Warlock (The Fathomless Patron)"
    spells_known = spells_prepared = (spells.EvardsBlackTentacles,)

    @property
    def name(self):
        num = self.owner.Warlock.level
        return self._name + " ({:d} HP)".format(num)


class FathomlessPlunge(Feature):
    """You can magically open temporary conduits to watery destinations. As an
    action, you can teleport yourself and up to five other willing creatures that
    you can see within 30 feet of you. Amid a whirl of tentacles, you all vanish
    and then reappear up to 1 mile away in a body of water you've seen
    (pond size or larger) or within 30 feet of it, each of you appearing in an
    unoccupied space within 30 feet of the others.

    Once you use this feature, you can't use it again until you finish a
    short or long rest.

    """

    name = "Fathomless Plunge"
    source = "Warlock (The Fathomless Patron)"


class GeniesVessel(Feature):
    """Your patron gifts you a magical vessel that grants you a measure of the genie's power.
    The vessel is a Tiny object, and you can use it as a spellcasting focus for your warlock spells.
    You decide what the object is, or you can determine what it is randomly by rolling on the Genie's Vessel table.

    ====  ===========================
    d6    Vessel
    ====  ===========================
    1     Oil Lamp
    2     Urn
    3     Ring with a Compartment
    4     Stoppered Bottle
    5     Hollow Statuette
    6     Ornate Lantern
    ====  ===========================

    While you are touching the vessel, you can use it in the following ways:

    **Bottled Respite**. As an action, you can magically vanish and enter your vessel, which remains
    in the space you left. The interior of the vessel is an extradimensional space in the shape of a
    20-foot-radius cylinder, 20 feet high, and resembles your vessel. The interior is appointed with
    cushions and low tables and is a comfortable temperature. While inside, you can hear the area around
    your vessel as if you were in its space. You can remain inside the vessel up to a number of hours
    equal to twice your proficiency bonus. You exit the vessel early if you use a bonus action to leave,
    if you die, or if the vessel is destroyed. When you exit the vessel, you appear in the unoccupied
    space closest to it. Any objects left in the vessel remain there until carried out, and if the
    vessel is destroyed, every object stored there harmlessly appears in the unoccupied spaces closest
    to the vessel's former space. Once you enter the vessel, you can't enter again until you finish a long rest.

    **Genie's Wrath**. Once during each of your turns when you hit with an attack roll, you can deal extra damage
    to the target equal to your proficiency bonus. The type of this damage is determined by your patron:
    bludgeoning (dao), thunder (djinni), fire (efreeti), or cold (marid).

    The vessel's AC equals your spell save DC. Its hit points equal your warlock level plus your proficiency bonus,
    and it is immune to poison and psychic damage.

    If the vessel is destroyed or you lose it, you can perform a 1-hour ceremony to receive a replacement from your patron.
    This ceremony can be performed during a short or long rest, and the previous vessel is destroyed if it still exists.
    The vessel vanishes in a flare of elemental power when you die.

    """

    name = "Genie's Vessel"
    source = "Warlock (The Genie Patron)"


class ElementalGift(Feature):
    """You begin to take on characteristics of your patron's kind. You now have resistance to a damage type
    determined by your patron's kind: bludgeoning (dao), thunder (djinni), fire (efreeti), or cold (marid).

    In addition, as a bonus action, you can give yourself a flying speed of 30 feet that lasts for 10 minutes,
    during which you can hover. You can use this bonus action a number of times equal to your proficiency bonus,
    and you regain all expended uses when you finish a long rest.

    """

    name = "Elemental Gift"
    source = "Warlock (The Genie Patron)"


class SanctuaryVessel(Feature):
    """When you enter your Genie's Vessel via the Bottled Respite feature, you can now choose up to five willing
    creatures that you can see within 30 feet of you, and the chosen creatures are drawn into the vessel with you.

    As a bonus action, you can eject any number of creatures from the vessel, and everyone is ejected if you leave
    or die or if the vessel is destroyed.

    In addition, anyone (including you) who remains within the vessel for at least 10 minutes gains the benefit
    of finishing a short rest, and anyone can add your proficiency bonus to the number of hit points they regain
    if they spend any Hit Dice as part of a short rest there.

    """

    name = "Sanctuary Vessel"
    source = "Warlock (The Genie Patron)"


class LimitedWish(Feature):
    """You entreat your patron to grant you a small wish. As an action, you can speak your desire to your
    Genie's Vessel, requesting the effect of one spell that is 6th level or lower and has a casting time of 1 action.
    The spell can be from any class's spell list, and you don't need to meet the requirements in that spell,
    including costly components; the spell simply takes effect as part of this action.

    Once you use this feature, you can't use it again until you finish 1d4 long rests.

    """

    name = "Limited Wish"
    source = "Warlock (The Genie Patron)"


# All Invocations
Invocation = EldritchInvocation


# PHB
class AgonizingBlast(Invocation):
    """When you cast eldritch blast, add your Charisma modifier to the damage it
    deals on a hit.

    """

    name = "Agonizing Blast"


class ArmorOfShadows(Invocation):
    """You can cast mage armor on yourself at will, without expending a spell slot
    or material components.

    """

    name = "Armor of Shadows"
    at_will_spells = (spells.MageArmor,)


class AscendantStep(Invocation):
    """You can cast levitate on yourself at will, without expending a spell slot
    or material components.

    **Prerequisite**: 9th level.

    """

    name = "Ascendant Step"
    at_will_spells = (spells.Levitate,)


class BeastSpeech(Invocation):
    """You can cast speak with animals at will, without expending a spell slot."""

    name = "Beast Speech"
    at_will_spells = (spells.SpeakWithAnimals,)


class BeguilingInfluence(Invocation):
    """You gain proficiency in the Deception and Persuasion skills."""

    name = "Beguiling Influence"
    needs_implementation = True


class BewitchingWhispers(Invocation):
    """You can cast compulsion once using a warlock spell slot. You can't do so
    again until you finish a long rest.

    **Prerequisite**: 7th Level.
    """

    name = "Bewitching Whispers"


class BookOfAncientSecrets(Invocation):
    """You can now inscribe magical rituals in your Book of Shadows. Choose two
    1st-level spells that have the ritual tag from any class's spell list. The
    spells appear in the book and don't count against the number of spells you
    know. With your Book of Shadows in hand, you can cast the chosen spells as
    rituals. You can't cast the spells except as rituals, unless you've learned
    them by some other means. You can also cast a warlock spell you know as a
    ritual if it has the ritual tag.

    On your adventures, you can add other ritual spells to your Book of
    Shadows. When you find such a spell, you can add it to the book if the
    spell's level is equal to or less than half your warlock level (rounded up)
    and if you can spare the time to transcribe the spell. For each level of
    the spell, the transcription process takes 2 hours and costs 50 gp for the
    rare inks needed to inscribe it.

    """

    name = "Book of Ancient Secrets"


class ChainsOfCarceri(Invocation):
    """You can cast hold monster at will-targeting a celestial, fiend, or
    elemental-without expending a spell slot or material components. You must
    finish a long rest before you can use this invocation on the same creature
    again.

    **Prerequisites**: 15th level, Pact of the Chain Feature.
    """

    name = "Chains of Carceri"


class DevilsSight(Invocation):
    """You can see normally in darkness, both magical and nonmagical, to a
    distance of 120 feet.

    """

    name = "Devil's Sight"


class DreadfulWord(Invocation):
    """You can cast confusion once using a warlock spell slot. You can't do so
    again until you finish a long rest.

    """

    name = "Dreadful Word"


class EldritchSight(Invocation):
    """You can cast detect magic at will, without expending a spell slot."""

    name = "Eldritch Sight"
    at_will_spells = (spells.DetectMagic,)


class EldritchSpear(Invocation):
    """When you cast eldritch blast, its range is 300 feet."""

    name = "Eldritch Spear"


class EyesOfTheRuneKeeper(Invocation):
    """
    You can read all writing.

    """

    name = "Eyes of the Rune Keeper"


class FiendishVigor(Invocation):
    """You can cast false life on yourself at will as a 1st-level spell, without
    expending a spell slot or material components.

    """

    name = "Fiendish Vigor"
    at_will_spells = (spells.FalseLife,)


class GazeOfTwoMinds(Invocation):
    """You can use your action to touch a willing humanoid and perceive through
    its senses until the end of your next turn. As long as the creature is on
    the same plane of existence as you, you can use your action on subsequent
    turns to maintain this connection, extending the duration until the end of
    your next turn. While perceiving through the other creature's senses, you
    benefit from any special senses possessed by that creature, and you are
    blinded and deafened to your own surroundings.

    """

    name = "Gaze of Two Minds"


class LifeDrinker(Invocation):
    """When you hit a creature with your pact weapon, the creature takes extra
    necrotic damage equal to your Charisma modifier (minimum 1).

    **Prerequisite**: 12th Level, Pact of the Blade.
    """

    name = "Life Drinker"
    needs_implementation = True


class MaskOfManyFaces(Invocation):
    """You can cast disguise self at will, without expending a spell slot."""

    name = "Mask of Many Faces"
    at_will_spells = (spells.DisguiseSelf,)


class MasterOfMyriadForms(Invocation):
    """
    You can cast alter self at will, without expending a spell slot.

    **Prerequisite**: 15th Level.
    """

    name = "Master of Myriad Forms"
    at_will_spells = (spells.AlterSelf,)


class MinionsOfChaos(Invocation):
    """You can cast conjure elemental once using a warlock spell slot. You can't
    do so again until you finish a long rest.

    **Prerequisite**: 9th Level.
    """

    name = "Minions of Chaos"


class MireTheMind(Invocation):
    """You can cast slow once using a warlock spell slot. You can't do so again
    until you finish a long rest.

    """

    name = "Mire the Mind"


class MistyVisions(Invocation):
    """You can cast silent image at will, without expending a spell slot or
    material components.

    """

    name = "Misty Visions"
    at_will_spells = (spells.SilentImage,)


class OneWithShadows(Invocation):
    """When you are in an area of dim light or darkness, you can use your action
    to become invisible until you move or take an action or a reaction.

    **Prerequisite**: 5th Level.
    """

    name = "One with Shadows"


class OtherworldlyLeap(Invocation):
    """You can cast jump on yourself at will, without expending a spell slot or
    material components.

    **Prerequisite**: 9th Level.

    """

    name = "Otherworldly Leap"
    at_will_spells = (spells.Jump,)


class RepellingBlast(Invocation):
    """When you hit a creature with eldritch blast, you can push the creature up
    to 10 feet away from you in a straight line.

    """

    name = "Repelling Blast"


class SculptorOfFlesh(Invocation):
    """You can cast polymorph once using a warlock spell slot. You can't do so
    again until you finish a long rest.

    **Prerequisite**: 7th Level.
    """

    name = "Sculptor of Flesh"


class SignOfIllOmen(Invocation):
    """You can cast bestow curse once using a warlock spell slot. You can't do so
    again until you finish a long rest.

    **Prerequisite**: 5th Level.

    """

    name = "Sign of Ill Omen"


class ThiefOfFiveFates(Invocation):
    """You can cast bane once using a warlock spell slot. You can't do so again
    until you finish a long rest.

    """

    name = "Thief of Five Fates"


class ThirstingBlade(Invocation):
    """You can attack with your pact weapon twice, instead of once, whenever you
    take the Attack action on your turn.

    **Prerequisite**: 5th Level, Pact of the Blade.
    """

    name = "Thirsting Blade"


class VisionsOfDistantRealms(Invocation):
    """
    You can cast arcane eye at will, without expending a spell slot.

    **Prerequisite**: 15th level.
    """

    name = "Visions of Distant Realms"
    at_will_spells = (spells.ArcaneEye,)


class VoiceOfTheChainMaster(Invocation):
    """You can communicate telepathically with your familiar and perceive through
    your familiar's senses as long as you are on the same plane of
    existence. Additionally, while perceiving through your familiar's senses,
    you can also speak through your familiar in your own voice, even if your
    familiar is normally incapable of speech.

    **Prerequisite**: Pact of the Chain.

    """

    name = "Voice of the Chain Master"


class WhispersOfTheGrave(Invocation):
    """You can cast speak with dead at will, without expending a spell slot.

    **Prerequsite**: 9th Level.

    """

    name = "Whispers of the Grave"
    at_will_spells = (spells.SpeakWithDead,)


class WitchSight(Invocation):
    """You can see the true form of any shapechanger or creature concealed by
    illusion or transmutation magic while the creature is within 30 feet of you
    and within line of sight.

    """

    name = "Witch Sight"


# XGTE
class AspectOfTheMoon(Invocation):
    """You no longer need to sleep and can't be forced to sleep by any means. To
    gain the benefits of a long rest, you can spend all 8 hours doing light
    activity, such as reading your Book of Shadows and keeping watch.

    **Prerequisite**: Pact of the Tome.
    """

    name = "Aspect of the Moon"


class CloakOfFlies(Invocation):
    """As a bonus action, you can surround yourself with a magical aura that looks
    like buzzing flies. The aura extends 5 feet from you in every direction,
    but not through total cover. It lasts until you're incapacitated or you
    dismiss it as a bonus action.

    The aura grants you advantage on Charisma
    (Intimidation) checks but disadvantage on all other Charisma checks. Any
    other creature that starts its turn in the aura takes poison damage equal
    to your Charisma modifier (minimum of O damage).

    Once you use this invocation, you can't use it again until you finish a
    short or long rest.

    **Prerequisite**: 5th level.
    """

    name = "Cloak of Flies"


class EldritchSmite(Invocation):
    """Once per turn when you hit a creature with your pact weapon, you can expend
    a warlock spell slot to deal an extra 1d8 force damage to the target, plus
    another 1d8 per level of the spell slot, and you can knock the target
    prone if it is Huge or smaller.

    **Prerequisite**: 5th level, Pact of the Blade.

    """

    name = "Eldritch Smite"


class GhostlyGaze(Invocation):
    """As an action, you gain the ability to see through solid objects to a range
    of 30 feet. Within that range, you have darkvision if you don't already
    have it. This special sight lasts for 1 minute or until your concentration
    ends (as if you were concentrating on a spell). During that time, you
    perceive objects as ghostly, transparent images.

    Once you use this invocation, you can't use it again until you finish a
    short or long rest.

    **Prerequisite**: 7th level.
    """

    name = "Ghostly Gaze"


class GiftOfTheDepths(Invocation):
    """You can breathe underwater, and you gain a swimming speed equal to your
    walking speed. You can also cast water breathing once without expending a
    spell slot. You regain the ability to do so when you finish a long rest.

    **Prerequisite**: 5th level.
    """

    name = "Gift of the Depths"


class GiftOfTheEverLivingOnes(Invocation):
    """Whenever you regain hit points while your familiar is within 100 feet
    ofyou, treat any dice rolled to determine the hit points you regain as
    having rolled their maximum value for you.

    **Prerequisite**: Pact of the Chain.
    """

    name = "Gift of the Ever-Living Ones"


class GraspOfHadar(Invocation):
    """Once on each of your turns when you hit a creature with your eldritcli
    blast, you can move that creature in a straight line 10 feet closer to you.

    """

    name = "Grasp of Hadar"


class ImprovedPactWeapon(Invocation):
    """You can use any weapon you summon with your Pact of the Blade feature as a
    spellcasting focus for your warlock spells.

    In addition, the weapon gains a +1 bonus to its attack and damage rolls,
    unless it is a magic weapon that already has a bonus to those rolls.

    Finally, the weapon you conjure can be a shortbow, longbow, light crossbow,
    or heavy crossbow.

    **Prerequisite**: Pact of the Blade.
    """

    name = "Improved Pact Weapon"

    def weapon_func(self, weapon: weapons.Weapon, **kwargs):
        """
        Add +1 to attack and damage if magic is not already magic.
        """
        if (weapon.attack_bonus == 0) or (weapon.damage_bonus == 0):
            weapon.attack_bonus += 1
            weapon.damage_bonus += 1


class LanceOfLethargy(Invocation):
    """Once on each of your turns when you hit a creature with your eldritch
    blast, you can reduce that creature's speed by 10 feet until the end of your
    next turn.

    """

    name = "Lance of Lethargy"


class MaddeningHex(Invocation):
    """As a bonus action, you cause a psychic disturbance around the target cursed
    by your hex spell or by a warlock feature of yours, such as Hexblade's
    Curse or Sign of Ill Omen. When you do so, you deal psychic damage to the
    cursed target and each creature of your choice that you can see within 5
    feet of it. The psychic damage equals your Charisma modifier (minimum of 1
    damage). To use this invocation, you must be able to see the cursed
    target, and it must be within 30 feet of you.

    **Prerequisite**: 5th level.
    """

    name = "Maddening Hex"


class RelentlessHex(Invocation):
    """Your curse creates a temporary bond between you and your target. As a bonus
    action, you can magically telerport up to 30 feet to an unoccupied space
    you can see within 5 feet of the target cursed by your hex spell or by a
    warlock feature of yours, such as Hexblade's Curse or Sign of 111 Omen. To
    teleport in this way, you must be able to see the cursed target.

    """

    name = "Relentless Hex"


class ShroudOfShadow(Invocation):
    """You can cast invisibility at will, without expending a spell slot.

    **Prerequisite**: 15th Level.

    """

    at_will_spells = (spells.Invisibility,)
    name = "Shroud of Shadow"


class TombOfLevistus(Invocation):
    """As a reaction when you take damage, you can entomb yourself in ice, which
    melts away at the end of your next turn. You gain 10 temporary hit points
    per warlock level, which take as much of the triggering damage as
    possible. Immediately after you take the damage, you gain vulnerability to
    fire damage, your speed is reduced to 0, and you are incapacitated. These
    effects, including any remaining temporary hit points, all end when the ice
    melts.

    Once you use this invocation, you can't use it again until you finish a
    short or long rest.

    **Prerequisite**: 5th Level.

    """

    name = "Tomb of Levistus"


class TrickstersEscape(Invocation):
    """You can cast freedom ofmovement once on yourself without expending a spell
    slot. You regain the ability to do so when you finish a long rest.

    """

    name = "Tricksters Escape"


# TCE
class BondOfTheTalisman(Invocation):
    """While someone else is wearing your talisman, you can use your action to teleport
    to the unoccupied space closest to them, provided the two of you are on the same
    plane of existence. The wearer of your talisman can do the same thing, using their action
    to teleport to you. The teleportation can be used a number of times equal to
    your proficiency bonus, and all expended uses are restored when you finish a long rest.

    **Prerequisite**: 12th Level, Pact of the Talisman.

    """

    name = "Bond of the Talisman"


class EldritchMind(Invocation):
    """You have advantage on Constitution saving throws that
    you make to maintain your concentration on a spell.

    """

    name = "Eldritch Mind"


class FarScribe(Invocation):
    """A new page appears in your Book of Shadows. With your permission, a creature can use its action to
    write its name on that page, which can contain a number of names equal to your proficiency bonus.
    You can cast the *sending* spell, targeting a creature whose name is on the page, without using a
    spell slot and without using material components. To do so, you must write the message on the page.
    The target hears the message in their mind, and if the target replies, their message appears on the
    page, rather than in your mind. The writing disappears after 1 minute.
    As an action, you can magically erase a name on the page by touching it.

    **Prerequisite**: 5th Level, Pact of the Tome.

    """

    name = "Far Scribe"


class GiftOfTheProtectors(Invocation):
    """A new page appears in your Book of Shadows. With your permission, a creature can use its action to
    write its name on that page, which can contain a number of names equal to your proficiency bonus.
    When any creature whose name is on the page is reduced to 0 hit points but not killed outright,
    the creature magically drops to 1 hit point instead. Once this magic is triggered, no creature can benefit
    from it until you finish a long rest. As an action, you can magically erase a name on the page by touching it.

    **Prerequisite**: 9th Level, Pact of the Tome.

    """

    name = "Gift of the Protectors"


class InvestmentOfTheChainMaster(Invocation):
    """When you cast find familiar, you infuse the summoned familiar with a measure of your eldritch
    power, granting the creature the following benefits:

    * The familiar gains either a flying speed or a swimming speed (your choice) of 40 feet.
    * As a bonus action, you can command the familiar to take the Attack action.
    * The familiar's weapon attacks are considered magical for the purpose of overcoming immunity and resistance to nonmagical attacks.
    * If the familiar forces a creature to make a saving throw, it uses your spell save DC.
    * When the familiar takes damage, you can use your reaction to grant it resistance against that damage.

    **Prerequisite**: Pact of the Chain.
    """

    name = "Investment of the Chain Master"


class ProtectionOfTheTalisman(Invocation):
    """When the wearer of your talisman fails a saving throw, they can add a d4 to the roll,
    potentially turning the save into a success. This benefit can be used a number of times
    equal to your proficiency bonus, and all expended uses are restored when you finish a long rest.

    **Prerequisite**: 7th Level, Pact of the Talisman.
    """

    name = "Protection of the Talisman"


class RebukeOfTheTalisman(Invocation):
    """When the wearer of your talisman is hit by an attacker you can see within 30 feet of you, you can use
    your reaction to deal psychic damage to the attacker equal to your proficiency bonus and push it up to 10
    feet away from the talisman's wearer.

    **Prerequisite**: Pact of the Talisman.
    """

    name = "Rebuke of the Talisman"


class UndyingServitude(Invocation):
    """You can cast animate dead without using a spell slot. Once you do so, you can't cast it
    in this way again until you finish a long rest.

    **Prerequisite**: 5th Level.
    """

    name = "Undying Servitude"
