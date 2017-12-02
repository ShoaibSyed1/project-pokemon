from esper import Processor

from game.components import Tile, Transform

class TileProcessor(Processor):
    def __init__(self):
        pass
    
    def process(self, delta):
        for ent, (tile, transform) in self.world.get_components(Tile, Transform):
            pass