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
    result = array
    write_index = 0
    read_index = len(array) - 1
    total_writes_needed = sum(x is not None for x in result)
    while write_index < total_writes_needed:
        if result[write_index] is not None:
            write_index += 1
        else:
            if array[read_index] is not None:
                result[write_index] = array[read_index]
                result[read_index] = None
                write_index += 1
                read_index -= 1
            else:
                read_index -= 1
    return result


result = move_right_values_to_left(drive)

checksum = 0

for i in range(len(result)):
    if result[i] is None:
        continue
    checksum += result[i] * i

print(checksum)