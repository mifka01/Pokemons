from exceptions import MaximumPokemonsReached

class Trainer:
    maximum_pokemons = 6
    def __init__(self, name: str,level: int, pokemons: list):
        self.name = name
        if len(pokemons) <= self.maximum_pokemons:
            self.pokemons = pokemons
        else:
            raise MaximumPokemonsReached
        self.level = level
        self.potions = len(pokemons) / 2 * level
        self.active_pokemon = pokemons[0]
        self.healing = 10 * self.level
        self.attack_power = 10 * self.level


    def use_potion(self):
        print(f"{self.name} healed {self.active_pokemon.name} for {self.healing} health")
        self.active_pokemon.heal(self.healing)
        self.potions -= 1

    def change_active_pokemon(self, pokemon_number):
        self.active_pokemon = self.pokemons[pokemon_number]
        print(f"{self.name} has switched active pokemon to {self.pokemons[pokemon_number].name}")



