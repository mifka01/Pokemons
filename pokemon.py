import json
import random


class Pokemon:
    def __init__(self, name):
        with open('data/pokemons.json') as json_file:
            data = json.load(json_file)
            base_stats = data[name]["base_stats"]
            self.name = name
            self.level = 4
            self.experiences = 0
            self.types = base_stats["types"]
            self.max_health = base_stats["hp"]
            self.current_health = self.max_health
            self.knocked_out = False
            self.attack_power = base_stats["attack"]
            self.defense = base_stats["defense"]
            self.grown_rate = base_stats["grown_rate"]
            self.sp_atk = base_stats["sp_atk"]
            self.sp_def = base_stats["sp_def"]
            self.speed = base_stats["speed"]
            self.total = self.max_health + self.attack_power + self.defense + self.sp_atk + self.sp_def + self.speed
            self.defense_stats = data[name]["defense_stats"]
            self.spells = self.get_spells(data)

    def __repr__(self):
        return f"{self.name} is currently level {self.level}, is {self.types} type and has {self.current_health} of {self.max_health} maximum health"

    def lose_health(self, amount: int):
        """Decrease pokemon's health by given amount."""

        if self.current_health - amount > 0:
            self.current_health -= amount
            print(
                f"{self.name} now has {self.current_health} of {self.max_health} maximum health")
        elif not self.knocked_out:
            self.knocked_out = True
            self.current_health = 0
            print(f"{self.name} was knocked out")

    def heal(self, amount: int):
        """Increase pokemon's health by given amount."""

        if self.current_health + amount < self.max_health:
            self.current_health += amount
        else:
            self.current_health = self.max_health

        if self.current_health > 0:
            self.knocked_out = False
        print(
            f"{self.name} now has {self.current_health} of {self.max_health} maximum health")

    def attack(self, spell, target):
        """Attacks given target by given spell."""
        target.lose_health(self.damage_calculation(spell, target))

    def damage_calculation(self, spell, target):
        """Calculates damage of attacking Pokemon."""

        T = int(self.speed / 2)
        P = random.randint(0, 255)
        critical = 1
        stab = 1
        defense_type = 0
        
        for pokemon_spell in self.spells:
            if spell in pokemon_spell.keys():
                spell_power = pokemon_spell[spell]["spell_power"]
                spell_type = pokemon_spell[spell]["spell_type"]

        if T is P:
            critical = (2*self.level+5)/(self.level+5)

        for poke_type in self.types:
            origin = poke_type[0:3].lower() + "_weakness"
            defense_type += target.defense_stats[origin]
            if poke_type == spell_type:
                stab = 1.5
            else:
                stab = 1
        modifier = defense_type * random.uniform(0.85, 1.00) * critical * stab
        damage = (((((2*self.level)/5)+2)* spell_power *    
                   (target.attack_power/target.defense)/50)+2) * modifier

        return int(damage)

    def get_spells(self, data):
        """Add spells to Pokemon based od his level."""
        levels = data[self.name]["spells"].keys()
        spells = []
        for lv in range(0,self.level+1):
            if str(lv) in levels:
                spells.append(data[self.name]["spells"][str(lv)])
        return spells
