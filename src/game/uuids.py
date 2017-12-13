import uuid

uuids = {}

def get(name):
    if uuids.get(name, None) == None:
        uuids[name] = uuid.uuid4()
    
    return uuids[name]