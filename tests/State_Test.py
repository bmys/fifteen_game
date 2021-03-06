import unittest
from state import State
import numpy as np


class StateTest(unittest.TestCase):

    def test_zero_position(self):
        state_array = np.array([
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]])

        state = State(state_array, None, None, (1, 2), ['U', 'L', 'D'])
        self.assertEqual(state.zero_position, (1, 2))

    def test_hash(self):

        state_array = np.array([
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]])

        state = State(state_array, None, None, (1, 2), ['U', 'L', 'D'])
        state2 = State(state_array, None, None, (1, 2), ['R', 'L', 'D'])
        self.assertEqual(hash(state), hash(state2))

    def test_comparison(self):
        state_array = np.array([
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]])

        state = State(state_array, None, None, (1, 2), ['U', 'L', 'D'])
        state2 = State(state_array, None, None, (1, 2), ['R', 'L', 'D'])
        self.assertEqual(state, state2)

        state_array2 = np.array([
            [1, 2, 3],
            [7, 5, 0],
            [4, 8, 6]])

        state3 = State(state_array2, None, None, (1, 2), ['R', 'L', 'D'])
        self.assertNotEqual(state, state3)

