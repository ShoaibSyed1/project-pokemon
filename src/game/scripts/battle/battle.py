from enum import Enum

from game.loaders import EntityLoader
from game.scripts.script import Script

class BattleController(Script):
    def __init__(self, battle_info):
        self.battle_info = battle_info
        self.state = BattleState.INITIALIZING

    def start(self):
        pass
    
    def update(self, delta):
        if self.state == BattleState.INITIALIZING:
            self.pokemon_front = self.world.create_entity()
            EntityLoader.load("battle/front", self.world,
                                                   {'sprite': "pokemon/battle/" + self.battle_info['front_info']['pokemon']})
            self.state = BattleState.WAITING

class BattleState(Enum):
    INITIALIZING = 0
    WAITING = 1