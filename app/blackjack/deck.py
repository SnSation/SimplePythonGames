import random
from .card import Card

class Deck:
    def __init__(self):
        self.name = "Deck"
        self.cards = []
        self.decks = 1
        self.suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
        self.faces = [2, 3, 4, 5, 6, 7 , 8, 9, 10, "J", "Q", "K", "A"]
        
    def __repr__(self):
        return f'< Deck | Cards: {len(self.cards)} >'
        
    def set_cards(self, cards):
        self.cards = cards
        
    def get_cards(self):
        return self.cards
    
    def set_decks(self, deck_count):
        self.decks = deck_count
        
    def get_decks(self):
        return self.decks
    
    def set_suits(self, suits):
        self.suits = suits
        
    def get_suits(self):
        return self.suits
    
    def set_faces(self, faces):
        self.faces = faces
        
    def get_faces(self, faces):
        return self.faces
    
    def shuffle_cards(self):
        new_cards = []
        for card in self.cards:
            card_index = random.randint(0, (len(self.cards)-1))
            new_cards.append(self.cards.pop(card_index))
        self.cards = new_cards
    
    def reset_cards(self):
        self.cards = []
        for i in range(self.decks):
            for suit in self.suits:
                for face in self.faces:
                    new_card = Card(suit, face)
                    self.cards.append(new_card)
                    
    def deal_card(self):
        return self.cards.pop()