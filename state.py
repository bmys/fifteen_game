import numpy as np


class State:

    def __init__(self, frame: object, parent: object, move: object, zero_pos: object, available_moves: object) -> object:
        """
        :param frame:
        :param parent:
        :param move:
        :param zero_pos:
        :param available_moves:
        """
        self.frame = frame
        self.parent = parent
        self.move = move
        self.zero_position = zero_pos
        self.available_moves = available_moves

    def get_path(self, path=''):
        # print(path)
        if self.move is None:
            return path
        else:
            # print(self.move)
            return self.parent.get_path(self.move + path)

    def __eq__(self, other):
        try:
            return np.array_equal(self.frame, other.frame)
        except AttributeError:
            return False

    def __repr__(self):
        return self.frame

    def __str__(self):
        return str(self.frame)

    def __hash__(self):
        return hash(self.frame.tobytes())
