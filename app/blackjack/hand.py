class Hand:
    def __init__(self, number=1):
        self.number = number
        self.cards = []
        self.total = 0

    def __repr__(self):
        return f'< Hand | Number: {self.number} >'

    # Getters and Setters

    def set_number(self, number):
        self.number = 1

    def get_number(self):
        return self.number

    def set_cards(self, cards):
        self.cards = cards

    def get_cards(self):
        return self.cards

    def set_total(self):
        if len(self.cards) != 0:
            self.total = sum(card.value for card in self.cards)
        else:
            self.total = 0

    def get_total(self):
        return self.total

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        card_index = self.cards.index(card)
        return self.cards.pop(card_index)