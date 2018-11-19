#!/usr/bin/python3
from sys import argv
import numpy as np

from search.bfs import BFS
from search.dfs import DFS


def load_puzzle(file_name):
    with open(file_name, 'r') as file:
        text = file.read().splitlines()
    text = text[1:]

    for idx, line in enumerate(text):
        text[idx] = tuple(int(i) for i in line.split(' '))
    return np.array(text)


def save_to_file(name, solution):
    with open(name, 'w') as file:
        file.write(solution)


if len(argv) > 1:
    #load console args
    method, spec, file_names = argv[1], argv[2], argv[3:]

    # print(f'method: {method}')
    # print(f'spec: {spec}')
    # print('file_names:')

    search_type = {'bfs': BFS, 'dfs': DFS}

    puzzle = load_puzzle( file_names[0])

    search = search_type[method](puzzle)

    # print(file_names)
    solution = search.search()
    print(solution)
    save_to_file(file_names[1], solution)



