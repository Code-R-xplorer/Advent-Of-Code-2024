from utils import read_file


def transform(line):
    return list(map(int, list(line)))


values = read_file(10, transform, False)


def find_unique_peak_paths(grid):
    def is_valid_move(x, y, current_height):
        # Check if the move is within the grid and increases by exactly 1 in height
        return (0 <= x < len(grid) and 0 <= y < len(grid[0])
                and grid[x][y] == current_height + 1)

    def dfs(x, y, path, reached_peaks):
        current_height = grid[x][y]
        # If the current height is 9, a valid path is found
        if current_height == 9:
            peak = (x, y)
            # Add the path only if the peak hasn't been reached by this trailhead
            if peak not in reached_peaks:
                reached_peaks.add(peak)
                paths.append(path[:])
            return

        # Explore all four directions: up, down, left, right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, current_height):
                dfs(nx, ny, path + [(nx, ny)], reached_peaks)

    paths = []
    # Iterate through the grid to find all trailheads (0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:  # Start a DFS from each trailhead
                reached_peaks = set()
                dfs(i, j, [(i, j)], reached_peaks)

    return paths


unique_peak_paths = find_unique_peak_paths(values)
print(f'Part 1: {len(unique_peak_paths)}')


def find_all_paths(grid):
    def is_valid_move(x, y, current_height):
        # Check if the move is within the grid and increases by exactly 1 in height
        return (0 <= x < len(grid) and 0 <= y < len(grid[0])
                and grid[x][y] == current_height + 1)

    def dfs(x, y, path):
        current_height = grid[x][y]
        # If the current height is 9, a valid path is found
        if current_height == 9:
            paths.append(path[:])
            return

        # Explore all four directions: up, down, left, right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, current_height):
                dfs(nx, ny, path + [(nx, ny)])

    paths = []
    # Iterate through the grid to find all trailheads (0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:  # Start a DFS from each trailhead
                dfs(i, j, [(i, j)])

    return paths


all_paths = find_all_paths(values)
print(f'Part 2: {len(all_paths)}')
