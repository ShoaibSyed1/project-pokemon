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
        from game.components.ui import Element
        from game.data import PlayerData
        from game.processors import AnimationProcessor, EventProcessor, RenderProcessor, ScriptProcessor, TileProcessor, WorldProcessor
        from game.scripts import PlayerScript
        from game.scripts.ui import Textbox, UiController

        self.game_info = self.world.create_entity(GameInfo())

        self.world.create_entity(
            Animation(16, 16, 8, 8, 50, 0, 4),
            Sprite(pygame.image.load("assets/image.png")),
            Tile(Vector2(5, 0)),
            Transform(pos=Vector2(600, 3), scale=Vector2(8, 8), layer=10))

        self.camera = self.world.create_entity(
            Transform(pos=Vector2(0, 0), scale=Vector2(2, 2)))
        
        player_data = PlayerData("lol", "surface", Vector2(5, 5), [], [], [])
        player_script = PlayerScript(self.camera, player_data)

        self.player = self.world.create_entity(
            Animation(16, 20, 16, 20, 200, 0, 4),
            AnimationGroups('still', {
                'still': AnimationGroup(True, 0, 1, -1),
                'walk_down': AnimationGroup(True, 0, 1, 100)
            }),
            EventListener([pygame.KEYDOWN, pygame.KEYUP]),
            Sprite(pygame.image.load("assets/sprites/players/james/overworld.png"), Rect(0, 0, 32, 40)),
            ScriptComponent(player_script),
            Tile(Vector2(0, 0), move_speed=1),
            Transform(pos=Vector2(64, 64), scale=Vector2(2, 2), layer=10))
        
        scr = Textbox(self.player)
        
        self.world.create_entity(
            Element("textbox", Vector2(768, 144), Vector2(128, 400)),
            EventListener([pygame.KEYDOWN, pygame.KEYUP]),
            ScriptComponent(scr),
            Sprite(pygame.image.load("assets/sprites/ui/textbox/textbox.png")),
            Transform(pos=Vector2(128, 576-32), layer=10)
        )
        
        self.world.create_entity(
            EventListener([pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]),
            ScriptComponent(UiController(self.camera))
        )
        
        world_info = self.world.create_entity(
            WorldInfo("surface")
        )

        self.world.add_processor(AnimationProcessor(), 2)
        self.world.add_processor(EventProcessor(self.game_info))
        self.world.add_processor(RenderProcessor(self.game.window, self.camera))
        self.world.add_processor(ScriptProcessor(), 3)
        self.world.add_processor(TileProcessor())
        self.world.add_processor(WorldProcessor(world_info, self.player, self.scale))

    def update(self, delta):
        self.game.running = self.world.component_for_entity(self.game_info, GameInfo).running
        self.world.process(delta)