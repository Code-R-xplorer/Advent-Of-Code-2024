from utils import read_file
import re

values = read_file(3, str, True)

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
