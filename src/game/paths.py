ASSETS = "assets/"
WORLDS = ASSETS + "worlds/"

CHUNKS = "chunks/"

def get_world(world):
    return WORLDS + world + "/world.json"

def get_mappings(world):
    return WORLDS + world + "/mappings.json"

def get_chunk(world, chunk):
    return WORLDS + world + "/" + CHUNKS + chunk + ".json"