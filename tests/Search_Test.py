import unittest
from state import State
from search import BFS
import numpy as np


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
        bfs.search()

    def test_search2(self):
        state_array = np.array([
            [1, 2, 3],
            [4, 0, 5],
            [7, 8, 6]])
        bfs = BFS(state_array)
        bfs.search()