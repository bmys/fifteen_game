from game import *
from state import State


class DFS:
    def __init__(self, start, s_order):
        self.game = Game(start, s_order)

        self.frontier = list()

        self.explored = dict()
        self.max_level_reached = 0
        self.watch = self.game.frame

    def _expand(self):

        state = self.frontier.pop()
        self.watch = state
        expand_list = []
        recursion_level = state.rec + 1
        # print(state.get_path())
        self.max_level_reached = recursion_level if recursion_level > self.max_level_reached \
            else self.max_level_reached

        # if state.rec > 20:
        #     print('nawrot')

        if state.rec < 8:
            for move in state.available_moves:
                other_state = self.game.new_state(state, move)

                if self.game.check_result(other_state):
                    return other_state.get_path()

                if other_state in self.explored:
                    if self.explored[other_state] <= recursion_level:
                        continue
                    else:
                        self.explored[other_state] = recursion_level
                        # print('zmieniam')

                # a = False
                # for st in self.frontier:
                #     a = True if np.array_equal(st.frame, other_state.frame) else False

                # if a:
                #     continue

                self.explored[state] = state.rec
                expand_list.append(other_state)
            expand_list.reverse()
            self.frontier.extend(expand_list)
        return False

    def search(self):

        # Fill firsts states
        if self.game.check_result(self.game):
            return ''

        first_state = State(self.game.frame, None, None,
                            self.game.zero_position,
                            self.game.available_moves(self.game.zero_position), 0)

        self.frontier.append(first_state)

        while self.frontier:
            found_solution = self._expand()
            if found_solution is False:
                continue
            else:
                return found_solution