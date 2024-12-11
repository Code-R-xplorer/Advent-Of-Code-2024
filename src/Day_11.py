from utils import read_file


def transform(line: str):
    return list(map(int, line.split()))


values = read_file(11, transform, False)

stones = values[0]


def is_even_length(number: int) -> bool:
    return len(str(number)) % 2 == 0


def change_stone(stone):
    if stone == 0:
        return [1]
    elif is_even_length(stone):
        number_str = str(stone)
        mid_index = len(number_str) // 2
        part1 = int(number_str[:mid_index])
        part2 = int(number_str[mid_index:])
        return [part1, part2]
    else:
        return [stone * 2024]


def simulate_blinking(blinks, simulation_stones):
    for _ in range(blinks):
        temp_stones = []
        for current_stone in simulation_stones:
            new_stones = change_stone(current_stone)
            for new_stone in new_stones:
                temp_stones.append(new_stone)
        simulation_stones = temp_stones
    return simulation_stones


print(f'Part 1: {len(simulate_blinking(25, stones.copy()))}')
