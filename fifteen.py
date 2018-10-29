import numpy as np
from State import State

class Fifteen:

    def __init__(self, arr):

        self.frame = arr
        self.zero_pos = tuple(np.concatenate(np.where(self.frame == 0), axis=0))
        self.frame_size = self.frame.shape

        self.goal_matrix = np.arange(1, self.frame.size+1).reshape(self.frame_size)
        self.goal_matrix[-1][-1] = 0

        self.choose ={
            'L': (0, -1),
            'R': (0, 1),
            'U': (-1, 0),
            'D': (1, 0)}

    def available_moves(self, state):

        moves = ['L', 'R', 'U', 'D']

        zero_pos = state.zero_position

        if zero_pos[1] == 0:
            moves.remove('L')

        if zero_pos[1] == self.frame_size[1]-1:
            moves.remove('R')

        if zero_pos[0] == 0:
            moves.remove('U')

        if zero_pos[0] == self.frame_size[0]-1:
            moves.remove('D')

        return moves

    def swap(self, state, direction):

        new_place = tuple(map(lambda x, y: x + y, state.zero_position, self.choose[direction]))
        new_frame = state.frame.copy()

        new_frame[state.zero_position], new_frame[new_place] = \
            new_frame[new_place], new_frame[state.zero_position]

        return State(new_frame, state, direction, new_place, self.available_moves(new_frame))

    def check_result(self, state):
        if np.array_equal(state.frame, self.goal_matrix):
            print('you win')
            return True

        return False

    def check_first(self, state):
        if np.array_equal(self.frame, self.goal_matrix):
            print('you win')
            return True

        return False


