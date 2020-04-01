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

    def attack(self, spell, target):
        """Increase pokemon's health by given amount."""
        if not self.active_pokemon.knocked_out:
            print(f"{self.name} is attacking with {self.active_pokemon.name} on {target.name}'s {target.active_pokemon.name}'")
            self.active_pokemon.attack(spell, target.active_pokemon)
        else:
            print(f"{self.name}'s {self.active_pokemon.name} is knocked out and cant attack")

    def use_potion(self):
        """Uses potions to heal currently active Pokemon."""
        print(f"{self.name} healed {self.active_pokemon.name} for {self.healing} health")
        self.active_pokemon.heal(self.healing)
        self.potions -= 1

    def change_active_pokemon(self, pokemon_number):
        """Changes active Pokemon by given index."""
        if pokemon_number < len(self.pokemons) and pokemon_number >= 0:
            if self.pokemons[pokemon_number].knocked_out:
                print(f"{self.pokemons[pokemon_number].name} is knocked you have to choose another Pokemon")
            elif self.pokemons[pokemon_number] == self.active_pokemon:
                print(f"{self.active_pokemon.name} is already your active pokemon")
            else:
                self.active_pokemon = self.pokemons[pokemon_number]
                print(f"{self.name} has switched active Pokemon to {self.pokemons[pokemon_number].name}")


