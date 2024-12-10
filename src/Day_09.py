from utils import read_file

values = read_file(9, str, False)

values = list(map(int, list(values[0])))

drive = []

id = 0

for i in range(0, len(values), 2):
    for j in range(values[i]):
        drive.append(id)
    if i == len(values) - 1:
        break
    for j in range(values[i + 1]):
        drive.append(None)
    id += 1


def move_right_values_to_left(array):
    new_array = array
    write_index = 0
    read_index = len(array) - 1
    total_writes_needed = sum(x is not None for x in new_array)
    while write_index < total_writes_needed:
        if new_array[write_index] is not None:
            write_index += 1
        else:
            if array[read_index] is not None:
                new_array[write_index] = array[read_index]
                new_array[read_index] = None
                write_index += 1
                read_index -= 1
            else:
                read_index -= 1
    return new_array


def calculate_checksum(array):
    checksum = 0

    for i in range(len(array)):
        if array[i] is None:
            continue
        checksum += array[i] * i

    return checksum


print(f'Part 1: {calculate_checksum(move_right_values_to_left(drive.copy()))}')


# Part 1: 6399153661894

def move_whole_files(disk):
    # Parse the input into a list of tuples (file_id, start_index, size)
    files = []
    i = 0

    while i < len(disk):
        if isinstance(disk[i], int):  # If it is part of a file
            file_id = disk[i]
            start_index = i
            size = 0

            # Count the size of the current file
            while i < len(disk) and disk[i] == file_id:
                size += 1
                i += 1

            files.append((file_id, start_index, size))
        else:
            i += 1

    # Sort files by file ID in descending order
    files.sort(key=lambda x: x[0], reverse=True)

    # Process files and move them if possible
    for file_id, start_index, size in files:
        # Find leftmost span of free space large enough to fit the file
        free_space_start = None
        free_space_size = 0

        for j in range(len(disk)):
            if disk[j] is None:
                if free_space_start is None:
                    free_space_start = j
                free_space_size += 1
            else:
                if free_space_size >= size:
                    break
                free_space_start = None
                free_space_size = 0

        # Check if a suitable span of free space exists
        if free_space_start is not None and free_space_size >= size and free_space_start < start_index:
            # Move the file to the free space
            for k in range(size):
                disk[free_space_start + k] = file_id
                disk[start_index + k] = None

    return disk


print(f'Part 2: {calculate_checksum(move_whole_files(drive.copy()))}')
# Part 2: 6421724645083
