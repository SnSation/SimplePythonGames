from .player import Player

class Dealer(Player):
    def __init__(self, name="Dealer"):
        self.set_funds(1000000)

    def __repr__(self):
        return f'< Dealer | Name: {self.name} >'

        
    # def shuffle_cards(self):
    #     new_cards = []
    #     for card in self.cards:
    #         card_index = random.randint(0, (len(self.cards)-1))
    #         new_cards.append(self.cards.pop(card_index))
    #     self.cards = new_cards