#!/usr/bin/python3
from sys import argv
import numpy as np

from search.bfs import BFS
from search.dfs import DFS
from search.astar import AStar

search_order = {'DLRU': ['D', 'L', 'R', 'U'],
 'DLUR': ['D', 'L', 'U', 'R'],
 'DRLU': ['D', 'R', 'L', 'U'],
 'DRUL': ['D', 'R', 'U', 'L'],
 'DULR': ['D', 'U', 'L', 'R'],
 'DURL': ['D', 'U', 'R', 'L'],
 'LDRU': ['L', 'D', 'R', 'U'],
 'LDUR': ['L', 'D', 'U', 'R'],
 'LRDU': ['L', 'R', 'D', 'U'],
 'LRUD': ['L', 'R', 'U', 'D'],
 'LUDR': ['L', 'U', 'D', 'R'],
 'LURD': ['L', 'U', 'R', 'D'],
 'RDLU': ['R', 'D', 'L', 'U'],
 'RDUL': ['R', 'D', 'U', 'L'],
 'RLDU': ['R', 'L', 'D', 'U'],
 'RLUD': ['R', 'L', 'U', 'D'],
 'RUDL': ['R', 'U', 'D', 'L'],
 'RULD': ['R', 'U', 'L', 'D'],
 'UDLR': ['U', 'D', 'L', 'R'],
 'UDRL': ['U', 'D', 'R', 'L'],
 'ULDR': ['U', 'L', 'D', 'R'],
 'ULRD': ['U', 'L', 'R', 'D'],
 'URDL': ['U', 'R', 'D', 'L'],
 'URLD': ['U', 'R', 'L', 'D']}


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

    search_type = {'bfs': BFS, 'dfs': DFS, 'astar': AStar}

    puzzle = load_puzzle( file_names[0])
    # print(f'specs: {spec}')

    if method != 'astar':
        specific = search_order[spec.upper()]
    else:
        specific = spec.upper()

    search = search_type[method](puzzle, specific)

    # print(file_names)
    solution = search.search()
    print(solution)
    solution = '' if solution is None else solution
    save_to_file(file_names[1], solution)



