from .player import Player

class Dealer(Player):
    def __init__(self, name="Dealer"):
        self.set_funds(1000000)

    def __repr__(self):
        return f'< Dealer | Name: {self.name} >'