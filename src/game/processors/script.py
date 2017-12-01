from esper import Processor

from game.components import ScriptComponent

class ScriptProcessor(Processor):
    def __init__(self):
        pass
    
    def process(self, delta):
        for ent, script_comp in self.world.get_component(ScriptComponent):
            script_comp.script.update(delta)
