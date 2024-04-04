'''So, you want build an army in Warhammer 40K? Let's do it!'''
class Unit:  # These are the attributes we want the different units in the army to have.
    def __init__(self, name, unit_type, weapon_type, power_level):
        self.name = name
        self.unit_type = unit_type
        self.weapon_type = weapon_type
        self.power_level = power_level

    def describe(self):  # This line prints the different attributes to the given unit.
        print(f"Name: {self.name}, Type: {self.unit_type}, Weapon: {self.weapon_type}, Power Level: {self.power_level}")

    def getName(self):
        return self.name

    def getUnitType(self):
        return self.unit_type

    def getWeaponType(self):
        return self.weapon_type

    def getPowerLevel(self):
        return self.power_level


class Army:  # Here are the units we want added to the army.
    def __init__(self):
        self.units = []

    def add_unit(self, unit):  # This adds units to the army.
        self.units.append(unit)
        print(f"Added {unit.name} to the army.")

    def describe_army(self):  # This is the composition of the army.
        print("Army Composition:")
        for unit in self.units:
            unit.describe()

    def getUnits(self):
        return self.units


if __name__ == "__main__":  # Your army explained in details.
    tactical_squad = Unit("Intercessors", "Infantry", "Bolter", 5)
    infiltrators = Unit("Infiltrators", "Specialists", "Sniper rifles", 10)
    dreadnought = Unit("Dreadnought", "Vehicle", "Multi-Melta", 15)
    desolators = Unit("Desolators", "Anti-vehicle", "Rocket launchers", 20)
    chaplain = Unit("Chaplain", "Hero character", "Psychic powers", 25)
    primarch = Unit("Roboute Guilliman", "Primarch", "Emperor's sword", 50)

# Behold! Your mighty army!
    my_army = Army()
    my_army.add_unit(tactical_squad)
    my_army.add_unit(infiltrators)
    my_army.add_unit(dreadnought)
    my_army.add_unit(desolators)
    my_army.add_unit(chaplain)
    my_army.add_unit(primarch)

    my_army.describe_army()

    print("\n-----\n")

    print(my_army.getUnits()[2].getName())

print("\nNow,bring glory to mankind! For the Emper
