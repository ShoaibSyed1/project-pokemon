from game.loaders import EntityLoader
from game.scripts.script import Script

class StatusPanel(Script):
    def __init__(self):
        pass
    
    def start(self):
        EntityLoader.load("battle/ui/status_health_back", self.world)
        EntityLoader.load("battle/ui/status_health_front", self.world)