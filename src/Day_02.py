from utils import read_file


def transform(line):
    return [int(c) for c in line.split()]


values = read_file(2, transform, False)


def is_safe(report):
    """Check if the report is safe without any modifications."""
    increasing = report[0] < report[1]  # Determine initial trend (true for increasing)
    for i in range(len(report) - 1):
        # Check if two adjacent values are equal
        if report[i] == report[i + 1]:
            return False
        # Check if the absolute difference exceeds 3
        if abs(report[i] - report[i + 1]) > 3:
            return False
        # Check for consistent trend (increasing or decreasing)
        if increasing and report[i] >= report[i + 1]:  # Should strictly increase
            return False
        if not increasing and report[i] <= report[i + 1]:  # Should strictly decrease
            return False
    return True


def can_be_safe_with_one_removal(report):
    """Check if removing one level makes the report safe."""
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]  # Remove the level at index i
        if is_safe(new_report):
            return True
    return False


def count_safe_reports(values):
    """Count how many reports are safe, either directly or with one removal."""
    safe_reports = 0
    for report in values:
        if is_safe(report) or can_be_safe_with_one_removal(report):
            safe_reports += 1
    return safe_reports


print(f'Part 1: {sum(1 for report in values if is_safe(report))}')
print(f'Part 2: {count_safe_reports(values)}')
