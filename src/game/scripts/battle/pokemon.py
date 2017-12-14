import random
from enum import Enum

from game import constants
from game.components import Transform
from game.scripts.script import Script

class PokemonScript(Script):
    def start(self):
        self.transform = self.world.component_for_entity(self.entity, Transform)
    
    def update(self, delta):
        if self.state == PokemonState.RATTLE:
            #Rattle Pokemon
            self.state.rattle.time -= delta
            self.state.rattle.delay += delta

            self.transform.pos.x = self.state.rattle.cur_x + self.state.rattle.offset_x
            self.transform.pos.y = self.state.rattle.cur_y + self.state.rattle.offset_y

            if self.state.rattle.delay >= constants.RATTLE_DELAY:
                #Change rattle position
                self.state.rattle.delay = 0
                self.state.rattle.offset_x = random.randrange(-constants.RATTLE_RANGE, constants.RATTLE_RANGE)
                self.state.rattle.offset_y = random.randrange(-constants.RATTLE_RANGE, constants.RATTLE_RANGE)

            if self.state.rattle.time <= 0:
                #End Rattle State
                self.transform.pos.x = self.state.rattle.cur_x
                self.transform.pos.y = self.state.rattle.cur_y
                self.state = PokemonState.NORMAL
    
    def rattle(self, time):
        self.state = PokemonState.RATTLE
        self.state.rattle = RattleInfo(time, self.transform.pos.x, self.transform.pos.y)

class PokemonState(Enum):
    NORMAL = 0
    RATTLE = 1

class RattleInfo:
    def __init__(self, time, cur_x, cur_y):
        self.time = time
        self.cur_x = cur_x
        self.cur_y = cur_y
        self.offset_x = 0
        self.offset_y = 0
        self.delay = 0