from game import *
from state import State


class DFS_r:
    def __init__(self, start, s_order):
        self.game = Game(start, s_order)

        self.frontier = set()

        self.explored = set()
        self.max_level_reached = 0

    def _expand(self, st):
        if st.rec > self.max_level_reached:
            self.max_level_reached = st.rec

        if self.game.check_result(st):
            return st.get_path()

        if st in self.frontier or st in self.explored or st.rec > 20:
            return False

        self.frontier.add(st)

        for move in st.available_moves:

            new_state = self.game.new_state(st, move)

            val = self._expand(new_state)

            if val is False:
                continue

            else:
                return val

        self.frontier.remove(st)
        self.explored.add(st)


        return False

    def search(self):

        # Fill firsts states
        if self.game.check_result(self.game):
            return ''

        first_state = State(self.game.frame, None, None,
                            self.game.zero_position,
                            self.game.available_moves(self.game.zero_position),
                            0)

        return self._expand(first_state)
