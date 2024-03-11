class Unit:
    def __init__(self, name, unit_type, weapon_type, power_level):
        self.name = name
        self.unit_type = unit_type
        self.weapon_type = weapon_type
        self.power_level = power_level

    def describe(self):
        print(f"Name: {self.name}, Type: {self.unit_type}, Weapon: {self.weapon_type}, Power Level: {self.power_level}")


class Army:
    def __init__(self):
        self.units = []

    def add_unit(self, unit):
        self.units.append(unit)
        print(f"Added {unit.name} to the army.")

    def describe_army(self):
        print("Army Composition:")
        for unit in self.units:
            unit.describe()


if __name__ == "__main__":
    tactical_squad = Unit("Intercessors", "Infantry", "Bolter", 5)
    dreadnought = Unit("Dreadnought", "Vehicle", "Multi-Melta", 15)
    primarch = Unit("Roboute Guilliman", "Primarch", "Emperor's sword", 50)
    infiltrators = Unit("Infiltrators", "Specialists", "Sniper rifles", 10)

    my_army = Army()
    my_army.add_unit(tactical_squad)
    my_army.add_unit(dreadnought)
    my_army.add_unit(primarch)
    my_army.add_unit(infiltrators)

    my_army.describe_army()
