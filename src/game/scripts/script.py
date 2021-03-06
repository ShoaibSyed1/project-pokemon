from game.components.uuid import Uuid

class Script:
    def __init__(self):
        self.world = None
        self.entity = None
    
    def start(self): pass    
    def update(self, delta): pass

    #From EventListener
    def on_event(self, event): pass

    #From InputComponent
    def on_ui_event(self, event): pass

    #From TileObject
    def on_interact(self, player): pass

    def get_entity(self, uuid):
        ents = list(filter(lambda x: x[1].uuid == uuid, self.world.get_component(Uuid)))
        if len(ents) == 1:
            return ents[0][0]
        elif len(ents) > 1:
            raise ConflictingUUIDError()
        return None

class ConflictingUUIDError(Exception):
    pass