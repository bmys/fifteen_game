from game import *
from state import State
from metrics import hamming, manhattan
import queue


class AStar:
    def __init__(self, start, metric=None):
        self.metric = hamming if metric == 'h' else manhattan
        self.game = Game(start)

        self.frontier = queue.PriorityQueue()

        self.visited = set()

    def _expand(self):

        state = self.frontier.get()
        state = state[1]
        self.visited.add(state)

        for move in self.game.available_moves(state.zero_position):
            other_state = self.game.new_state(state, move)

            if other_state in self.visited:
                continue

            if self.game.check_result(other_state):
                print('Win Wiecej niz 1 iteracje')
                return other_state.get_path()

            else:
                val = self.metric(other_state, self.game.goal_matrix)
                self.frontier.put(val)

        return False

    def search(self):

        # Fill firsts states
        if self.game.check_result(self.game):
            return ''

        first_state = State(self.game.frame, None, None,
                            self.game.zero_position,
                            self.game.available_moves(self.game.zero_position))

        self.frontier.put(self.metric(first_state, self.game.goal_matrix))

        while True:
            found_solution = self._expand()
            if found_solution is False:
                continue
            else:
                return found_solution


