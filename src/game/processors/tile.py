from esper import Processor

from pygame.math import Vector2

from game.components import Direction, Tile, Transform

class TileProcessor(Processor):
    def __init__(self, tile_size=32):
        self.collision_map = {}
        self.tile_size = tile_size
    
    def process(self, delta):
        for ent, (tile, transform) in self.world.get_components(Tile, Transform):
            tile_pos = (tile.pos.x, tile.pos.y)
            if self.collision_map.get(tile_pos, None) == None:
                self.collision_map[tile_pos] = tile.solid
            if not tile.is_moving:
                transform.pos = Vector2(tile.pos.x * self.tile_size, tile.pos.y * self.tile_size)
            if len(tile.move_path) > 0:
                tile.move_dir = tile.move_path[-1]
                pos = tile.pos

                tile.is_moving = True

                if tile.move_dir == Direction.DOWN:
                    transform.pos.y += tile.move_speed
                    if transform.pos.y >= (tile.pos.y + 1) * self.tile_size:
                        transform.pos.y = (tile.pos.y + 1) * self.tile_size
                        tile.pos.y += 1
                        tile.move_path.pop()
                        tile.is_moving = False
                elif tile.move_dir == Direction.UP:
                    transform.pos.y -= tile.move_speed
                    if transform.pos.y <= (tile.pos.y - 1) * self.tile_size:
                        transform.pos.y = (tile.pos.y - 1) * self.tile_size
                        tile.pos.y -= 1
                        tile.move_path.pop()
                        tile.is_moving = False
                elif tile.move_dir == Direction.RIGHT:
                    transform.pos.x += tile.move_speed
                    if transform.pos.x >= (tile.pos.x + 1) * self.tile_size:
                        transform.pos.x = (tile.pos.x + 1) * self.tile_size
                        tile.pos.x += 1
                        tile.move_path.pop()
                        tile.is_moving = False
                elif tile.move_dir == Direction.LEFT:
                    transform.pos.x -= tile.move_speed
                    if transform.pos.x <= (tile.pos.x - 1) * self.tile_size:
                        transform.pos.x = (tile.pos.x - 1) * self.tile_size
                        tile.pos.x -= 1
                        tile.move_path.pop()
                        tile.is_moving = False