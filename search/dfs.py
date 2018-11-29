from game import *
from state import State
from collections import OrderedDict


class DFS:
    def __init__(self, start, s_order, max_recursion=20):
        self.game = Game(start, s_order)

        self.frontier = OrderedDict()

        self.explored = dict()

        self.max_recursion = max_recursion
        self.max_level_reached = 0

    def _expand(self):

        state = self.frontier.popitem(0)
        state = state[0]
        expand_list = []
        recursion_level = state.rec + 1

        self.max_level_reached = recursion_level if recursion_level > self.max_level_reached \
            else self.max_level_reached

        if state.rec < self.max_recursion:

            for move in state.available_moves:
                other_state = self.game.new_state(state, move)

                if self.game.check_result(other_state):
                    return other_state.get_path()

                if other_state in self.explored:
                    if self.explored[other_state] < other_state.rec:
                        continue
                    else:
                        self.explored[other_state] = other_state.rec

                if other_state in self.frontier:
                    if self.frontier[other_state].rec < other_state.rec:
                        continue
                    else:
                        self.frontier.pop(other_state)

                expand_list.append(other_state)

            self.explored[state] = state.rec
            expand_list.reverse()

            for st in expand_list:
                self.frontier[st] = st

        return False

    def search(self):

        # Fill firsts states
        if self.game.check_result(self.game):
            return ''

        first_state = State(self.game.frame, None, None,
                            self.game.zero_position,
                            self.game.available_moves(self.game.zero_position),
                            0)

        self.frontier[first_state] = first_state.rec

        while self.frontier:
            found_solution = self._expand()
            if found_solution is False:
                continue
            else:
                return found_solution
