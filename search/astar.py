from game import *
from state import State
from metrics import hamming, manhattan
import heapq


class AStar:
    def __init__(self, start, metric=None):
        assert metric in ('H', 'M')
        self.metric = hamming if metric == 'H' else manhattan
        self.game = Game(start, ['L', 'U', 'R', 'D'])

        self.frontier = []

        self.explored = set()

        self.max_level_reached = 0

    def _expand(self):

        state = heapq.heappop(self.frontier)
        state = state[1]
        self.explored.add(state)

        for move in state.available_moves:
            other_state = self.game.new_state(state, move)

            recursion_level = other_state.rec + 1
            self.max_level_reached = recursion_level if recursion_level > self.max_level_reached \
                else self.max_level_reached

            if other_state in self.explored:
                continue

            if self.game.check_result(other_state):
                return other_state.get_path()

            else:
                val = self.metric(other_state, self.game.goal_matrix)
                heapq.heappush(self.frontier, val)

        return False

    def search(self):

        # Fill firsts states
        if self.game.check_result(self.game):
            return ''

        first_state = State(self.game.frame, None, None,
                            self.game.zero_position,
                            self.game.available_moves(self.game.zero_position),
                            0)

        heapq.heappush(self.frontier, self.metric(first_state, self.game.goal_matrix))

        while True:
            found_solution = self._expand()
            if found_solution is False:
                continue
            else:
                return found_solution


