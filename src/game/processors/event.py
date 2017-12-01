import pygame

from esper import Processor

from game.components import GameInfo, ScriptComponent

class EventProcessor(Processor):
    def __init__(self, game_info):
        self.game_info = game_info
    
    def process(self, delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.world.component_for_entity(self.game_info, GameInfo).running = False
            
            for ent, script_comp in self.world.get_component(ScriptComponent):
                script_comp.script.on_event(event)
