import numpy as np
import operator
from state import State
from copy import copy


class Game:
    def __init__(self, arr, s_order):
        self.frame = arr
        self.zero_position = find_zero(self)
        self.frame_size = tuple(map(operator.sub, self.frame.shape, (1, 1)))
        # Create goal matrix
        self.goal_matrix = np.arange(1, self.frame.size+1).reshape(arr.shape)
        self.goal_matrix[-1][-1] = 0

        self.goal_hash = hash(bytes(self.goal_matrix))


        self.choose = {
            'L': (0, -1),
            'R': (0, 1),
            'U': (-1, 0),
            'D': (1, 0)
        }

        self.pop_list = {
            'L': 'R',
            'R': 'L',
            'U': 'D',
            'D': 'U',
            None: None
        }

        self.s_order = s_order

    def available_moves(self, zero_position):
        """
        Return available moves in this state
        :param zero_position
        :return:List of available moves
        """

        moves = copy(self.s_order)

        if zero_position[1] == 0:
            moves.remove('L')

        if zero_position[1] == self.frame_size[1]:
            moves.remove('R')

        if zero_position[0] == 0:
            moves.remove('U')

        if zero_position[0] == self.frame_size[0]:
            moves.remove('D')

        return moves

    def check_result(self, state: State) -> bool:
        """Check if state array and goal array are equal
        :param state
        :return:Bool
        """

        if np.array_equal(state.frame, self.goal_matrix):

            return True
        return False

    def new_state(self, state, direction):
        """
       Create new element by swapping frame elements
        :param state:
        :param direction:
        :return: new state
        """

        new_place = tuple(map(operator.add, state.zero_position, self.choose[direction]))
        new_frame = np.copy(state.frame)

        # swap elements
        new_frame[state.zero_position], new_frame[new_place] = \
            new_frame[new_place], new_frame[state.zero_position]
        # state.available_moves.pop(direction)
        new_moves = self.available_moves(new_place)

        try:
            new_moves.remove(self.pop_list[direction])
        except ValueError:
            pass

        return State(new_frame, state, direction, new_place, new_moves, state.rec+1)

    def __repr__(self):
        return str(self.frame)


def find_zero(state):
    """
     Find "0" position in matrix
    :param state
    :return: tuple of zero coordinates
    """

    temp = np.where(state.frame == 0)
    temp = tuple(np.concatenate(temp, axis=0))
    return temp
