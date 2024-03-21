moves = {"3": ["LR"],
         "5": ["DR"],
         "6": ["LD"],
         "7": ["LR", "LD", "DR"],
         "9": ["UR"],
         "96": ["LD", "UR"],
         "A": ["LU"],
         "B": ["LR", "LU", "UR"],
         "C": ["UD"],
         "C3": ["LR", "UD"],
         "D": ["UD", "UR", "DR"],
         "E": ["LU", "LD", "UD"],
         "F": ["LR", "LD", "LU", "UD", "DR", "UR"]}

class Tile:
    def __init__(self, id, cost, available):
        self.id = id
        self.cost = int(cost)
        self.available = int(available)

    def __str__(self):
        return f"Tyle - Id: {self.id} Cost: {self.cost}, Available: {self.available}"

    def use(self):
        if self.disponibili > 0:
            self.disponibili -= 1
        else:
            raise Exception("Not available")
    def can_move(self, f, t):
        return (f+t in moves[self.id] or t+f in moves[self.id])
    def is_available(self):
        return self.available > 0

class GoldenPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
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

def find_nearest_silver_point(current_point):
    min_distance = float('inf')
    nearest_point = None
    filtered_silver_points = list(filter(lambda point: not point.visited, silver_points))
    for s in filtered_silver_points:
        distance = calculate_distance(current_point, s)
        if distance < min_distance:
            min_distance = distance
            nearest_point = s

    return nearest_point
def find_nearest_golden_point(current_point):
    min_distance = float('inf')
    nearest_point = None
    filtered_golden_points = list(filter(lambda point: not point.visited, golden_points))
    for g in filtered_golden_points:
        distance = calculate_distance(current_point, g)
        if distance < min_distance:
            min_distance = distance
            nearest_point = g

    return nearest_point

def find_nearest_point(current_point):
    min_distance = float('inf')
    nearest_point = None
    filtered_silver_points = list(filter(lambda point: not point.visited, silver_points + golden_points))
    for s in filtered_silver_points:
        distance = calculate_distance(current_point, s)
        if distance < min_distance:
            min_distance = distance
            nearest_point = s
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

def end():
    for g in golden_points:
        if not g.visited:
            return False
    return True


print_grid_ascii(grid)
print("\n-----------------\n")
s = find_nearest_silver_point(golden_points[1])
current_point = golden_points[1]
#current_point.visited = True
while not end():
    if s.y > current_point.y:
        for y in range(current_point.y, s.y + 1):
            cell = grid[y][s.x]
            if cell is not "G":
                grid[y][s.x] = 'F'
    else:
        for y in range(s.y, current_point.y + 1):
            cell = grid[y][s.x]
            if cell is not "G":
                grid[y][s.x] = 'F'  
    if s.x > current_point.x:
        for x in range(current_point.x, s.x + 1):
            cell = grid[current_point.y][x]
            if cell is not "G":
                grid[current_point.y][x] = 'F'
    else:
        for x in range(s.x, current_point.x + 1):
            cell = grid[current_point.y][x]
            if cell is not "G":
                grid[current_point.y][x] = 'F'
    current_point = s
    s.visited = True 
    s = find_nearest_point(current_point)


write_grid_to_file(grid, './data/01-comedy-solution.txt')

print_grid_ascii(grid)

