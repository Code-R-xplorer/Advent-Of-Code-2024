from datetime import datetime
import os
from git import Repo

current = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(current)
source = os.path.join(root_dir, 'src')
inputs = os.path.join(root_dir, 'Inputs')

day_number = "%02d" % datetime.now().day
script_file = os.path.join(source, f"Day_{day_number}.py")
input_file = os.path.join(inputs, f"day_{day_number}.txt")
test_input_file = os.path.join(inputs, f"day_{day_number}_test.txt")

if os.path.isfile(script_file):
    print(f'Day {datetime.now().day} has already been setup')
    exit()

with open(os.path.join(source, f"Day_{day_number}.py"), 'w') as f:
    f.write("from utils import read_file\n\n"
            f"values = read_file({datetime.now().day}, str, True)\n\n")
    f.close()

with open(os.path.join(inputs, f"day_{day_number}.txt"), 'w') as f:
    f.close()

with open(os.path.join(inputs, f"day_{day_number}_test.txt"), 'w') as f:
    f.close()

repo = Repo(root_dir)
origin = repo.remote(name='origin')
day_branch = repo.create_head(f"day_{day_number}")
day_branch.checkout()

repo.index.add([script_file, input_file, test_input_file])
repo.index.commit(f"Day {datetime.now().day} Setup")
