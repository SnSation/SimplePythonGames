from .deck import Deck
from .dealer import Dealer
from .display import Display

class Game:
    def __init__(self, player_count=1):
        self.name = "Blackjack"
        self.user = None
        self.menus = {}
        self.deck = Deck()
        self.dealer = Dealer()
        self.players = {}
        self.humans = player_count
        self.order = []
        self.pot = 0
        self.running = 0
        self.display = Display()
        
    def __repr__(self):
        return f'< Blackjack | Name: {self.name} >'
        
    def set_user(self, user):
        self.user = user
        
    def get_user(self):
        return self.user
        
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_menus(self, menus):
        self.menus = menus
        
    def get_menus(self):
        return self.menus
    
    def add_menu(self, menu):
        self.menus[menu.name] = menu
    
    def remove_menu(self, menu):
        del self.menus[menu.name]
        
    def get_menu(self, menu_name):
        return self.menus[menu_name]
    
    def set_deck(self, deck):
        self.deck = deck
        
    def get_deck(self):
        return self.deck
    
    def set_players(self, players):
        self.players = players
    
    def get_players(self):
        return self.players
            
    def add_player(self, player):
        self.players[player.name] = player
        
    def remove_player(self, player_name):
        return self.players[player_name]
        
    def get_player(self, player_name):
        return self.players[player_name]
    
    def set_order(self):
        self.order = []
        for player in self.players:
            self.order.append(player)
            
    def get_order(self):
        return self.order
    
    def remove_from_order(self, player):
        self.order.remove(player)
        
    def set_pot(self, pot):
        self.pot = pot
        
    def get_pot(self):
        return self.pot