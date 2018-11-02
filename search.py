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
                self.visited[hash(new_state)] = new_state

            print(new_state)

        while len(self.visited) != 0:
            for key, value in self.visited.items():

                #If state already exists in visited or explored just skip it
                if key in self.visited or key in self.explored:
                    continue

                #If this is goal state finish
                if self.game.check_result(value):
                    print('WIN WIN WIN!')
                    return

                #If state has no more moves, move it to explored
                if len(value.available_moves) == 0:
                    self.explored.add(self.visited.pop(key))
                    continue

                for move in value.available_moves:
                    new_state = self.game.new_state(value, move)
                    if self.game.check_result(new_state):
                        print('Bravissimo!')
                        return
                    else:


                print('__________')
                print(key)
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