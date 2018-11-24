from game import *
from state import State


class DFS:
    def __init__(self, start, s_order):
        self.game = Game(start, s_order)

        self.frontier = list()

        self.visited = dict()

    def _expand(self):

        state = self.frontier.pop(0)
        self.visited[state] = state.rec
        expand_list = []
        recursion_level = state.rec + 1

        if state.rec < 20:
            for move in state.available_moves:
                other_state = self.game.new_state(state, move)

                if self.game.check_result(other_state):
                    return other_state.get_path()

                if other_state in self.visited:
                    if self.visited[other_state] > recursion_level:
                        print('pomijam')
                        continue
                    else:
                        self.visited[other_state] = recursion_level
                        print('zmieniam')

                # a = False
                # for st in self.frontier:
                #     a = True if np.array_equal(st.frame, other_state.frame) else False

                # if a:
                #     continue

                else:
                    other_state.rec = recursion_level
                    expand_list.append(other_state)

            self.frontier = expand_list + self.frontier
        return False

    def search(self):

        # Fill firsts states
        if self.game.check_result(self.game):
            return ''

        first_state = State(self.game.frame, None, None,
                            self.game.zero_position,
                            self.game.available_moves(self.game.zero_position))
        first_state.rec = 0
        self.frontier.append(first_state)

        while self.frontier:
            found_solution = self._expand()
            if found_solution is False:
                continue
            else:
                return found_solution
