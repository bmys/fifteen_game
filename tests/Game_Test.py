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

    def test_available_moves(self):
        state = np.array([
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]])
        game = Game(state)

        self.assertEqual(game.available_moves((2, 2)), ['L', 'U'])
        self.assertEqual(game.available_moves((0, 0)), ['R', 'D'])
        self.assertEqual(game.available_moves((1, 1)), ['L', 'R', 'U', 'D'])
        self.assertEqual(game.available_moves((0, 1)), ['L', 'R', 'D'])
        self.assertEqual(game.available_moves((2, 1)), ['L', 'R', 'U'])
        self.assertEqual(game.available_moves((1, 2)), ['L', 'U', 'D'])

    def test_check_result(self):

        arr1 = np.array([
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]])

        arr2 = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]])

        game = Game(arr1)

        state1 = State(arr2, None, None, (2,2), None)
        state2 = State(arr1, None, None, (2,2), None)

        self.assertTrue(game.check_result(state1))
        self.assertFalse(game.check_result(state2))
