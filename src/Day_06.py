from utils import read_file


def transform(line: str):
    return list(line)


mapped_area = read_file(6, transform, False)

points_visited = [[False] * (len(mapped_area[0])+1) for i in range(len(mapped_area)+1)]

guard_pos = (0, 0)
guard_direction = (0, 0)
# UP, RIGHT, DOWN, LEFT
all_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for y in range(len(mapped_area)):
    for x in range(len(mapped_area[0])):
        if mapped_area[y][x] == '<':
            points_visited[y][x] = True
            guard_pos = (y, x)
            guard_direction = (0, -1)
        if mapped_area[y][x] == '>':
            points_visited[y][x] = True
            guard_pos = (y, x)
            guard_direction = (0, 1)
        if mapped_area[y][x] == '^':
            points_visited[y][x] = True
            guard_pos = (y, x)
            guard_direction = (-1, 0)
        if mapped_area[y][x] == 'v':
            points_visited[y][x] = True
            guard_pos = (y, x)
            guard_direction = (1, 0)

while 0 <= guard_pos[0] < len(mapped_area) and 0 <= guard_pos[1] < len(mapped_area[0]):
    next_pos = (guard_pos[0] + guard_direction[0], guard_pos[1] + guard_direction[1])

    # Check if the next position is within bounds
    if not (0 <= next_pos[0] < len(mapped_area) and 0 <= next_pos[1] < len(mapped_area[0])):
        break  # Exit the loop if the next position is out of bounds

    if mapped_area[next_pos[0]][next_pos[1]] == '#':
        guard_direction = all_directions[(all_directions.index(guard_direction) + 1) % len(all_directions)]
    else:
        guard_pos = next_pos
        points_visited[guard_pos[0]][guard_pos[1]] = True

locations_visited = 0
for row in points_visited:
    locations_visited += sum(row)

print(f'Part 1: {locations_visited}')
# Part 1: 4789
