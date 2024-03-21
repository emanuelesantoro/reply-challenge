from tile import Tile

class GoldenPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class SilverPoint:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

def parse_input(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:  # Specify utf-8-sig to skip the BOM character
        width, height, golden_points, silver_points, number_tile_types = map(int, f.readline().split())
        
        golden_point_coords = [GoldenPoint(*map(int, f.readline().split())) for _ in range(golden_points)]
        silver_point_coords = [SilverPoint(*map(int, f.readline().split())) for _ in range(silver_points)]
        tiles = [Tile(*line.split()) for line in f]

    return width, height, golden_point_coords, silver_point_coords, tiles

# Example usage:
filename = './data/00-trailer.txt'  # Change this to your input file name
width, height, golden_points, silver_points, tiles = parse_input(filename)

print("Width:", width)
print("Height:", height)
print("Golden Points:")
for point in golden_points:
    print(point.x, point.y)
print("Silver Points:")
for point in silver_points:
    print(point.x, point.y)
print("Tiles:")
for tile in tiles:
    print(tile.id, tile.cost, tile.available)
