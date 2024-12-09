from collections import namedtuple, defaultdict

from utils import read_file

values = read_file(8, str, True)

Position = namedtuple("Position", ["x", "y"])

grid_size_y = len(values)
grid_size_x = len(values[0])

antennas = defaultdict(set)

for y in range(grid_size_y):
    for x in range(grid_size_x):
        if not values[y][x] == ".":
            antennas[values[y][x]].add(Position(x, y))

aninodes = set()

print(antennas)

for antenna in antennas:
    antenna_positions = list(antennas[antenna])
    for pos1 in range(len(antenna_positions)):
        for pos2 in range(len(antenna_positions)):
            if antenna_positions[pos1] == antenna_positions[pos2]:
                continue
            diff = abs(antenna_positions[pos1].x - antenna_positions[pos2].x), abs(antenna_positions[pos1].y - antenna_positions[pos2].y)
            antinode_1 = Position(antenna_positions[pos1].x - diff[0], antenna_positions[pos1].y - diff[1])
            antinode_2 = Position(antenna_positions[pos2].x + diff[0], antenna_positions[pos2].y + diff[1])
            if 0 < antinode_1.x >= grid_size_x and 0 < antinode_1.y >= grid_size_y:
                aninodes.add(antinode_1)
            if 0 < antinode_2.x >= grid_size_x and 0 < antinode_2.y >= grid_size_y:
                aninodes.add(antinode_2)

print(len(aninodes))

