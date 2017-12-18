from game.components import Sprite, Transform
from game.loaders import EntityLoader
from game.scripts.script import Script

class StatusPanel(Script):
    def __init__(self, arg):
        self.is_front = arg['is_front']
        self.cur_health = 0
        self.max_health = 0

        self.status_health = None
        self.status_health_spr = None
    
    def start(self):
        if self.is_front:
            self.status_health = EntityLoader.load("battle/ui/status_health_front", self.world)
        else:
            self.status_health = EntityLoader.load("battle/ui/status_health_back", self.world)
        
        self.status_health_spr = self.world.component_for_entity(self.status_health, Sprite)
        self.stats_health_transform = self.world.component_for_entity(self.status_health, Transform)
    
    def update(self, delta):
        hwidth = self.status_health_spr.surface.get_width() * self.stats_health_transform.scale.x * (self.cur_health + 1) / (self.max_health + 1)

        self.status_health_spr.bounds.width = hwidth