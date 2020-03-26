from pokemon import Pokemon
from trainer import Trainer

charmander = Pokemon("Charmander", 1, "Fire")

growlithe = Pokemon("Growlithe", 1, "Fire")
bulbasaur = Pokemon("Bulbasaur", 1, "Grass")
oddish = Pokemon("Oddish", 1, "Grass")
squirtle = Pokemon("Squirtle", 1, "Water")
psyduck = Pokemon("Psyduck", 1, "Water")

torchic = Pokemon("Torchic",1,"Fire")
vulpix = Pokemon("Vulpix",1,"Fire")
paras = Pokemon("Paras",1,"Grass")
bellsprout = Pokemon("Bellsprout",1,"Grass")
poliwag = Pokemon("Poliwag",1,"Water")
seel = Pokemon("Seel",1,"Water")

blaine = Trainer("Blaine",1,[torchic, vulpix, paras, bellsprout, poliwag, seel])
flint = Trainer("Flint", 1, [charmander,growlithe,bulbasaur,oddish,squirtle,psyduck])

print(blaine.active_pokemon)
print(flint.active_pokemon)

print("Pokemon battle begins")
print("\n")
print("Round one")
blaine.active_pokemon.attack(flint.active_pokemon)
flint.use_potion()
print("\n")
print("Round two")
blaine.change_active_pokemon(4)
flint.change_active_pokemon(2)
print("\n")
print("Round three")
blaine.active_pokemon.attack(flint.active_pokemon)
flint.active_pokemon.attack(blaine.active_pokemon)
print("\n")
print("Round four")
blaine.use_potion()
flint.use_potion()
print("\n")

