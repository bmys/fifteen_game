import unittest
from state import State
from search import BFS, DFS, AStar
import numpy as np
from metrics import manhattan, hamming


class mockObj:
    def __init__(self, frame):
        self.frame = frame


class ManhattanTest(unittest.TestCase):

    def test_distance(self):

        state_array = np.array([
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]])

        goal_array = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]])

        state = mockObj(state_array)

        dist = manhattan(state, goal_array)

        self.assertEqual(dist[0], 1)

    def test_distance2(self):

        state_array = np.array([
            [1, 2, 3],
            [4, 0, 5],
            [7, 8, 6]])

        goal_array = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]])

        state = mockObj(state_array)

        dist = manhattan(state, goal_array)

        self.assertEqual(dist[0], 2)
