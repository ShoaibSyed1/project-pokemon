from pymunk.vec2d import Vec2d

from game.components.transform import Transform
from game.scripts.script import Script

class PlayerScript(Script):    
    def start(self):
        self.transform = self.world.component_for_entity(self.entity, Transform)
    
    def update(self, delta):
        pass
    
    def fixed_update(self, delta):
        pass
    
    def on_event(self, event):
        pass