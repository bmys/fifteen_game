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
        else:
            first_state = State(self.game.frame, None, None, self.game.zero_position, self.game.available_moves(self.game.zero_position))
            for move in self.game.available_moves(self.game.zero_position):
                new_state = self.game.new_state(first_state, move)
                self.visited[hash(new_state)] = new_state

            while len(self.visited) != 0:
                current_state = self.visited.popitem()[1]
                if self.game.check_result(current_state):
                    print('U win!')
                    return ''
                else:
                    for move in self.game.available_moves(current_state.zero_position):
                        other_state = State(current_state.frame,
                                            current_state, move,
                                            current_state.zero_position,
                                            self.game.available_moves(current_state))
                        if self.game.check_result(other_state):
                            return ''
                        else:
                            self.visited[hash(current_state)] = current_state


            current_state = self.game
