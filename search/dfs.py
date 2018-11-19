from game import *
from state import State


class DFS:
    def __init__(self, start):
        self.game = Game(start)

        self.frontier = list()

        self.visited = set()

    def _expand(self):

        state = self.frontier.pop(0)
        self.visited.add(state)
        expand_list = []

        if state.rec < 20:
            for move in self.game.available_moves(state.zero_position):
                other_state = self.game.new_state(state, move)

                if self.game.check_result(other_state):
                    print('Win Wiecej niz 1 iteracje')
                    return other_state.get_path()

                if other_state in self.visited:
                    continue

                else:
                    other_state.rec = state.rec + 1
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
