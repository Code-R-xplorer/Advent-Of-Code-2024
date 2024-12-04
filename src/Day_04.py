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
