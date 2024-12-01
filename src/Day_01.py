from utils import read_file

# =================================== File Setup ===================================


def transform_to_two_lists(line: str):
    # Split the line by whitespace and convert each part to an integer
    return tuple(map(int, line.split()))


values = read_file(1, transform_to_two_lists, False)

# Use zip to unpack the tuples into two separate lists
list_1, list_2 = zip(*values)

# Convert back into lists for further use
list_1 = list(list_1)
list_2 = list(list_2)


# =================================== Part 1 Solution ===================================


# Sort both lists into ascending order
sorted_list_1 = sorted(list_1)
sorted_list_2 = sorted(list_2)

# Calculate the total distance by comparing the distance with each pair in the lists
total_distance = 0

for i in range(len(sorted_list_1)):
    total_distance += abs(sorted_list_1[i] - sorted_list_2[i])

print(f'Part 1: {total_distance}')
# Part 1: 1320851


# =================================== Part 2 Solution ===================================


similarity_score = 0

for i in range(len(list_1)):
    number = list_1[i]
    occurrences = list_2.count(number)
    similarity_score += number * occurrences

print(f'Part 2: {similarity_score}')
# Part 2: 26859182
