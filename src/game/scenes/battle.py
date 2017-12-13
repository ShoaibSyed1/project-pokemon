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
        from game.loaders import EntityLoader, UiLoader
        from game.processors import AnimationProcessor, EventProcessor, RenderProcessor, ScriptProcessor

        self.game_info = self.world.create_entity(GameInfo())

        self.camera = EntityLoader.load("camera", self.world)
        EntityLoader.load("ui_controller", self.world)

        loader = UiLoader("battle/battle")
        loader.start(self.world)

        self.world.add_processor(AnimationProcessor(), 2)
        self.world.add_processor(EventProcessor(self.game_info))
        self.world.add_processor(RenderProcessor(self.game.window, self.camera))
        self.world.add_processor(ScriptProcessor(), 3)
    
    def update(self, delta):
        self.game.running = self.world.component_for_entity(self.game_info, GameInfo).running
        self.world.process(delta)