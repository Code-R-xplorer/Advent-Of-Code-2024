from utils import read_file


def transform(line: str):
    return list(line)


grid = read_file(4, transform, False)


def find_word(grid, word, x, y, dx, dy):
    for i in range(len(word)):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] != word[i]:
            return False
        x += dx
        y += dy
    return True


word = "XMAS"
directions = [
    (0, 1),  # horizontal right
    (1, 0),  # vertical down
    (1, 1),  # diagonal down-right
    (-1, 1),  # diagonal up-right
    (0, -1),  # horizontal left
    (-1, 0),  # vertical up
    (-1, -1),  # diagonal up-left
    (1, -1),  # diagonal down-left
]

count = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        for dx, dy in directions:
            if find_word(grid, word, x, y, dx, dy):
                count += 1

print(f'Part 1: {count}')
# Part 1: 2646


def check_in_bounds(grid, x, y):
    grid_width = len(grid)
    grid_height = len(grid[0])
    return 0 <= x < grid_width and 0 <= y < grid_height


def find_x_shape(grid, x, y):
    if grid[x][y] != "A":
        return False
    tl = (x - 1, y - 1)  # Top-left
    tr = (x + 1, y - 1)  # Top-right
    bl = (x - 1, y + 1)  # Bottom-left
    br = (x + 1, y + 1)  # Bottom-right

    if (not check_in_bounds(grid, tl[0], tl[1]) or
            not check_in_bounds(grid, tr[0], tr[1]) or
            not check_in_bounds(grid, bl[0], bl[1]) or
            not check_in_bounds(grid, br[0], br[1])):
        return False

    return ((grid[tl[0]][tl[1]] == "M" and grid[tr[0]][tr[1]] == "S" and
            grid[bl[0]][bl[1]] == "M" and grid[br[0]][br[1]] == "S")
            or (grid[tl[0]][tl[1]] == "S" and grid[tr[0]][tr[1]] == "M" and
            grid[bl[0]][bl[1]] == "S" and grid[br[0]][br[1]] == "M")
            or (grid[tl[0]][tl[1]] == "M" and grid[tr[0]][tr[1]] == "M" and
            grid[bl[0]][bl[1]] == "S" and grid[br[0]][br[1]] == "S")
            or (grid[tl[0]][tl[1]] == "S" and grid[tr[0]][tr[1]] == "S" and
            grid[bl[0]][bl[1]] == "M" and grid[br[0]][br[1]] == "M"))


count = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if find_x_shape(grid, x, y):
            count += 1

print(f'Part 2: {count}')
# Part 2: 2000
