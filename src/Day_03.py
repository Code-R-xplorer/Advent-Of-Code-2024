from utils import read_file
import re

values = read_file(3, str, False)

# Regular expression to match valid mul(X,Y)
pattern = r"mul\(\d{1,3},\d{1,3}\)"

matches = []

for line in values:
    matches += re.findall(pattern, line)

# Pattern to extract X and Y
extract_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Extract X and Y for each match
results = [re.match(extract_pattern, match).groups() for match in matches]

# Convert the tuples to integers (optional)
results = [(int(x), int(y)) for x, y in results]

total_results = 0

for x, y in results:
    total_results += (x * y)

print(f'Part 1: {total_results}')
# Part 1: 173419328

pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"

matches = []

for line in values:
    matches += re.findall(pattern, line)

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

# Extract X and Y for each match
results = [re.match(extract_pattern, match).groups() for match in instructions]

# Convert the tuples to integers (optional)
results = [(int(x), int(y)) for x, y in results]

total_results = 0

for x, y in results:
    total_results += (x * y)

print(f'Part 2: {total_results}')