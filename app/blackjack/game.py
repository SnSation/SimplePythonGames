from .deck import Deck
from .dealer import Dealer
from .display import Display

class Game:
    def __init__(self):
        self.name = "Blackjack"
        # User: User Object for data save / load
        self.user = None
        # State: Dictionary for saving / loading game state
        self.state = { }
        # Display Object for viewing the game
        self.display = None
        self.deck = None
        self.players = {}
        self.order = []
        # Turn: Dictionary of actions taken during a turn for saving state
        self.turn = {}
        # History: List of actions taken throughout the game for saving state
        self.history = []
        # Dictionary of Menu Objects
        # {
        #     Menu Name : Menu Object
        # }
        self.menus = {}
        self.dealer = None
        self.pot = 0
        
    def __repr__(self):
        return f'< Blackjack | Name: {self.name} >'
        
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_user(self, user_obj):
        self.user = user_obj
        
    def get_user(self):
        return self.user

    def set_state(self, state_dict):
        self.state = state_dict

    def get_state(self):
        return self.state

    def add_state(self, state_name, state_value):
        current_state = self.get_state()
        current_state[state_name] = state_value
        self.set_state(current_state)

    def remove_state(self, state_name):
        current_state = self.get_state()
        del current_state[state_name]
        self.set_state(current_state)

    def set_display(self, display_obj):
        self.display = display_obj

    def get_display(self):
        return self.display
        
    def set_menus(self, menus_dict):
        self.menus = menus_dict
        
    def get_menus(self):
        return self.menus
    
    def add_menu(self, menu_obj):
        current_menus = self.get_menus()
        current_menus[menu_obj.name] = menu_obj
        self.set_menus(current_menus)
    
    def remove_menu(self, menu_name):
        current_menus = self.get_menus()
        del current_menus[menu_name]
        self.set_menus(current_menus)
        
    def get_menu(self, menu_name):
        current_menus = self.get_menus()
        return current_menus[menu_name]
    
    def set_deck(self, deck_obj):
        self.deck = deck_obj
        
    def get_deck(self):
        return self.deck
    
    def set_players(self, players_dict):
        self.players = players_dict
    
    def get_players(self):
        return self.players
            
    def add_player(self, player_obj):
        current_players = self.get_players()
        current_players[player_obj.name] = player_obj
        self.set_players(current_players)
        
    def remove_player(self, player_name):
        current_players = self.get_players()
        del current_players[player_name]
        
    def get_player(self, player_name):
        current_players = self.get_players()
        return current_players[player_name]
    
    def set_order(self, player_list):
        self.order = player_list
            
    def get_order(self):
        return self.order

    def add_to_order(self, player_name):
        current_order = self.get_order()
        current_order.append(player_name)
        self.set_order(current_order)
    
    def remove_from_order(self, player_name):
        current_order = self.get_order()
        current_order.remove(player_name)
        self.set_order(current_order)
        
    def set_pot(self, amount):
        self.pot = amount
        
    def get_pot(self):
        return self.pot

    def add_to_pot(self, amount):
        current_pot = self.get_pot()
        current_pot += amount
        self.set_pot(current_pot)

    def remove_from_pot(self, amount):
        current_pot = self.get_pot()
        if current_pot - amount > 0:
            current_pot -= amount
        else:
            current_pot = 0
        self.set_pot(current_pot)

    def get_from_pot(self, amount):
        current_pot = self.get_pot()
        payout = amount
        if current_pot < amount:
            payout = current_pot
        
        self.remove_from_pot(amount)

        return payout

    # Initialization Methods
    def create_deck(self, deck_count=1):
        # print("Building Deck")
        suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
        faces = [2, 3, 4, 5, 6, 7 , 8, 9, 10, "Jack", "Queen", "King", "Ace"]

        new_deck = Deck()
        new_deck.set_name(f'{self.name} Deck')
        new_deck.set_suits(suits)
        new_deck.set_faces(faces)
        new_deck.set_deck(deck_count)
        
        self.deck = new_deck
        # print("Deck Built")

    # Game Action Methods
    def save_state(self):
        pass

    def load_state(self, state_dict):
        pass

    def start(self):
        print("Start")

    def play(self):
        print("Play")
        

# Module Functions
# def new_game(self):
#         self.create_deck()

#         # Test Functions
#         deck_name = self.deck.get_name()
#         print(deck_name)
#         game_deck = self.deck
#         game_deck.set_name("Test Name")
#         print(game_deck.get_name())
#         print(self.deck.get_name())

# Test Section