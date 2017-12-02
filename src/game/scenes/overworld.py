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

        self.scripts = []
    
    def start(self):
        from pygame import Rect

        import Box2D
        from pymunk.vec2d import Vec2d

        from game.components import Animation, Sprite, Transform, ScriptComponent
        from game.processors import AnimationProcessor, EventProcessor, RenderProcessor, ScriptProcessor
        from game.scripts import PlayerScript

        self.game_info = self.world.create_entity(GameInfo())

        self.world.create_entity(
            Animation(16, 16, 8, 8, 50, 0, 4),
            Sprite(pygame.image.load("assets/image.png")),
            Transform(pos=Vec2d(3, 3), scale=Vec2d(8, 8)))
        
        player_script = PlayerScript()

        self.player = self.world.create_entity(
            Sprite(pygame.image.load("assets/player/player.png"), Rect(0, 0, 32, 48)),
            ScriptComponent(player_script),
            Transform(pos=Vec2d(64, 64), scale=Vec2d(2, 2)))        

        self.world.add_processor(AnimationProcessor(), 2)
        self.world.add_processor(EventProcessor(self.game_info))
        self.world.add_processor(RenderProcessor(self.game.window))
        self.world.add_processor(ScriptProcessor())

        for ent, script_comp in self.world.get_component(ScriptComponent):
            script_comp.script.entity = ent
            script_comp.script.world = self.world
            script_comp.script.start()

    def update(self, delta):
        self.game.running = self.world.component_for_entity(self.game_info, GameInfo).running
        self.world.process(delta)