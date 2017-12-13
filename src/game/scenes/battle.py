import esper

from game.components import GameInfo
from game.scenes.scene import Scene

class Battle(Scene):
    def __init__(self, game):
        self.game = game

        self.world = esper.World()

        self.camera = None
        self.game_info = None
    
    def start(self):
        import pygame
        from pygame.math import Vector2
        
        from game import uuids
        from game.components import Animation, ScriptComponent, ScriptComponent, Sprite, Transform, Uuid
        from game.components.ui import Element
        from game.loaders import SpriteLoader, UiLoader
        from game.processors import AnimationProcessor, EventListener, EventProcessor, RenderProcessor, ScriptProcessor
        from game.scripts.ui import Button, UiController

        self.game_info = self.world.create_entity(GameInfo())

        self.camera = self.world.create_entity(Transform({'pos': Vector2(0, 0)}), Uuid(uuids.CAMERA))

        self.world.create_entity(
            EventListener({
                'events': ["KEYDOWN", "KEYUP", "MOUSEBUTTONDOWN", "MOUSEBUTTONUP", "MOUSEMOTION"]
            }),
            ScriptComponent(UiController())
        )

        loader = UiLoader("battle/battle")
        loader.start(self.world)

        self.world.add_processor(AnimationProcessor(), 2)
        self.world.add_processor(EventProcessor(self.game_info))
        self.world.add_processor(RenderProcessor(self.game.window, self.camera))
        self.world.add_processor(ScriptProcessor(), 3)
    
    def update(self, delta):
        self.game.running = self.world.component_for_entity(self.game_info, GameInfo).running
        self.world.process(delta)