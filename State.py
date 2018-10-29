class State:

    def __init__(self, frame, parent, move, zero_pos, avalible_moves):

        self.frame = frame
        self.parent = parent
        self.move = move
        self.zero_position = zero_pos
        self.available_moves = avalible_moves
        pass

    def __eq__(self, other):
        return self.frame == other.frame and \
            self.parent == other.parent and \
            self.move == other.move

    def __repr__(self):
        print(self.frame)

    def __str__(self):
        return str(self.frame)

    def __hash__(self):
        return hash(self.frame)
