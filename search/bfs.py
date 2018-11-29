from collections import OrderedDict
from state import State
from game import *


class BFS:
    def __init__(self, start, s_order):
        self.game = Game(start, s_order)
        self.frontier = OrderedDict()
        self.explored = set()
        self.max_level_reached = 0

    def search(self):

        if self.game.check_result(self.game):
            return ''

        first_state = State(self.game.frame, None, None,
                            self.game.zero_position,
                            self.game.available_moves(self.game.zero_position),
                            0)

        self.frontier[first_state] = first_state

        while self.frontier:
            current_state = iter(self.frontier).__next__()
            current_state = self.frontier.pop(current_state)

            for move in current_state.available_moves:
                other_state = self.game.new_state(current_state, move)

                if other_state in self.frontier or other_state in self.explored:
                    continue

                if self.game.check_result(other_state):
                    self.max_level_reached = other_state.rec
                    return other_state.get_path()

                else:
                    self.frontier[other_state] = other_state

            self.explored.add(current_state)
