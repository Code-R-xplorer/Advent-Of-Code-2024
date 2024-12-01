import os

root_dir = os.path.dirname(os.path.abspath(__file__))
inputs = os.path.join(root_dir, 'Inputs')


def read_file(day: int, transform=str, use_test=False, strip_line=True) -> list:
    try:
        if use_test:
            with open(os.path.join(inputs, f'day_{"%02d" % day}_test.txt')) as f:
                if strip_line:
                    return [transform(line.strip()) for line in f]
                else:
                    return [transform(line.strip('\n')) for line in f]
        else:
            with open(os.path.join(inputs, f'day_{"%02d" % day}.txt')) as f:
                if strip_line:
                    return [transform(line.strip()) for line in f]
                else:
                    return [transform(line.strip('\n')) for line in f]
    except FileNotFoundError as e:
        print(e)
