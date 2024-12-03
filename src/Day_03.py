from utils import read_file
import re

values = read_file(3, str, False)


def get_matches(pattern):
    hits = []
    for line in values:
        hits += re.findall(pattern, line)
    return hits


def get_total_results(hits):
    # Pattern to extract X and Y
    extract_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Extract X and Y for each match
    results = [re.match(extract_pattern, hit).groups() for hit in hits]

    # Convert the tuples to integers (optional)
    results = [(int(x), int(y)) for x, y in results]

    total_results = 0

    for x, y in results:
        total_results += (x * y)
    return total_results


matches = get_matches(r"mul\(\d{1,3},\d{1,3}\)")

print(f'Part 1: {get_total_results(matches)}')
# Part 1: 173419328

matches = get_matches(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)")

instructions = []
do_instruction = True

for i in range(len(matches)):
    if matches[i] == "don't()":
        do_instruction = False
        continue
    if matches[i] == "do()":
        do_instruction = True
        continue
    if do_instruction:
        instructions.append(matches[i])

print(f'Part 2: {get_total_results(instructions)}')
# Part 2: 90669332
