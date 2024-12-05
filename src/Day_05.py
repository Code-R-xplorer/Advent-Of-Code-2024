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

for r in result[1]:
    updates.append(list(map(int, r.split(','))))


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

def reorder_update(update, rules):
    """Reorder an update to adhere to the rules."""
    # Create a dependency graph
    dependencies = {x: set() for x in update}
    for x, y in rules:
        if x in update and y in update:
            dependencies[y].add(x)

    # Perform a topological sort
    sorted_update = []
    while dependencies:
        # Find items with no dependencies
        no_deps = [item for item, deps in dependencies.items() if not deps]
        if not no_deps:
            raise ValueError("Cycle detected in rules")

        # Add items with no dependencies to the sorted list
        for item in no_deps:
            sorted_update.append(item)
            del dependencies[item]

        # Remove the items from other dependencies
        for deps in dependencies.values():
            deps.difference_update(no_deps)

    return sorted_update


total_reordered_middle = 0

for u in updates:
    if not check_update_order(u, page_rules):
        total_reordered_middle += reorder_update(u, page_rules)[int((len(u) - 1) / 2)]

print(f'Part 2: {total_reordered_middle}')
# Part 2: 5833
