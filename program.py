from sys import argv
import numpy as np

from search import BFS, DFS


def load_puzzle(file_name):
    with open(file_name, 'r') as file:
        text = file.read().splitlines()
    text = text[1:]

    for idx, line in enumerate(text):
        text[idx] = tuple(int(i) for i in line.split(' '))
    return np.array(text)

if len(argv) > 1:
    #load console args
    method, spec, file_names = argv[1], argv[2], argv[3:]

    # print(f'method: {method}')
    # print(f'spec: {spec}')
    # print('file_names:')

    search_type = {'bfs': BFS, 'dfs': DFS}

    puzzle = load_puzzle('puzzles/' + file_names[0])

    search = search_type[method](puzzle)

    print(search.search())

