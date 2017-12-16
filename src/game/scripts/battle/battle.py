from enum import Enum

from game.loaders import EntityLoader
from game.scripts.script import Script

class BattleController(Script):
    def __init__(self, battle_info):
        self.battle_info = battle_info
        self.state = BattleState.WAITING

    def start(self):
        self.pokemon_front = EntityLoader.load("battle/front", self.world,
                              {'sprite': "pokemon/battle/" + self.battle_info['front_info']['pokemon']})
        self.pokemon_back = EntityLoader.load("battle/back", self.world,
                              {'sprite': "pokemon/battle/" + self.battle_info['front_info']['pokemon']})
    
    def update(self, delta):
        pass

class BattleState(Enum):
    WAITING = 0