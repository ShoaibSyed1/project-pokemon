from esper import Processor

from pygame.math import Vector2

from game.components import Direction, Tile, TileObject, Transform

class TileProcessor(Processor):
    def __init__(self, tile_size=32):
        self.tile_size = tile_size
    
    def process(self, delta):
        for ent, (tile, transform) in self.world.get_components(Tile, Transform):
            if not tile.is_moving:
                transform.pos = Vector2(tile.pos.x * self.tile_size, tile.pos.y * self.tile_size)
            if len(tile.move_path) > 0:
                tile.move_dir = tile.move_path[-1]
                pos = tile.pos

                tile.is_moving = True

                to_list = filter(lambda x: x[1][1].is_solid, self.world.get_components(Tile, TileObject))

                if tile.move_dir == Direction.DOWN:
                    if len(list(filter(lambda x: x[1][0].pos == Vector2(tile.pos.x, tile.pos.y + 1), to_list))) > 0:
                        tile.move_path.pop()
                        tile.is_moving = False
                    else:
                        transform.pos.y += tile.move_speed
                        if transform.pos.y >= (tile.pos.y + 1) * self.tile_size:
                            transform.pos.y = (tile.pos.y + 1) * self.tile_size
                            tile.pos.y += 1
                            tile.move_path.pop()
                            tile.is_moving = False
                elif tile.move_dir == Direction.UP:
                    if len(list(filter(lambda x: x[1][0].pos == Vector2(tile.pos.x, tile.pos.y - 1), to_list))) > 0:
                        tile.move_path.pop()
                        tile.is_moving = False
                    else:
                        transform.pos.y -= tile.move_speed
                        if transform.pos.y <= (tile.pos.y - 1) * self.tile_size:
                            transform.pos.y = (tile.pos.y - 1) * self.tile_size
                            tile.pos.y -= 1
                            tile.move_path.pop()
                            tile.is_moving = False
                elif tile.move_dir == Direction.RIGHT:
                    if len(list(filter(lambda x: x[1][0].pos == Vector2(tile.pos.x + 1, tile.pos.y), to_list))) > 0:
                        tile.move_path.pop()
                        tile.is_moving = False
                    else:
                        transform.pos.x += tile.move_speed
                        if transform.pos.x >= (tile.pos.x + 1) * self.tile_size:
                            transform.pos.x = (tile.pos.x + 1) * self.tile_size
                            tile.pos.x += 1
                            tile.move_path.pop()
                            tile.is_moving = False
                elif tile.move_dir == Direction.LEFT:
                    if len(list(filter(lambda x: x[1][0].pos == Vector2(tile.pos.x - 1, tile.pos.y), to_list))) > 0:
                        tile.move_path.pop()
                        tile.is_moving = False
                    else:
                        transform.pos.x -= tile.move_speed
                        if transform.pos.x <= (tile.pos.x - 1) * self.tile_size:
                            transform.pos.x = (tile.pos.x - 1) * self.tile_size
                            tile.pos.x -= 1
                            tile.move_path.pop()
                            tile.is_moving = False