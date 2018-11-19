from collections import OrderedDict
from state import State
from game import *

class BFS:
    def __init__(self, start):
        self.game = Game(start)
        # Slownik -- hash mapa, zapamietujekolejnosc dodawania
        self.frontier = OrderedDict()
        # zbior by nie sprawdzac czy juz w nim. bo w zbiorze jeden element moze byc tylko raz
        self.explored = set()

    def search(self):
        # Check if first state is goal state
        # Ta czesc tylko sprawdza pierwszy stan i rozwijaja go w inne stany

        # SPRAWDZENIE
        if self.game.check_result(self.game):
            return ''

        # ROZWIJNIE
        first_state = State(self.game.frame, None, None,
                            self.game.zero_position,
                            self.game.available_moves(self.game.zero_position))
        # DLA MOZLIWEGO RUCHU TWORZYMY NOWY STAN
        for move in self.game.available_moves(first_state.zero_position):

            new_state = self.game.new_state(first_state, move)
            if self.game.check_result(new_state):
                return new_state.move
            # Dodajemy to otwartych stanow
            self.frontier[hash(new_state)] = new_state
        del first_state
        #  ____________________________________________________________________
        while len(self.frontier) != 0:
            # Pobieramy klucz pierwszego elementu
            current_state = iter(self.frontier).__next__()
            # Zdejmujemy ten obiekt
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