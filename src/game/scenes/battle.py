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
        
        from game.components import Animation, ScriptComponent, ScriptComponent, Sprite, Transform
        from game.components.ui import Element
        from game.processors import AnimationProcessor, EventListener, EventProcessor, RenderProcessor, ScriptProcessor
        from game.scripts.ui import Button, UiController

        self.game_info = self.world.create_entity(GameInfo())

        self.camera = self.world.create_entity(Transform(Vector2(0, 0)))

        self.world.create_entity(
            EventListener([pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]),
            ScriptComponent(UiController())
        )

        self.world.create_entity(
            Animation(64, 16, 32, 16, -1),
            Element(Vector2(32, 16)),
            ScriptComponent(Button()),
            Sprite(pygame.image.load("assets/ui/battle/button.png")),
            Transform(Vector2(0, 416), scale=Vector2(5, 5))
        )

        self.world.add_processor(AnimationProcessor(), 2)
        self.world.add_processor(EventProcessor(self.game_info))
        self.world.add_processor(RenderProcessor(self.game.window, self.camera))
        self.world.add_processor(ScriptProcessor())

        for ent, script_comp in self.world.get_component(ScriptComponent):
            script_comp.script.entity = ent
            script_comp.script.world = self.world
            script_comp.script.start()
    
    def update(self, delta):
        self.game.running = self.world.component_for_entity(self.game_info, GameInfo).running
        self.world.process(delta)