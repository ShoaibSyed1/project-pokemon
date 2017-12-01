from esper import Processor
from pymunk import Space

from game.components import PhysicsBody, Transform

class PhysicsProcessor(Processor):
    def __init__(self, step_time=0.01):
        self.space = Space()

        self.step_time = step_time
        self.accum = 0.0
    
    def get_space(self):
        return self.space
    
    def process(self, delta):
        self.accum += delta

        while self.accum >= self.step_time:
            self.phys_process()
            self.accum -= self.step_time
    
    def phys_process(self):
        self.space.step(self.step_time)

        for ent, (phys_body, transform) in self.world.get_components(PhysicsBody, Transform):
            transform.pos = phys_body.body.position