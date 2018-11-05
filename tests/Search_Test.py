import unittest
from state import State
from search import BFS
import numpy as np
from collections import OrderedDict

class BFSTest(unittest.TestCase):

    def test_first_state_correct(self):
        state_array = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]])
        bfs = BFS(state_array)
        self.assertEqual(bfs.search(), '')

    def test_search(self):
        state_array = np.array([
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]])
        bfs = BFS(state_array)
        self.assertEqual(bfs.search(), 'D')

    def test_dict(self):
        a = OrderedDict()
        a['foo'] = 5
        a['bar'] = 3
        # print(a.popitem())
        print(a)
        for i in a:
            print(i)

        b = iter(a)
        print(b.__next__())

    def test_search2(self):
        state_array = np.array([
            [6, 2, 3],
            [1, 5, 0],
            [4, 7, 8]])
        bfs = BFS(state_array)
        bfs.search()