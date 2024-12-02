from utils import read_file


def transform(line):
    return [int(c) for c in line.split()]


values = read_file(2, transform, False)

safe_reports = 0

for report in values:
    increasing = report[0] > report[1]
    safe_reports += 1

    for i in range(len(report) - 1):
        if report[i] == report[i + 1]:
            safe_reports -= 1
            break
        difference = abs(report[i] - report[i + 1])
        if difference > 3:
            safe_reports -= 1
            break
        if increasing:
            if report[i] < report[i + 1]:
                safe_reports -= 1
                break
        else:
            if report[i] > report[i + 1]:
                safe_reports -= 1
                break

print(safe_reports)
# Part 1: 639
