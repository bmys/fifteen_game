from game import *
from state import State


class DFSr:
    def __init__(self, start, s_order,  rec_level=20):
        self.game = Game(start, s_order)

        self.frontier = set()

        self.explored = dict()
        self.max_level_reached = 0
        self.rec_level = rec_level

    def _expand(self, st):
        if st.rec > self.max_level_reached:
            self.max_level_reached = st.rec

        if self.game.check_result(st):
            return st.get_path()

        if st in self.frontier or st.rec > self.rec_level:
            return False

        if st in self.explored:
            if st.rec < self.explored[st]:
                self.explored[st] = st.rec
            else:
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
        self.explored[st] = st.rec

        return False

    def search(self):

        # Fill firsts states
        if self.game.check_result(self.game):
            return ''

        first_state = State(self.game.frame, None, None,
                            self.game.zero_position,
                            self.game.available_moves(self.game.zero_position),
                            0)
        a = self._expand(first_state)
        if a is False:
            return ''
        else:
            return a
