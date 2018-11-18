from sys import argv
import numpy as np


def load_puzzle(file_name):
    with open(file_name, 'r') as file:
        text = file.read().splitlines()
    text = text[1:]

    for idx, line in enumerate(text):
        text[idx] = tuple(int(i) for i in line.split(' '))
    return np.array(text)

print(load_puzzle('puzzles/4x4_01_00001.txt'))

method, spec, *file_name = argv[1], argv[2], argv[3:]
print(f'method: {method}')
print(f'spec: {spec}')
print('file_names:')
for i in file_name:
    print(i)