from esper import Processor

from game.components import ScriptComponent

class ScriptProcessor(Processor):
    def __init__(self):
        pass
    
    def process(self, delta):
        script_list = list(self.world.get_component(ScriptComponent))
        
        for ent, script_comp in script_list:
            if not script_comp.started:
                script_comp.script.entity = ent
                script_comp.script.world = self.world
                script_comp.script.start()
                script_comp.started = True
            script_comp.script.update(delta)
