from game import *
from state import State
from collections import OrderedDict


class BFS:
    def __init__(self, start):
        self.game = Game(start)
        self.visited = OrderedDict()
        self.explored = set()

    def search(self):
        # Check if first state is goal state

        if self.game.check_result(self.game):
            return ''

        # Expand first state
        for move in self.game.available_moves(self.game.zero_position):
            new_state = self.game.new_state(self.game, move)
            if self.game.check_result(new_state):
                print('you just win at second iteration')
                return new_state.move
            else:
                self.visited[new_state] = new_state
            print(new_state)

        for value in self.visited:
            print(value)
        #
        #     # Check if this goal state
        #     if self.game.check_result(new_state):
        #         for key, value in self.visited.items():
        #             print('%s : \n%s\n' % (key, value))
        #         return
        #     else:
        #         self.visited[new_state.frame.tostring()] = new_state
        #     # if self.game.check_result(new_state):
        #     #     break
        pass