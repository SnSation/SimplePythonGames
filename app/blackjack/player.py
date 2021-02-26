class Player:
    def __init__(self, name, display):
        self.name = name
        self.is_playing = 1
    
#         Hands: Playable Hands
#         {
#             Hand Number : {
#                 "cards" : List of Cards in Hand,
#                 "total" : Total Value of Cards in Hand,
#                 "bet" : Funds bet on Hand,
#                 "state": 1 = Played, 0 = Unplayed,
#                 "natural": 1 = Natural Blackjack
#             }
#         }
        self.hands = {
            1: {
                "cards": [],
                "total":0,
                "bet": 0,
                "state":0,
                "natural":0
            }
        }
        
#         Funds: Amount Available for Bet Method
        self.funds = 0
        
#         Actions: Player Actions
#         { Action Type : 
#             [
#                 Input: Action Description
#             ]
#         }
        self.actions = {
            "game": [
                ("q", "Leave the Game"),
                ("m", "Menu"),
            ],
            "hand": [
                ("h", "Hit"),
                ("s", "Stand"),
                ("t", "Split Hand"),
                ("a", "Switch Ace Value")
            ]
        }
        
#         Display: Information From Display Object
        self.display = display
        
    def __repr__(self):
        return f'< Player | Name: {self.name} >'
    
#     Name Methods
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    # Hand Methods
    def set_hands(self, hands):
        self.hands = hands
        
    def get_hands(self):
        return self.hands
    
    def set_hand(self, hand_number=1, cards=[], bet=0, state=0):
        self.hands[hand_number] = {
            "cards":cards,
            "total":sum(card.get_value() for card in cards),
            "bet":bet,
            "state":state,
            "natural":0
        }
        # Check for Bust
        if self.hands[hand_number]['total'] > 21:
            self.hands[hand_number]["state"] = 1
        # Check for Natural Blackjack
        if (len(self.hands[hand_number]["cards"]) == 2) and self.hands[hand_number]["total"] == 21:
            self.hands[hand_number]["natural"] = 1
        
    def get_hand(self, hand_number=1):
        return self.hands[hand_number]
        
    def set_hand_cards(self, cards=[], hand_number=1):
        self.hands[hand_number]["cards"] = cards
        
    def get_hand_cards(self, hand_number=1):
        return self.hands[hand_number]["cards"]
    
    def set_hand_total(self, hand_number=1):
        self.hands[hand_number]["total"] = sum(card.get_value() for card in self.hands[hand_number]["cards"])
        
    def get_hand_total(self, hand_number=1):
        return self.hands[hand_number]["total"]
    
    def set_hand_state(self, state, hand_number=1):
        self.hands[hand_number]["state"] = state
        
    def get_hand_state(self, hand_number=1):
        return self.hands[hand_number]["state"]
    
    def add_hand_card(self, card, hand_number=1):
        self.hands[hand_number]["cards"].append(card)
        self.set_hand_total(hand_number)
        
    def check_hand(self, hand_number=1):
        self.set_hand_total(hand_number)
        if self.hands[hand_number]["total"] >= 21:
            self.hands[hand_number]["state"] = 1
            return self.hands[hand_number]["state"]
        return self.hands[hand_number]["state"]        
        
    def reset_hands(self):
        empty_hand = {
            "cards":[],
            "total":0,
            "bet":0,
            "state":0,
            "natural":0
        }
        self.set_hands({1:empty_hand})
    
    # Funds Methods
    def set_funds(self, amount):
        self.funds = amount
        
    def get_funds(self):
        return self.funds
    
    def add_funds(self, amount):
        self.funds += amount
        
    def remove_funds(self, amount):
        self.funds -= amount    
    
    # Turn Methods
    def set_turn(self, turn):
        self.turn = turn
        
    def get_turn(self, turn):
        return self.turn
    
    def start_turn(self, deck):
        self.set_turn(1)
        
    def end_turn(self):
        self.set_turn(0)
        
    # Action Methods
    def set_actions(self, actions):
        self.actions = actions
    
    def get_actions(self):
        return self.actions
    
    def add_action(self, action_type, user_input, action_description):
        new_action = (user_input, action_description)
        if self.actions[action_type]:
            self.actions[action_type].append(new_action)
        else:
            self.actions[action_type] = [new_action]
        
    def get_action(self, action_type, identifier):
        for k,v in self.actions[action_type].items():
            if k == identifier:
                return v
            elif v == identifier:
                return v
            else:
                return None
        
    # Turn Action Methods    
    def bet(self, amount, hand_number=1):
        if (self.funds - amount) > 0:
            self.funds -= amount
            self.hands[hand_number]["bet"] = amount
        else:
            current_funds = self.funds
            self.funds = 0
            self.hands[hand_number]["bet"] = current_funds
        
    def hit(self, deck, hand_number=1):
        self.add_hand_card(deck.deal_card(), hand_number)
        self.set_hand_total(hand_number)
        
    def stand(self, hand_number=1):
        self.set_hand_total(hand_number)
        self.set_hand_state(1, hand_number)
    
    def switch_ace(self, hand_number=1):
        for card in self.hands[hand_number]["cards"]:
            if card.get_face() == "A":
                
                input_query = {
                    "prompt": f"Switch Value of the Ace of {card.get_suit()}?",
                    "options":["yes = 'y'", "no = 'n'"]
                }
                self.display.set_input_query(input_query)
                switch_card = self.display.get_user_input()
                
                if switch_card.lower() == "y":    
                    if card.get_value() == 11:
                        card.set_value(1)
                        self.set_hand_total(hand_number)
                    else:
                        card.set_value(11)
                        self.set_hand_total(hand_number)
        
    def split_hand(self, hand_number=1):
        if self.hands[hand_number]["cards"][0].get_face() == self.hands[hand_number]["cards"][1].get_face():
            # self.set_hand[len(self.hands)+1, [self.hands[hand_number]["cards"].pop()], self.hands[hand_number]["bet"], 0]
            # self.set_hand_total(hand_number)
            pass
    
    # Turn Methods
    def get_input(self, action_type):
        self.display.clear_input()
        
        for k,v in self.actions["game"]:
            self.display.add_input_option(f'Input "{k}" --- {v}')
        for k, v in self.actions[action_type]:
            self.display.add_input_option(f'Input "{k}" --- {v}')
            
        self.display.set_input_prompt("What would you like to do?")
        
        return self.display.get_user_input()
    
    def play_hand(self, deck, hand_number):
#         Get Player Action
        player_action = self.get_input("hand")

        if player_action == "q":
#             Remove Player from the Game
            pass
        elif player_action == "m":
#             Open Player Menu
            self.display.open_menu()
        elif player_action == "h":
#             Hit on this Hand
            self.hit(deck, hand_number)
        elif player_action == "s":
#             Stand on this Hand
            self.stand(hand_number)
        elif player_action == "a":
#             Switch Ace Value
            self.switch_ace(hand_number)
        elif player_action == "t":
#             Split Hand
            self.split_hand(hand_number)
        else:
#             Display Error Message
            self.display.set_error("Input Not Recognized")
            self.play_hand(deck, hand_number)
    
        self.display.update("Player", self)
                