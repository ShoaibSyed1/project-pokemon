class ProcessorList:
    def __init__(self):
        self.procs = {}
    
    def register(self, proc, name):
        self.procs[name] = proc
    
    def get(self, name, arg):
        if arg == None:
            return self.procs[name]()
        return self.procs[name](arg)

processor_list = ProcessorList()

get = processor_list.get

from game.processors.animation import AnimationProcessor
from game.processors.event import EventProcessor
from game.processors.render import RenderProcessor
from game.processors.script import ScriptProcessor

from game.processors.tile import TileProcessor
from game.processors.world import WorldProcessor

processor_list.register(TileProcessor, "tile_processor")
processor_list.register(WorldProcessor, "world_processor")
