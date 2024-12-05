from utils import read_file
from itertools import groupby

values = read_file(5, str, False)

result = []

# Group elements based on whether they are not the split value
for key, group in groupby(values, lambda x: x != ''):

    # If the key is True, the group contains
    # elements not equal to the split value
    if key:
        # Convert the group to a list and add to result
        result.append(list(group))

page_rules = []

for rule in result[0]:
    x = int(rule.split('|')[0])
    y = int(rule.split('|')[1])
    page_rules.append((x, y))

updates = []

for update in result[1]:
    updates.append(list(map(int, update.split(','))))


def check_update_order(update, rules):
    """Check if the update adheres to the rules."""
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False  # Rule violated
    return True


total_correct_middle = 0

for u in updates:
    if check_update_order(u, page_rules):
        total_correct_middle += u[int((len(u) - 1) / 2)]

print(f'Part 1: {total_correct_middle}')
# Part 1: 5329
