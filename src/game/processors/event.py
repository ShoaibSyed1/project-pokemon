import pygame

from esper import Processor

from game.components.game_info import GameInfo

class EventProcessor(Processor):
    def __init__(self, game_info):
        self.game_info = game_info
    
    def process(self, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.world.component_for_entity(self.game_info, GameInfo).running = False
