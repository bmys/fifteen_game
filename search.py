from fifteen import Fifteen, State


class BFS:
    def __init__(self, start):
        self.game = Fifteen(start)
        self.visited = {}
        self.explored = set()
        pass

    def search(self):
        # First state
        first_state = State(self.game.frame,
                            None,
                            None,
                            self.game.zero_pos)

        if self.game.check_result(first_state):
            print('You win at first iteration!')
            return

        print(self.game.check_result(first_state))

        for move in self.game.available_moves(first_state):
            new_state = self.game.swap(first_state, move)
            print(new_state)

            # Check if this goal state
            if self.game.check_result(new_state):
                for key, value in self.visited.items():
                    print('%s : \n%s\n' % (key, value))
                return
            else:
                self.visited[new_state.frame.tostring()] = new_state
            # if self.game.check_result(new_state):
            #     break




