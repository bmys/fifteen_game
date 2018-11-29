from game import *
from state import State
from collections import OrderedDict


class DFS:
    def __init__(self, start, s_order, max_recursion=20):
        self.game = Game(start, s_order)

        self.frontier = OrderedDict()

        self.visited = dict()

        self.max_recursion = max_recursion

    def _expand(self):

        state = self.frontier.popitem(0)
        state = state[0]
        expand_list = []
        recursion_level = state.rec + 1

        if state.rec < self.max_recursion:

            for move in state.available_moves:
                other_state = self.game.new_state(state, move)
                other_state.rec = recursion_level

                if self.game.check_result(other_state):
                    return other_state.get_path()

                if other_state in self.visited:
                    if self.visited[other_state] < recursion_level:
                        continue
                    else:
                        self.visited[other_state] = recursion_level

                if other_state in self.frontier:
                    if self.frontier[other_state].rec < recursion_level:
                        continue
                    else:
                        self.frontier.pop(other_state)

                expand_list.append(other_state)

            self.visited[state] = state.rec
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
                            self.game.available_moves(self.game.zero_position))
        first_state.rec = 0

        self.frontier[first_state] = first_state.rec

        while self.frontier:
            found_solution = self._expand()
            if found_solution is False:
                continue
            else:
                return found_solution
