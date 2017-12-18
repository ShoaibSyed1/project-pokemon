import esper

from game.components import GameInfo

class Scene:
    def __init__(self, game, path):
        self.game = game
        self.path = path

        self.world = esper.World()

        self.scripts = []

        self.camera = None
        self.game_info = None
    
    def start(self):
        from game.loaders import EntityLoader, SceneLoader
        from game.processors import AnimationProcessor, ElementProcessor, EventProcessor, RenderProcessor, ScriptProcessor

        self.game_info = self.world.create_entity(GameInfo())

        self.camera = EntityLoader.load("camera", self.world)
        EntityLoader.load("ui_controller", self.world)

        preloader = EntityLoader.load("preloader", self.world)
        self.world.delete_entity(preloader)

        self.world.add_processor(AnimationProcessor(), 5)
        self.world.add_processor(ElementProcessor(), 3)
        self.world.add_processor(EventProcessor(self.game_info))
        self.world.add_processor(RenderProcessor(self.game.window, self.camera))
        self.world.add_processor(ScriptProcessor(), 4)

        SceneLoader.load(self.path, self.world)
    
    def update(self, delta):
        self.game.running = self.world.component_for_entity(self.game_info, GameInfo).running
        self.world.process(delta)