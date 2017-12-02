import pygame

from esper import Processor

from game.components import GameInfo, InputComponent,  ScriptComponent

class EventProcessor(Processor):
    def __init__(self, game_info):
        self.game_info = game_info
    
    def process(self, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.world.component_for_entity(self.game_info, GameInfo).running = False
            elif event.type == pygame.KEYDOWN:
                key = event.key
                for ent, inp in self.world.get_component(InputComponent):
                    if key in inp.keys:
                        inp.keys[key] = True
            elif event.type == pygame.KEYUP:
                key = event.key
                for ent, inp in self.world.get_component(InputComponent):
                    if key in inp.keys:
                        inp.keys[key] = False
                    