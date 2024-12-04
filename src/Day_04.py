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
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def find_x_shape(grid, x, y):
    if grid[x][y] != "A":
        return False

    # Define the positions of the corners relative to the center (x, y)
    corners = {
        'tl': (x - 1, y - 1),  # Top-left
        'tr': (x + 1, y - 1),  # Top-right
        'bl': (x - 1, y + 1),  # Bottom-left
        'br': (x + 1, y + 1)   # Bottom-right
    }

    # Check if all corner positions are within bounds
    for pos in corners.values():
        if not check_in_bounds(grid, pos[0], pos[1]):
            return False

    # Patterns to match
    patterns = [
        ('M', 'S', 'M', 'S'),
        ('S', 'M', 'S', 'M'),
        ('M', 'M', 'S', 'S'),
        ('S', 'S', 'M', 'M')
    ]

    tl, tr, bl, br = corners['tl'], corners['tr'], corners['bl'], corners['br']
    for pattern in patterns:
        if (grid[tl[0]][tl[1]], grid[tr[0]][tr[1]], grid[bl[0]][bl[1]], grid[br[0]][br[1]]) == pattern:
            return True

    return False


count = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if find_x_shape(grid, x, y):
            count += 1

print(f'Part 2: {count}')
# Part 2: 2000
