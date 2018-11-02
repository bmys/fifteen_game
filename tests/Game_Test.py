import unittest
from state import State
from game import *
import numpy as np


class GameTest(unittest.TestCase):

    def test_zero_position(self):
        state_array = np.array([
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]])

        game = Game(state_array)
        self.assertEqual(game.zero_position, (1, 2))

        state_array = np.array([
            [0, 2, 3],
            [4, 5, 1],
            [7, 8, 6]])

        game = Game(state_array)
        self.assertEqual(game.zero_position, (0, 0))

    def test_frame_size(self):
        state_array = np.array([
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]])

        game = Game(state_array)
        self.assertEqual(game.frame_size, (2, 2))

        state_array = np.array([
            [0, 2, 3, 1],
            [4, 5, 1, 1],
            [7, 8, 6, 1]])

        game = Game(state_array)
        self.assertEqual(game.frame_size, (2, 3))

    def test_goal_matrix(self):
        state = np.array([
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]])
        game = Game(state)
        goal_matrix = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]])
        self.assertTrue(np.array_equal(game.goal_matrix, goal_matrix))






