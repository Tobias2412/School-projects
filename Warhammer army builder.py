class Army:
    def __init__(self, name, faction):
        self.name = name
        self.faction = faction
        self.units = []

    def add_unit(self, unit):
        self.units.append(unit)
        print(f"{unit.name} added to the army.")

    def remove_unit(self, unit_name):
        self.units = [unit for unit in self.units if unit.name != unit_name]
        print(f"{unit_name} removed from the army.")

    def display_army(self):
        print(f"Army name: {self.name}, Faction: {self.faction}")
        for unit in self.units:
            unit.display_unit()

class Unit:
    def __init__(self, name, type, weapon_type, power_level):
        self.name = name
        self.type = type
        self.weapon_type = weapon_type
        self.power_level = power_level


    def display_unit(self):
        print(f"Name: {self.name}, Type: {self.type}, Weapon type: {self.weapon_type}, Power level: {self.power_level}")

orks = Army("Bad Moons", "WAAAAAAAAAGH")
shoota_boiz = Unit("Shootaz", "Boyz","Shoota", 5)
choppa_boiz = Unit("Choppaz", "Boyz", "Choppa", 5)
orks.add_unit(shoota_boiz)
orks.add_unit(choppa_boiz)

orks.display_army()
