import esper

from game.scenes.scene import Scene

from game.components.game_info import GameInfo

class Overworld(Scene):
    def __init__(self, game):
        self.game = game

        self.world = esper.World()
        
        self.game_info = None
    
    def start(self):
        from game.processors.event import EventProcessor
        from game.processors.render import RenderProcessor

        self.game_info = self.world.create_entity(GameInfo())

        self.world.add_processor(EventProcessor(self.game_info))
        self.world.add_processor(RenderProcessor(self.game.window))

    def update(self, delta):
        self.game.running = self.world.component_for_entity(self.game_info, GameInfo).running
        self.world.process()