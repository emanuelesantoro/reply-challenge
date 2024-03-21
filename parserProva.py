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
        self.visited = False

def parse_input(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:  # Specify utf-8-sig to skip the BOM character
        width, height, golden_points, silver_points, number_tile_types = map(int, f.readline().split())
        
        golden_point_coords = [GoldenPoint(*map(int, f.readline().split())) for _ in range(golden_points)]
        silver_point_coords = [SilverPoint(*map(int, f.readline().split())) for _ in range(silver_points)]
        tiles = [Tile(*line.split()) for line in f]

    return width, height, golden_point_coords, silver_point_coords, tiles

def get_cheapest_tile(tiles, f, t):
    if not tiles:
        return None
    filtered_tiles = list(filter(lambda tile: tile.can_move(f, t) and tile.is_available(), tiles))
    if not filtered_tiles:
        return None
    return min(filtered_tiles, key=lambda tile: tile.cost)

# Example usage:
filename = './data/01-comedy.txt'  # Change this to your input file name
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

# Create a matrix with null elements
grid = [[None for _ in range(width)] for _ in range(height)]

# Set the coordinates of golden points in the matrix
for point in golden_points:
    grid[point.y][point.x] = 'G'

# Set the coordinates of silver points in the matrix
for point in silver_points:
    grid[point.y][point.x] = 'S'

def calculate_distance(golden_point1, golden_point2):
    distance = abs(golden_point1.x - golden_point2.x) + abs(golden_point1.y - golden_point2.y)
    return distance

def find_nearest_silver_point(grid, current_point):
    min_distance = float('inf')
    nearest_point = None
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'S':
                distance = calculate_distance(current_point, SilverPoint(col, row, 0))
                if distance < min_distance:
                    min_distance = distance
                    nearest_point = SilverPoint(col, row, 0)

    return nearest_point
def find_nearest_golden_point(grid, current_point):
    min_distance = float('inf')
    nearest_point = None
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'G':
                distance = calculate_distance(current_point, GoldenPoint(col, row))
                if distance < min_distance:
                    min_distance = distance
                    nearest_point = GoldenPoint(col, row)

    return nearest_point


# print(get_cheapest_tile(tiles , "R", "L"))
def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def print_grid_ascii(grid):
    for row in grid:
        print(' '.join(['-' if cell is None else cell for cell in row]))

def write_grid_to_file(grid, filename):
    with open(filename, 'w') as f:
        for row in range(height):
                for col in range(width):
                    cell = grid[row][col]
                    if cell not in[None, 'G', 'S']:
                        f.write(f"{cell} {col} {row}\n")

write_grid_to_file(grid, './data/01-comedy-solution.txt')
