import json
from enum import Enum

class PokemonData:
    def __init__(self, pokemon, name, xp, moves):
        self.pokemon = pokemon
        self.name = name
        self.xp = xp
        self.moves = moves

class MoveData:
    def __init__(self, move, pp):
        self.name = move
        self.move = Moves[move]
        self.pp = pp

def load(path):
    info = {}
    with open(path) as file:
        info = json.load(file)
    
    return info

Pokemon = load("assets/data/pokemon.json")
PokeTypes = load("assets/data/poketypes.json")

Moves = load("assets/data/moves.json")

def get_level(pokemon, xp):
    import math

    return ((90 + min(Pokemon[pokemon]['xp_base'], 30)) / 100 / 13) * math.sqrt(7 * xp)

def get_yield(winner, loser):
    l = get_level(loser.pokemon, loser.xp)
    lp = get_level(winner.pokemon, winner.xp)

    return (Pokemon[loser.pokemon]['yield_base'] * l / 5) * ((2 * l + 10)**2.5) / ((l + lp + 10) ** 2.5) + 1