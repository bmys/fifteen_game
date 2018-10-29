from search import BFS
import numpy as np

arr = np.array([[1, 2, 3],
                 [4, 5, 0],
                 [7, 8, 6]])

a = BFS(arr)
a.search()