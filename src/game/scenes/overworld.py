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
        from game.loaders import EntityLoader
        from game.processors import AnimationProcessor, EventProcessor, RenderProcessor, ScriptProcessor, TileProcessor, WorldProcessor

        self.game_info = self.world.create_entity(GameInfo())
        
        self.camera = EntityLoader.load("camera", self.world)
        player = EntityLoader.load("overworld/player", self.world)
        world_info = EntityLoader.load("overworld/world_info", self.world)
        EntityLoader.load("overworld/random", self.world)
        EntityLoader.load("ui_controller", self.world)

        self.world.add_processor(AnimationProcessor(), 2)
        self.world.add_processor(EventProcessor(self.game_info))
        self.world.add_processor(RenderProcessor(self.game.window, self.camera))
        self.world.add_processor(ScriptProcessor(), 3)
        self.world.add_processor(TileProcessor())
        self.world.add_processor(WorldProcessor(world_info, player, self.scale))

    def update(self, delta):
        self.game.running = self.world.component_for_entity(self.game_info, GameInfo).running
        self.world.process(delta)