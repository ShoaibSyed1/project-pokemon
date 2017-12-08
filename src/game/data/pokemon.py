import json
from enum import Enum

class PokemonData:
    def __init__(self, pokeinfo, name, hp, xp, lvl, moves):
        self.pokeinfo = pokeinfo
        self.name = name
        self.hp = hp
        self.xp = xp
        self.lvl = lvl
        self.moves = moves


class PokeInfo:
    def __init__(self, pokemon, poketype, move_types):
        self.pokemon = pokemon
        self.poketype = poketype
        self.move_types = move_types

def load(path):
    info = {}
    with open(path) as file:
        info = json.load(file)
    
    return info

Pokemon = load("assets/data/pokemon.json")
PokeType = load("assets/data/poketypes.json")

Move = load("assets/data/moves.json")