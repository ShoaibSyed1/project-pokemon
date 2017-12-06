ASSETS = "assets/"
TILESETS = "tilesets/"
WORLDS = ASSETS + "worlds/"

CHUNKS = "chunks/"

def get_world(world):
    return WORLDS + world + "/world.json"

def get_mappings(world):
    return WORLDS + world + "/mappings.json"

def get_chunk(world, chunk):
    return WORLDS + world + "/" + CHUNKS + chunk + ".json"

def get_tileset_json(tileset):
    return ASSETS + TILESETS + tileset + ".json"

def get_tileset_img(tileset):
    return ASSETS + TILESETS + tileset + ".png"