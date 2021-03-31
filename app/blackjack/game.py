from .display import Display
from .deck import Deck
from .player import Player
from .dealer import Dealer
from .interface import Interface
import random

class Game:
    def __init__(self):
        self.name = "Blackjack"

        # User: User Object for data save / load
        self.user = None

        # Display Object for viewing the game
        self.display = Display()

        # Interface Object for User Interaction
        self.interface = Interface()

        # State: State Object holding game data for save/load
        self.state = None

        # Deck Object for Card Storage
        self.deck = Deck()

        # Players Dictionary
        # {
        #     Player Name : Player Object
        # }
        self.players = {}

        # Dealer Object is the central object between interactions
        self.dealer = Dealer()

        # Turn Order
        self.order = []

        # Dictionary of Menu Objects
        # {
        #     Menu Name : Menu Object
        # }
        self.menus = {}

        # Amount of Money Bet / Unclaimed
        # This will go unused in this iteration of Blackjack
        self.pot = 0

        # History: List of actions taken throughout the game for saving state
        self.history = []
        
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

    def set_interface(self, interface_obj):
        self.interface = interface_obj

    def get_interface(self):
        return self.interface

    def set_state(self, state_obj):
        self.state = state_obj

    def get_state(self):
        return self.state

    def set_display(self, display_obj):
        self.display = display_obj

    def get_display(self):
        return self.display
        
    def set_menus(self, menus_dict):
        self.menus = menus_dict
        
    def get_menus(self):
        return self.menus
    
    def set_menu(self, menu_obj):
        current_menus = self.get_menus()
        menu_name = menu_obj.get_name()
        current_menus[menu_name] = menu_obj
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
            
    def set_player(self, player_obj):
        current_players = self.get_players()
        player_name = player_obj.get_name()
        current_players[player_name] = player_obj
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

    def insert_in_order(self, player_name, position):
        current_order = self.get_order()
        position_index = position - 1
        current_order.insert(position_index, player_name)
        self.set_order(current_order)

    def set_dealer(self, dealer_obj):
        self.dealer = dealer_obj

    def get_dealer(self):
        return self.dealer
        
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

    def award_pot(self, player_obj, amount):
        current_pot = self.get_pot()
        selected_player = player_obj
        winnings = amount
        if winnings > current_pot:
            winnings = current_pot
        selected_player.add_to_bankroll(winnings)
        self.remove_from_pot(winnings)

    # Display Methods
    def set_display_content(self, section_dict):
        current_display = self.display
        sections_added = []
        for section_index in range(len(section_dict.keys())):
            section_name = section_dict[section_index]["name"]
            section_content = section_dict[section_index]["content"]
            current_display.set_section(section_name, section_content)
            sections_added.append(section_name)
        self.set_display(current_display)

        return sections_added

    def update_display(self):
        current_display = self.get_display()

        section_dict = {
            1 : {
                "name": "Players",
                "content": [player.name for player in self.get_players()]
            },
            2 : {
                "name": "Deck",
                "content": [card.name for card in self.get_deck()]
            },
            3 : {
                "name": "Dealer",
                "content": [self.get_dealer().name()]
            },
            4 : {
                "name": "Order",
                "content": [f'Turn {self.order.index(participant) + 1}: {participant}' for participant in self.get_order()]
            },
        }

        current_display.set_order(self.set_display_content(section_dict))

        self.set_display(current_display)

    def new_display(self):
        new_display = Display()
        new_display.set_title("Blackjack")
        new_display.set_subtitle("By Alexander Blair")
        new_display.set_border_pattern(["#"])
        new_display.set_padding(2)
        new_display.set_width(300)
        new_display.set_height(300)
        self.set_display(new_display)
        self.update_display()
        new_display.show()


    # Blackjack Specific State Methods
    def save_state(self):
        pass

    def load_state(self):
        pass

    def clear_state(self):
        self.state = None

    # Initialization Methods
    def create_deck(self, amount=1):
        suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
        faces = [2, 3, 4, 5, 6, 7 , 8, 9, 10, "Jack", "Queen", "King", "Ace"]

        new_deck = Deck()
        new_deck.set_name(f'{self.name} Deck')
        new_deck.set_suits(suits)
        new_deck.set_faces(faces)
        new_deck.set_deck(amount)
        
        self.deck = new_deck

        return self.deck

    def create_players(self, amount=1):
        ui = self.interface
        players_created = []
        while len(players_created) < amount:
            new_player = Player()
            new_player.set_name(ui.input_name("player"))
            self.set_player(new_player)
            players_created.append(new_player)

    def create_order(self):
        all_players = self.get_players()
        print(all_players)
        # randomized_players = random.sample(all_players, len(all_players))
        # self.set_order(randomized_players)


            

    # Game Action Methods
    def start(self):
        print("Start")
        ui = self.interface

        deck_count = ui.input_count("deck")
        print("Building Deck")
        self.create_deck(deck_count)
        print("Deck Complete")
        print(self.get_deck())

        player_count = ui.input_count("player")
        print("Creating Players")
        self.create_players(player_count)
        print("Players Created")
        print(self.get_players())

        self.create_order()

    def play(self):
        self.start()
        self.new_display()
        

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