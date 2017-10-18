def find_damage(attack_event):
    if attack_event.weapon.type[0] = "physical":
        damage_calculator = physical_damage

    return damage_calculator(attack_event)

def physical_damage(attack_event):
    # retrive property weapon type string
    weapon_type = attack_event.attacker.weapon.type[1]

    attribute = attack_event.attacker.attributes(weapon_type)
    return attack_event.attacker.weapon.value * (1 + .05*attribute)

class Attack_Event:
    def __init__(self, attacker, target, weapon):
        self.attacker = attacker
        self.target = target
        self.weapon = weapon

class Weapon:
    def __init__(self, type, value):
        self.type = [physical, str]
        self.value = value

class Actor:
    def __init__(self, attributes, weapon):
        self.attributes = attributes
        weapon = weapon


weapon 
