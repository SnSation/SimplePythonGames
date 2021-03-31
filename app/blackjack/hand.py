from .card import Card
class Hand:
    def __init__(self):
        # Name should be an Integer for the Hand Object
        self.name = None
        self.cards = []
        self.value = 0

        # Bet is the current bankroll a Player has bet on the Hand
        self.bet = 0

        # Split, Natural, and Bust are Flags that affect Bets / Payouts
        self.split = False
        self.natural = False
        self.bust = False

    def __repr__(self):
        return f'< Hand | Name: {self.name} >'

    # Getters and Setters
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_cards(self, card_list):
        self.cards = card_list

    def get_cards(self):
        return self.cards

    def set_value(self):
        current_cards = self.get_cards()
        new_value = 0
        if len(current_cards) > 0:
            new_value = sum([card.get_value() for card in current_cards])

        self.value = new_value

    def get_value(self):
        return self.value

    def set_bet(self, amount):
        self.bet = amount
    
    def get_bet(self):
        return self.bet

    def set_split(self, boolean_value):
        self.split = boolean_value

    def get_split(self):
        return self.split

    def set_natural(self):
        self.set_value()
        current_value = self.get_value()
        current_cards = self.get_cards()
        if (current_value == 21) and (len(current_cards) == 2):
            self.natural = True
        else:
            self.natural = False

    def get_natural(self):
        return self.natural

    def set_bust(self):
        self.set_value()
        current_value = self.get_value()
        if current_value > 21:
            self.bust = True
        else:
            self.bust = False

    def get_bust(self):
        return self.bust

    # Hand Action Methods
    def set_card(self, card_index, card_obj):
        current_cards = self.get_cards()
        current_cards[card_index] = card_obj
        self.set_cards(current_cards)
        self.set_value()

    def get_card(self, card_index):
        current_cards = self.get_cards()
        current_card = current_cards[card_index]
        return current_card

    def add_card(self, card_obj):
        current_cards = self.get_cards()
        current_cards.append(card_obj)
        self.set_cards(current_cards)
        self.set_value()

    def remove_card(self, card_obj):
        selected_card = card_obj
        current_cards = self.get_cards()
        current_cards.remove(selected_card)
        self.set_cards(current_cards)
        self.set_value()

    def give_card(self, card_obj):
        current_cards = self.get_cards()
        card_index = current_cards.index(card_obj)
        selected_card = current_cards.pop(card_index)
        self.set_cards(current_cards)
        self.set_value()

        return selected_card

    def clear_cards(self):
        self.set_cards([])
        self.set_value()

    def update_card(self, card_obj, attribute_name, attribute_value):
        current_cards = self.get_cards()
        card_index = current_cards.index(card_obj)
        current_card = self.get_card(card_index)

        # Change the Card Attriubte
        if attribute_name == "value":
            current_card.set_value(attribute_value)
        elif attribute_name == "suit":
            current_card.set_suit(attribute_value)
            current_card.generate_name()
        elif attribute_name == "face":
            current_card.set_face(attribute_value)
            current_card.generate_name()

        # Update the Hand
        self.set_card(card_index, current_card)
        self.set_value()

    def ace_switch(self, card_obj):
        current_cards = self.get_cards()
        card_index = current_cards.index(card_obj)
        current_card = self.get_card(card_index)
        current_face = current_card.get_face()
        current_value = current_card.get_value()

        new_value = None
        if current_face == "Ace":
            if current_value == 11:
                new_value = 1
            elif current_value == 1:
                new_value = 11
        self.update_card(current_card, "value", new_value)

    def reset(self):
        current_cards = self.get_cards()
        current_cards = []
        self.set_cards(current_cards)
        self.set_value()