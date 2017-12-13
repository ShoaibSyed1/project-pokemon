import esper

class Scene:
    def __init__(self, game, path):
        self.game = game
        self.path = path

        self.world = esper.World()

        self.game_info = None
    
    def start(self):
        from game.components import GameInfo
        from game.loaders import EntityLoader

        self.game_info = self.world.create_entity(GameInfo())