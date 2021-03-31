import random
from .card import Card

class Deck:
    def __init__(self):
        self.name = "Deck"
        self.suits = []
        self.faces = []
        self.cards = []
        
    def __repr__(self):
        return f'< Deck | Cards: {len(self.cards)} >'

    # Getters and Setters
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
        
    def set_suits(self, suit_list):
        self.suits = suit_list
        
    def get_suits(self):
        return self.suits

    def add_suit(self, suit_name):
        current_suits = self.get_suits()
        current_suits.append(suit_name)
        self.set_suits(current_suits)

    def remove_suit(self, suit_name):
        current_suits = self.get_suits()
        current_suits.remove(suit_name)
        self.set_suits(current_suits)

    def set_faces(self, face_list):
        self.faces = face_list
        
    def get_faces(self):
        return self.faces

    def add_face(self, face_name):
        current_faces = self.get_faces()
        current_faces.append(face_name)
        self.set_faces(current_faces)

    def remove_face(self, face_name):
        current_faces = self.get_faces()
        current_faces.remove(face_name)
        self.set_faces(current_faces)

    def set_cards(self, card_list):
        self.cards = card_list
        
    def get_cards(self):
        return self.cards

    def add_card(self, card_obj):
        current_cards = self.get_cards()
        current_cards.append(card_obj)
        self.set_cards(current_cards)

    def remove_card(self, card_name, amount = 1):
        current_cards = self.get_cards()
        cards_removed = 0
        current_index = 0
        while cards_removed < amount:
            current_card = current_cards[current_index]
            if current_card.name == card_name:
                current_cards.remove(current_card)
                cards_removed += 1
            if current_index == (len(current_cards) - 1):
                break
        
        self.set_cards(current_cards)

    # Deck Initialization
    def set_deck(self, deck_count=1):
        current_suits = self.get_suits()
        current_faces = self.get_faces()

        decks_built = 0
        cards_built = 0
        while decks_built < deck_count:
            for suit in current_suits:
                for face in current_faces:
                    new_card = Card()
                    new_card.set_suit(suit)
                    new_card.set_face(face)
                    new_card.generate_name()
                    new_card.valuate()
                    self.add_card(new_card)
                    cards_built += 1
                    # print(f'{cards_built} Cards Created')
            decks_built += 1
            

    # Deck Action Methods
    def take_cards(self, amount=1):
        current_cards = self.get_cards()
        cards_taken = []
        while len(cards_taken) < amount:
            cards_taken.append(current_cards.pop())

        self.set_cards(current_cards)

        return cards_taken

    