from fifteen import Fifteen, State


class BFS:
    def __init__(self, start):
        self.game = Fifteen(start)
        self.visited = {}
        self.explored = {}
        pass

    def search(self):
        # Pierwszy stan

        first_state = State(self.game.frame,
                            None,
                            None,
                            self.game.zero_pos
                            )

        if self.game.check_result(first_state):
            print('Latwo poszlo 1 iteracja')
            return

        print(self.game.check_result(first_state))

        for move in self.game.avalible_moves(first_state):
            new_state = self.game.swap(first_state, move)
            print(new_state)

            # Sprawdzanie czy to wymarzony state
            if self.game.check_result(new_state):
                for key, value in self.visited.items():
                    print('%s : \n%s\n' % (key, value))
                return
            else:
                self.visited[new_state.frame.tostring()] = new_state
            # if self.game.check_result(new_state):
            #     print('Brawo kurwa!')
            #     break




