from utils import read_file


def transform(line: str):
    return list(line)


mapped_area = read_file(6, transform, False)

points_visited = [[False] * (len(mapped_area[0]) + 1) for i in range(len(mapped_area) + 1)]

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

current_pos = guard_pos
current_direction = guard_direction

while 0 <= current_pos[0] < len(mapped_area) and 0 <= current_pos[1] < len(mapped_area[0]):
    next_pos = (current_pos[0] + current_direction[0], current_pos[1] + current_direction[1])

    # Check if the next position is within bounds
    if not (0 <= next_pos[0] < len(mapped_area) and 0 <= next_pos[1] < len(mapped_area[0])):
        break  # Exit the loop if the next position is out of bounds

    if mapped_area[next_pos[0]][next_pos[1]] == '#':
        current_direction = all_directions[(all_directions.index(current_direction) + 1) % len(all_directions)]
    else:
        current_pos = next_pos
        points_visited[current_pos[0]][current_pos[1]] = True

locations_visited = 0
for row in points_visited:
    locations_visited += sum(row)

print(f'Part 1: {locations_visited}')
# Part 1: 4789


def simulate_guard(mapped_area, position, direction):
    visited_states = set()  # Track visited positions and directions
    n_current_pos = position
    n_current_direction = direction

    while True:
        state = (n_current_pos, n_current_direction)
        if state in visited_states:
            # Loop detected
            return True
        visited_states.add(state)

        # Calculate the next position
        n_next_pos = (n_current_pos[0] + n_current_direction[0], n_current_pos[1] + n_current_direction[1])

        # Check if the next position is within bounds
        if not (0 <= n_next_pos[0] < len(mapped_area) and 0 <= n_next_pos[1] < len(mapped_area[0])):
            # Guard exits the map
            return False

        if mapped_area[n_next_pos[0]][n_next_pos[1]] == '#':
            # Turn right
            n_current_direction = all_directions[(all_directions.index(n_current_direction) + 1) % len(all_directions)]
        else:
            # Move forward
            n_current_pos = n_next_pos


# Find all valid obstacle placements
valid_obstacle_positions = []

for y in range(len(mapped_area)):
    for x in range(len(mapped_area[0])):
        if mapped_area[y][x] == '.' and points_visited[y][x]:
            # Place an obstacle
            mapped_area[y][x] = '#'

            # Simulate the guard's movement
            if simulate_guard(mapped_area, guard_pos, guard_direction):
                valid_obstacle_positions.append((y, x))

            # Remove the obstacle
            mapped_area[y][x] = '.'

print("Part 2: ", len(valid_obstacle_positions))
# Part 2: 1304
