from .player import Player

class Dealer(Player):
    def __init__(self):
        self.set_name("Dealer")
        self.set_bankroll(1000000)

    def __repr__(self):
        return f'< Dealer | Name: {self.name} >'

    