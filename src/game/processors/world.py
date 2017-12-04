from esper import Processor

from game.components import WorldInfo

class WorldProcessor(Processor):
    def __init__(self, entity):
        self.world_info = entity
    
    def process(self, delta):
        world_info = self.world.component_for_entity(self.world_info, WorldInfo)

        if world_info.info == None:
            pass
            #TODO: Load world info
        
        #TODO: Load world based on player position
