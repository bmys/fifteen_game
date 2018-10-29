import numpy as np


class State:

    def __init__(self, frame, parent, move, zero_pos, avalible_moves):

        self.frame = frame
        self.parent = parent
        self.move = move
        self.zero_position = zero_pos
        self.avalible_moves = avalible_moves
        pass

    def __eq__(self, other):
        return self.frame == other.frame and \
            self.parent == other.parent and \
            self.move == other.move

    def __repr__(self):
        print( self.frame)

    def __str__(self):
        return str(self.frame)


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

    def avalible_moves(self, state):

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
    #     Usuanac ruch rodzica


    # def avalible_moves_first_state(self, state):
    #     moves = ['L', 'R', 'U', 'D']
    #
    #     if self.zero_pos[1] == 0:
    #         moves.remove('L')
    #
    #     if self.zero_pos[1] == self.frame_size[1]-1:
    #         moves.remove('R')
    #
    #     if self.zero_pos[0] == 0:
    #         moves.remove('U')
    #
    #     if self.zero_pos[0] == self.frame_size[0]-1:
    #         moves.remove('D')
    #
    #     return moves
    # #     Usuanac ruch rodzica

    def swap(self, state, direction):

        # a = Tup(*self.zero_pos)
        # b = Tup(*direction)

        new_place = tuple(map(lambda x, y: x + y, state.zero_position, self.choose[direction]))
        new_frame = state.frame.copy()

        # print('New place: %s' % new_place)
        new_frame[state.zero_position], new_frame[new_place] = \
            new_frame[new_place], new_frame[state.zero_position]

        return State(new_frame, state, direction, new_place, self.avalible_moves(new_frame))

        # print(self.frame[])

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













# import numpy as np
# from Super_tuple import Tup
#
#
# class Fifteen:
#     def __init__(self, arr):
#         self.frame = arr
#         self.zero_pos = self.find_zero()
#         self.frame_size = self.frame.shape
#
#         self.goal_matrix = np.arange(1, self.frame.size+1).reshape(self.frame_size)
#         self.goal_matrix[-1][-1] = 0
#
#
#     def avalible_moves(self):
#
#         moves = ['L', 'R', 'U', 'D']
#
#         if self.zero_pos[1] == 0:
#             moves.remove('L')
#
#         if self.zero_pos[1] == self.frame_size[1]-1:
#             moves.remove('R')
#
#         if self.zero_pos[0] == 0:
#             moves.remove('U')
#
#         if self.zero_pos[0] == self.frame_size[0]-1:
#             moves.remove('D')
#
#         return moves
#
#     def find_zero(self):
#         temp = np.where(self.frame == 0)
#         temp = tuple(np.concatenate(temp, axis=0))
#         # print(temp)
#         return temp
#
#     def swap(self, direction):
#         choose = {
#             'L': (0, -1),
#             'R': (0, 1),
#             'U': (-1, 0),
#             'D': (1, 0)
#         }
#
#         if direction in self.avalible_moves():
#             self.change_place(choose[direction])
#         else:
#             print('nihuhu')
#
#         # print(self.frame[])
#
#     def change_place(self, direction):
#         # tuple unpack
#         a = Tup(*self.zero_pos)
#         b = Tup(*direction)
#         new_place =  a + b
#         # print('New place: %s' % new_place)
#         self.frame[self.zero_pos], self.frame[new_place] =\
#             self.frame[new_place], self.frame[self.zero_pos]
#         self.zero_pos = new_place
#
#     def print(self):
#         print(self.frame)
#
#     def check_result(self):
#         if np.array_equal(self.frame, self.goal_matrix):
#             print('Wygrałes talon, na kurwe i balon')
#
