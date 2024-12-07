from utils import read_file


def transform(line: str):
    a, b = line.split(': ')
    return [int(a), list(map(int, b.split(' ')))]


values = read_file(7, transform, False)


def check_operations(input_list):
    true_expressions = []

    for test_value, numbers in input_list:
        n = len(numbers)

        # Recursive function to evaluate expressions
        def evaluate_expression(index, current_value):
            if index == n:
                return current_value == test_value

            # Try adding the next number
            if evaluate_expression(index + 1, current_value + numbers[index]):
                return True

            # Try multiplying the next number
            if evaluate_expression(index + 1, current_value * numbers[index]):
                return True

            return False

        # Check if the expression can evaluate to the test value
        if evaluate_expression(1, numbers[0]):  # Start with the first number
            true_expressions.append(test_value)

    return true_expressions


print(f"Part 1: {sum(check_operations(values))}")
# Part 1: 5702958180383
