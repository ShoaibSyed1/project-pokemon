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
        from pygame.math import Vector2

        from game.components import Animation, InputComponent, Sprite, Transform, ScriptComponent, Tile
        from game.processors import AnimationProcessor, EventProcessor, RenderProcessor, ScriptProcessor, TileProcessor
        from game.scripts import PlayerScript

        self.game_info = self.world.create_entity(GameInfo())

        self.world.create_entity(
            Animation(16, 16, 8, 8, 50, 0, 4),
            Sprite(pygame.image.load("assets/image.png")),
            Tile(Vector2(0, 0)),
            Transform(pos=Vector2(3, 3), scale=Vector2(8, 8)))
        
        player_script = PlayerScript()

        self.player = self.world.create_entity(
            InputComponent([pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]),
            Sprite(pygame.image.load("assets/player/player.png"), Rect(0, 0, 32, 48)),
            ScriptComponent(player_script),
            Tile(Vector2(0, 0), move_speed=1),
            Transform(pos=Vector2(64, 64), scale=Vector2(2, 2)))        

        self.world.add_processor(AnimationProcessor(), 2)
        self.world.add_processor(EventProcessor(self.game_info))
        self.world.add_processor(RenderProcessor(self.game.window))
        self.world.add_processor(ScriptProcessor())
        self.world.add_processor(TileProcessor())

        for ent, script_comp in self.world.get_component(ScriptComponent):
            script_comp.script.entity = ent
            script_comp.script.world = self.world
            script_comp.script.start()

    def update(self, delta):
        self.game.running = self.world.component_for_entity(self.game_info, GameInfo).running
        self.world.process(delta)