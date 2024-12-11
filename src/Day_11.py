from utils import read_file
from collections import defaultdict

def transform(line: str):
    return list(map(int, line.split()))


values = read_file(11, transform, False)

stones = values[0]


def is_even_length(number: int) -> bool:
    return len(str(number)) % 2 == 0


def simulate_blinking_count_only(blinks, simulation_stones):
    # Count initial stones by their type
    stone_counts = defaultdict(int)
    for stone in simulation_stones:
        stone_counts[stone] += 1

    for _ in range(blinks):
        new_counts = defaultdict(int)
        for stone, count in stone_counts.items():
            if stone == 0:
                # Stone 0 always produces 1 stone of value 1
                new_counts[1] += count
            elif is_even_length(stone):
                # Even-length stones split into two
                number_str = str(stone)
                mid_index = len(number_str) // 2
                part1 = int(number_str[:mid_index])
                part2 = int(number_str[mid_index:])
                new_counts[part1] += count
                new_counts[part2] += count
            else:
                # Odd-length stones multiply into one stone
                new_stone = stone * 2024
                new_counts[new_stone] += count

        stone_counts = new_counts

    # Calculate the total number of stones
    total_stones = sum(stone_counts.values())
    return total_stones


print(f'Part 1: {simulate_blinking_count_only(25, stones.copy())}')
# Part 1: 203609

print(f'Part 2: {simulate_blinking_count_only(75, stones.copy())}')
# Part 2: 240954878211138
