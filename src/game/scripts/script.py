class Script:
    def __init__(self):
        self.world = None
        self.entity = None
    
    def start(self): pass    
    def update(self, delta): pass
    def fixed_update(self, delta): pass
    def on_event(self, event): pass