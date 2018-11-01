from search import BFS
import numpy as np
from state import *

if __name__ == '__main__':
    print('Witaj')
    arr = np.array([[1, 2, 3],
                     [4, 5, 0],
                     [7, 8, 6]],
                   dtype=np.uint8)
    state = State(arr, None, None, None, None)
    print(hash(state))
    A = BFS(arr)
    A.search()
    # a = BFS(arr)
    # a.search()
