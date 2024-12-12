from utils import read_file
from collections import namedtuple

def transform(line):
	return list(line)

values = read_file(12, transform, True)

Position = namedtuple("Position", ["x", "y"])

def create_grid(inputs):
	grid = {}
	for y in range(len(inputs)):
		for x in range(len(inputs[y])):
			grid[Position(x,y)] = inputs[y][x]
	return grid, len(inputs)

grid, grid_length = create_grid(values)


def get_neighbours(position):
	return [Position(position.x + 1, position.y), Position(position.x - 1, position.y), 
	Position(position.x, position.y + 1), Position(position.x, position.y - 1)]


for x in range(grid_length):
	for  y in range(grid_length):
		print(grid[Position(x,y)])
