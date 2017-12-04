ASSETS = "assets/"
TILESETS = ASSETS + "tilesets/"
WORLDS = ASSETS + "worlds/"

def get_world(name):
    return WORLDS + name + "/"

def get_chunk(world, chunk):
    return get_world(world) + "chunks/" + chunk + ".json"

def get_mapping(world, mapping):
    return get_world(world) + "/chunks/mappings/" + mapping + ".json"