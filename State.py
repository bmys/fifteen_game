class State:

    def __init__(self, frame, parent, move, zero_pos, available_moves):

        self.frame = frame
        self.parent = parent
        self.move = move
        self.zero_position = zero_pos
        self.available_moves = available_moves

    def __eq__(self, other):
        return hash(self.frame) == hash(other.frame)

    def __repr__(self):
        print(self.frame)

    def __str__(self):
        return str(self.frame)

    def __hash__(self):
        return hash(self.frame)
