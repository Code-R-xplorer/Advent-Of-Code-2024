from utils import read_file


def transform_to_two_lists(line: str):
    # Split the line by whitespace and convert each part to an integer
    return tuple(map(int, line.split()))


values = read_file(1, transform_to_two_lists, False)

# Use zip to unpack the tuples into two separate lists
list1, list2 = zip(*values)

# Convert back into lists for further use
list1 = list(list1)
list2 = list(list2)

# Sort both lists into ascending order
sorted_list_1 = sorted(list1)
sorted_list_2 = sorted(list2)


# Calculate the total distance by comparing the distance with each pair in the lists
total_distance = 0

for i in range(len(sorted_list_1)):
    total_distance += abs(sorted_list_1[i] - sorted_list_2[i])

print(total_distance)
# Part 1: 1320851
