from utils import read_file

values = read_file(9, str, True)


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


# print(f'Part 1: {calculate_checksum(move_right_values_to_left(drive))}')
# Part 1: 6399153661894

new_array = drive.copy()
current_id = 9
start_write_index = 0
read_index = len(new_array) - 1

while current_id != 0:
    if new_array[start_write_index] is not None:
        start_write_index += 1
    else:
        file_length = 0
        for i in range(read_index, 0, -1):
            if new_array[i] is current_id:
                file_length += 1
            else:
                break
        can_fit_file = True
        for i in range(start_write_index, start_write_index + file_length, 1):
            if new_array[i] is not None:
                can_fit_file = False
                current_id -= 1
                break

        if can_fit_file:
            for i in range(read_index, read_index - file_length, -1):
                new_array[start_write_index] = new_array[i]
                new_array[i] = None
                start_write_index += 1
                read_index -= 1
            start_write_index = 0
            current_id -= 1

print(drive)
print(new_array)