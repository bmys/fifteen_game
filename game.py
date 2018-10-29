import numpy as np
from Super_tuple import Tup

class Game:
    def __init__(self, arr):
        self.frame = arr
        self.zero_pos = self.find_zero()
        self.frame_size = self.frame.shape
        self.goal_matrix = np.arange(1, self.frame.size+1).reshape(self.frame_size)
        self.goal_matrix[-1][-1] = 0
        print('shape: %s \n zero_position: %s' % (self.frame_size, self.zero_pos))


    def avalible_moves(self):
        '''Return avalible moves in this moment'''

        moves = ['L', 'R', 'U', 'D']

        if self.zero_pos[1] == 0:
            moves.remove('L')

        if self.zero_pos[1] == self.frame_size[1]-1:
            moves.remove('R')

        if self.zero_pos[0] == 0:
            moves.remove('U')

        if self.zero_pos[0] == self.frame_size[0]-1:
            moves.remove('D')

        return moves

    def can_move(self, direction):
        '''Check if this move can be done'''

        if direction in self.avalible_moves():
            return True
        else:
            return False

    def find_zero(self):
        """
         Find "0" position in matrix
        :return:
        """

        temp = np.where(self.frame == 0)
        temp = tuple(np.concatenate(temp, axis=0))
        return temp

    def swap(self, direction):
        choose = {
            'L': (0, -1),
            'R': (0, 1),
            'U': (-1, 0),
            'D': (1, 0)
        }

        if direction in self.avalible_moves():
            self.change_place(choose[direction])
        else:
            print('nope')

        # print(self.frame[])

    def change_place(self, direction):
        # tuple unpack
        a = Tup(*self.zero_pos)
        b = Tup(*direction)
        new_place =  a + b
        # print('New place: %s' % new_place)
        self.frame[self.zero_pos], self.frame[new_place] =\
            self.frame[new_place], self.frame[self.zero_pos]
        self.zero_pos = new_place

    def print(self):
        print(self.frame)

    def check_result(self):
        if np.array_equal(self.frame, self.goal_matrix):
            print('You win')

arr2 = np.array([[1, 2, 3],
                 [4, 5, 0],
                 [7, 8, 6]])

a = Game(arr2)

while True:
    b = input()
    if b == 'Q':
        break
    elif b == 'P':
        a.print()
    elif b == 'PG':
        print(a.goal_matrix)
    elif b in ['L', 'R', 'U', 'D']:
        a.swap(b)
        a.print()
        a.check_result()
    else:
        print('wrong')
