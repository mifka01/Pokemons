from pokemon import Pokemon
from trainer import Trainer



class PokemonBattle:
    def __init__(self, trainer1, trainer2, num_of_pokemons: int):
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.num_of_pokemons = num_of_pokemons
        self.battle_end = False
        self.main_loop()

    def main_loop(self):
        """Starts main loop for Pokemon Battle."""
        while not self.battle_end:

# FROM HERE IT'S TESTING CODE
            print(f"{self.trainer1.name}'s Turn")
            trainer1_usable_spells = []
            for spell in self.trainer1.active_pokemon.spells:
                trainer1_usable_spells.append(*spell)
            print("Choose spells which you want to attack with")
            print(trainer1_usable_spells)
            trainer1_round = input()
            if trainer1_round in trainer1_usable_spells:
                self.trainer1.attack(trainer1_round, self.trainer2)
            print(f"{self.trainer2.name}'s Turn")
            trainer2_usable_spells= []
            for spell in self.trainer2.active_pokemon.spells:
                trainer2_usable_spells.append(*spell)
            print(trainer2_usable_spells)
            trainer2_round = input()
            if trainer2_round in trainer2_usable_spells:
                self.trainer2.attack(trainer2_round, self.trainer1)

charmander = Pokemon("Charmander")
squirtle = Pokemon("Squirtle")
pikachu = Pokemon("Pikachu")
weedle = Pokemon("Weedle")
caterpie = Pokemon("Caterpie")
bulbasaur = Pokemon("Bulbasaur")

duke = Trainer("Duke",1,[charmander,squirtle,pikachu,weedle,caterpie,bulbasaur])
sam = Trainer("Sam",1,[pikachu,squirtle,charmander,weedle,caterpie,bulbasaur])
PokemonBattle(duke,sam,2)