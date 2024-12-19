from utils import read_file
from collections import namedtuple, deque

def transform(line):
    return list(line)

values = read_file(12, transform, False)

Position = namedtuple("Position", ["x", "y"])

def create_grid(inputs):
    grid = {}
    visited = {}
    for y in range(len(inputs)):
        for x in range(len(inputs[y])):
            grid[Position(x, y)] = inputs[y][x]
            visited[Position(x, y)] = False
    return grid, visited, len(inputs)

def get_neighbours(position):
    return [
        Position(position.x + 1, position.y),
        Position(position.x - 1, position.y),
        Position(position.x, position.y + 1),
        Position(position.x, position.y - 1)
    ]

def bfs(start_position, grid, visited, grid_length):
    plant_type = grid[start_position]
    queue = deque([start_position])
    visited[start_position] = True
    area = 0
    perimeter = 0

    while queue:
        current = queue.popleft()
        area += 1
        # Check all neighbors
        for neighbor in get_neighbours(current):
            if 0 <= neighbor.x < grid_length and 0 <= neighbor.y < grid_length:
                if grid.get(neighbor) == plant_type and not visited[neighbor]:
                    # Add to queue if same type and not visited
                    visited[neighbor] = True
                    queue.append(neighbor)
                elif grid.get(neighbor) != plant_type:
                    # Neighboring cell is a different type, counts as perimeter
                    perimeter += 1
            else:
                # Out of bounds counts as perimeter
                perimeter += 1

    return area, perimeter

def get_regions(grid, visited, grid_length):
    regions = []
    # Iterate through the grid
    for y in range(grid_length):
        for x in range(grid_length):
            position = Position(x, y)
            if not visited[position]:  # If cell is not visited, start a new region
                area, perimeter = bfs(position, grid, visited, grid_length)
                regions.append((grid[position], area, perimeter))

    return regions

def part_1(values):
	grid, visited, grid_length = create_grid(values)
	regions = get_regions(grid, visited, grid_length)
	total_price = sum(area * perimeter for _, area, perimeter in regions)
	print(f'Part 1: {total_price}')

part_1(values) # Part 1: 1457298