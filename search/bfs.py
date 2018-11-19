from collections import OrderedDict
from state import State
from game import *


class BFS:
    def __init__(self, start, s_order):
        self.game = Game(start, s_order)
        self.frontier = OrderedDict()
        self.explored = set()

    def search(self):

        if self.game.check_result(self.game):
            return ''

        first_state = State(self.game.frame, None, None,
                            self.game.zero_position,
                            self.game.available_moves(self.game.zero_position))

        for move in self.game.available_moves(first_state.zero_position):

            new_state = self.game.new_state(first_state, move)
            if self.game.check_result(new_state):
                return new_state.move

            self.frontier[hash(new_state)] = new_state
        del first_state

        while len(self.frontier) != 0:
            current_state = iter(self.frontier).__next__()
            current_state = self.frontier.pop(current_state)

            for move in self.game.available_moves(current_state.zero_position):
                other_state = self.game.new_state(current_state, move)
                if other_state in self.frontier or other_state in self.explored:
                    continue
                if self.game.check_result(other_state):
                    print('Win Wiecej niz 1 iteracje')
                    print('Przetworzone stany: %s' % len(self.explored))
                    print('wszystkie stany: %s' % (len(self.explored) + len(self.frontier)))

                    return other_state.get_path()
                else:
                    self.frontier[hash(other_state)] = other_state
            self.explored.add(current_state)
            current_state = self.game