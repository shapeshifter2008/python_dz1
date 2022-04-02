import sys
from itertools import islice

param_start = None
param_end = None

if len(sys.argv) == 3:
    param_start = int(sys.argv[1])
    param_end = int(sys.argv[2])
elif len(sys.argv) == 2:
    param_start = int(sys.argv[1])

with open('bakery.csv', 'r', encoding='utf-8') as file_read:
    if param_end is not None:
        lines = islice(file_read, param_start-1, param_end)
    elif param_start is not None and param_start >= 1:
        lines = islice(file_read, param_start-1, len(file_read.readline()))
    else:
        lines = file_read.readlines()

    for line in lines:
        print(line.strip())
