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


