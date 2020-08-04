from exceptions import MaximumPokemonsReached

class Trainer:
    """
    Trainer class
    Parameters
    ----------
    name: name of trainer,
    x_pos: x position on game screen
    y_pos: y position on game screen
    Description
    ----------
    Trainer class can hold pokemons and it's parent for Player and Npc
    """
    maximum_pokemons = 6
    def __init__(self, name: str, x_pos: int, y_pos: int):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.trainer_image = None
        self.pokemons = []
        self.level = 1
        self.potions = None
        self.active_pokemon = None
        self.healing = 10 * self.level
        self.attack_power = 10 * self.level

    def __str__(self):
        return self.name

    def set_trainer_image(self, path: str):
        """
        Function    : setter for trainer_image
        Parameters  : self, path: str (path to image)
        Return      : None
        Examples of Usage:
            self.set_trainer_image(path: str)
        """
        self.trainer_image = path

    def level_one(self, pokemon: object):
        """
        Function    : first level for Trainer
        Description : sets first pokemon and level one stuff to Trainer class
        Parameters  : self, pokemon: Pokemon object
        Return      : None
        Examples of Usage:
            self.level_one(Bulbasaur: Pokemon)
        """
        self.add_pokemon(pokemon)
        self.potions = len(self.pokemons) / 2 * self.level
        self.active_pokemon = self.pokemons[0]

    def add_pokemon(self, pokemon: object):
        """
        Function    : add new pokemon to Trainer
        Description : appends new pokemon to list of Trainers pokemons
        Parameters  : self, pokemon: Pokemon object
        Return      : None
        Examples of Usage:
            self.add_pokemon(Bulbasaur: Pokemon)
        """
        if len(self.pokemons) <= self.maximum_pokemons:
            self.pokemons.append(pokemon)
        else:
            raise MaximumPokemonsReached

    def level_up(self):
        """
        Function    : level up Trainer
        Description : adds one level to self.level
        Parameters  : self
        Return      : None
        Examples of Usage:
            self.level_up()
        """
        self.level += 1
        

    def attack(self, spell, target):
        """
        Function    : attack the enemy trainer
        Description : deal damage to enemy active pokemon
        Parameters  : self, spell: str, target: Trainer object
        Return      : None
        Examples of Usage:
            self.attack("Scratch", "Dan: Trainer")
        """
        if not self.active_pokemon.knocked_out:
            print(f"{self.name} is attacking with {self.active_pokemon.name} on {target.name}'s {target.active_pokemon.name}'")
            self.active_pokemon.attack(spell, target.active_pokemon)
        else:
            print(f"{self.name}'s {self.active_pokemon.name} is knocked out and cant attack")

    def use_potion(self):
        """
        Function    : trainer uses one of his potions
        Description : heals currently active Pokemon
        Parameters  : self
        Return      : None
        Examples of Usage:
            self.use_potion()
        """
        print(f"{self.name} healed {self.active_pokemon.name} for {self.healing} health")
        self.active_pokemon.heal(self.healing)
        self.potions -= 1

    def change_active_pokemon(self, pokemon_number):
        """
        Function    : change active trainers Pokemon
        Description : heals currently active Pokemon
        Parameters  : self, pokemon_number: int
        Return      : None
        Examples of Usage:
            self.change_active_pokemon(4)
        """
        if pokemon_number >= 0 and pokemon_number < len(self.pokemons):
            if self.pokemons[pokemon_number].knocked_out:
                print(f"{self.pokemons[pokemon_number].name} is knocked you have to choose another Pokemon")
            elif self.pokemons[pokemon_number] == self.active_pokemon:
                print(f"{self.active_pokemon.name} is already your active pokemon")
            else:
                self.active_pokemon = self.pokemons[pokemon_number]
                print(f"{self.name} has switched active Pokemon to {self.pokemons[pokemon_number].name}")
    
    


