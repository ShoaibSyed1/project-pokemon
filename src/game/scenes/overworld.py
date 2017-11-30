import esper
import pygame

from game.scenes.scene import Scene

from game.components import GameInfo

class Overworld(Scene):
    def __init__(self, game):
        self.game = game

        self.world = esper.World()
        
        self.game_info = None

        self.player = None
    
    def start(self):
        from pygame import Rect

        from game.components import Animation, Sprite, Transform
        from game.math import Vector2
        from game.processors import AnimationProcessor, EventProcessor, RenderProcessor

        self.game_info = self.world.create_entity(GameInfo())

        self.world.create_entity(
            Animation(16, 16, 8, 8, 50, 0, 4),
            Sprite(pygame.image.load("assets/image.png")),
            Transform(pos=Vector2(3, 3), scale=Vector2(8, 8)))

        self.player = self.world.create_entity(
            Sprite(pygame.image.load("assets/player/player.png"), Rect(0, 0, 32, 48)),
            Transform(pos=Vector2(64, 64), scale=Vector2(2, 2)))

        self.world.add_processor(AnimationProcessor(), 2)
        self.world.add_processor(EventProcessor(self.game_info))
        self.world.add_processor(RenderProcessor(self.game.window))

    def update(self, delta):
        self.game.running = self.world.component_for_entity(self.game_info, GameInfo).running
        self.world.process(delta)