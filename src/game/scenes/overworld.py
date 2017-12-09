import esper
import pygame

from game.scenes.scene import Scene

from game.components import GameInfo

class Overworld(Scene):
    def __init__(self, game):
        self.game = game

        self.world = esper.World()
        
        self.camera = None
        self.game_info = None        
        self.player = None

        self.scale = 2

    
    def start(self):
        from pygame import Rect

        from pygame.math import Vector2

        from game.components import Animation, AnimationGroup, AnimationGroups, EventListener, InputComponent, Sprite, Transform, ScriptComponent, Tile, WorldInfo
        from game.data import PlayerData
        from game.processors import AnimationProcessor, EventProcessor, RenderProcessor, ScriptProcessor, TileProcessor, WorldProcessor
        from game.scripts import PlayerScript

        self.game_info = self.world.create_entity(GameInfo())

        self.world.create_entity(
            Animation(16, 16, 8, 8, 50, 0, 4),
            Sprite(pygame.image.load("assets/image.png")),
            Tile(Vector2(33, 0)),
            Transform(pos=Vector2(600, 3), scale=Vector2(8, 8)))

        self.camera = self.world.create_entity(
            Transform(pos=Vector2(0, 0), scale=Vector2(2, 2)))
        
        player_data = PlayerData("lol", "surface", Vector2(5, 5), [], [], [])
        player_script = PlayerScript(self.camera, player_data)

        self.player = self.world.create_entity(
            Animation(48, 32, 16, 32, 200, 1, 3),
            AnimationGroups('still', {
                'still': AnimationGroup(True, 0, 1, -1),
                'walk_down': AnimationGroup(True, 1, 3, 100)
            }),
            #InputComponent([pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]),
            EventListener([pygame.KEYDOWN, pygame.KEYUP]),
            Sprite(pygame.image.load("assets/player/player.png"), Rect(0, 0, 32, 64), layer=10),
            ScriptComponent(player_script),
            Tile(Vector2(0, 0), move_speed=1),
            Transform(pos=Vector2(64, 64), scale=Vector2(2, 2)))
        
        world_info = self.world.create_entity(
            WorldInfo("surface")
        )

        self.world.add_processor(AnimationProcessor(), 2)
        self.world.add_processor(EventProcessor(self.game_info))
        self.world.add_processor(RenderProcessor(self.game.window, self.camera))
        self.world.add_processor(ScriptProcessor())
        self.world.add_processor(TileProcessor())
        self.world.add_processor(WorldProcessor(world_info, self.player, self.scale))

        for ent, script_comp in self.world.get_component(ScriptComponent):
            script_comp.script.entity = ent
            script_comp.script.world = self.world
            script_comp.script.start()

    def update(self, delta):
        self.game.running = self.world.component_for_entity(self.game_info, GameInfo).running
        self.world.process(delta)