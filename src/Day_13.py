from itertools import groupby
from utils import read_file

values = read_file(13, str, False)


def find_min_cost(prizes):
    results = []

    for prize in prizes:
        a_x, b_x, x_target = prize['x']
        a_y, b_y, y_target = prize['y']
        min_cost = float('inf')
        found_solution = False

        for a in range(101):  # Iterate over possible values for a
            # Solve for b in the first equation
            if (x_target - a * a_x) % b_x == 0:
                b = (x_target - a * a_x) // b_x
                if b < 0 or b > 100:
                    continue  # b must be non-negative and within the limit

                # Check if this b works for the second equation
                if a * a_y + b * b_y == y_target:
                    found_solution = True
                    cost = 3 * a + b
                    min_cost = min(min_cost, cost)

        if found_solution:
            results.append(min_cost)

    return len(results), sum(results)


def get_prizes(inputs, unit_conversion=False):
    results = []

    # Group elements based on whether they are not the split value
    for key, group in groupby(inputs, lambda x: x != ''):

        # If the key is True, the group contains
        # elements not equal to the split value
        if key:
            # Convert the group to a list and add to result
            results.append(list(group))

    prizes = []

    for result in results:
        a_x = int(result[0].split(": ")[1].split(", ")[0].split("+")[1])
        a_y = int(result[0].split(": ")[1].split(", ")[1].split("+")[1])
        b_x = int(result[1].split(": ")[1].split(", ")[0].split("+")[1])
        b_y = int(result[1].split(": ")[1].split(", ")[1].split("+")[1])
        prize_x = int(result[2].split(": ")[1].split(", ")[0].split("=")[1])
        prize_y = int(result[2].split(": ")[1].split(", ")[1].split("=")[1])
        if unit_conversion:
            prize_x += 10000000000000
            prize_y += 10000000000000
        prizes.append({'x': (a_x, b_x, prize_x), 'y': (a_y, b_y, prize_y)})

    return prizes


num_prizes, total_cost = find_min_cost(get_prizes(values))
print(f"Number of prizes won: {num_prizes}")
print(f"Minimum tokens spent: {total_cost}")


# Part 1: 26599

def find_min_cost_2(prizes):
    results = []

    for prize in prizes:
        a_x, b_x, x_target = prize['x']
        a_y, b_y, y_target = prize['y']
        a_presses = (a_x * y_target - a_y * x_target) / (
                a_x * b_y - a_y * b_x
        )
        b_presses = (x_target - a_presses * b_x) / a_x
        if int(a_presses) == a_presses and int(b_presses) == b_presses:
            results.append(int(a_presses) + 3 * int(b_presses))

    return len(results), sum(results)


num_prizes, total_cost = find_min_cost_2(get_prizes(values, True))
print(f"Number of prizes won: {num_prizes}")
print(f"Minimum tokens spent: {total_cost}")
# Part 2: 106228669504887