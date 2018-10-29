import numpy as np
import operator


class Game:
    def __init__(self, arr):
        self.frame = arr
        self.zero_pos = find_zero(self)
        self.frame_size = self.frame.shape
        self.goal_matrix = np.arange(1, self.frame.size+1).reshape(self.frame_size)
        self.goal_matrix[-1][-1] = 0
        # print('shape: %s \n zero_position: %s' % (self.frame_size, self.zero_pos))

    def available_moves(self, state):
        """Return avaliable moves in this moment"""

        moves = ['L', 'R', 'U', 'D']

        if state.zero_position[1] == 0:
            moves.remove('L')

        if state.zero_position[1] == self.frame_size[1]-1:
            moves.remove('R')

        if state.zero_position[0] == 0:
            moves.remove('U')

        if state.zero_position[0] == self.frame_size[0]-1:
            moves.remove('D')

        return moves


    def check_result(self, state):
        if np.array_equal(state.frame, self.goal_matrix):
            print('You win')
            return True
        return False

    def __repr__(self):
        return self.frame


def find_zero(state):
    """
     Find "0" position in matrix
    :return: tuple of zero coordinates
    """

    temp = np.where(state.frame == 0)
    temp = tuple(np.concatenate(temp, axis=0))
    return temp


def change_place(state, direction):
    choose = {
        'L': (0, -1),
        'R': (0, 1),
        'U': (-1, 0),
        'D': (1, 0)
    }

    # tuple unpack
    # a = Tup(*state.zero_pos)
    # b = Tup(*choose[direction])

    new_place = tuple(map(operator.add, state.zero_pos, choose[direction]))

    state.frame[state.zero_position], state.frame[new_place] = \
        state.frame[new_place], state.frame[state.zero_position]
    state.zero_pos = new_place