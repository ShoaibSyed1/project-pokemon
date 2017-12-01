from pymunk.vec2d import Vec2d

from game.components import PhysicsBody
from game.components.transform import Transform
from game.scripts.script import Script

class PlayerScript(Script):    
    def start(self):
        self.physics_body = self.world.component_for_entity(self.entity, PhysicsBody)
        self.transform = self.world.component_for_entity(self.entity, Transform)
    
    def update(self, delta):
        pass
    
    def fixed_update(self, delta):
        #self.physics_body.body.apply_impulse_at_local_point(Vec2d(10, 0))
        #print(self.physics_body.body.position)
        pass
    
    def on_event(self, event):
        pass