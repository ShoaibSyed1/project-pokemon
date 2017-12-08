from enum import Enum

class PokemonData:
    def __init__(self, poketype, name, hp, xp, lvl, moves):
        self.poketype = poketype
        self.name = name
        self.hp = hp
        self.xp = xp
        self.lvl = lvl
        self.moves = moves

#TODO: Load pokemon from json
#TODO: Load moves from json
class PokeType(Enum):
    Bulbasaur = 0