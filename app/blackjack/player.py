from .hand import Hand
from .display import Display

class Player:
    def __init__(self):
        self.name = None

        # Bankroll: Amount available for Betting
        self.bankroll = None

        # Hands: List of Hand Objects
        self.hands = []

        # Display: The Display Object to be used as a Perspective in the Game Display
        self.display = None
        
    def __repr__(self):
        return f'< Player | Name: {self.name} >'

    # Getters and Setters    
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def set_bankroll(self, amount):
        self.bankroll = amount

    def get_bankroll(self):
        return self.bankroll

    def set_hands(self, hands_list):
        self.hands = hands_list

    def get_hands(self):
        return self.hands

    def set_hand(self, hand_index, hand_obj):
        current_hands = self.get_hands()
        new_hand = hand_obj
        if hand_index < len(current_hands):
            current_hands[hand_index] = new_hand
        else:
            current_hands.append(new_hand)

        self.set_hands(current_hands)

    def get_hand(self, hand_index):
        current_hands = self.get_hands()
        return current_hands[hand_index]

    def set_display(self, display_obj):
        self.display = display_obj

    def get_display(self):
        return self.display

    # Player Action Methods
    # Bankroll Interaction
    def add_to_bankroll(self, amount):
        current_bankroll = self.get_bankroll()
        current_bankroll += amount
        self.set_bankroll(current_bankroll)
        
    def remove_from_bankroll(self, amount):
        current_bankroll = self.get_bankroll
        amount_to_remove = amount
        if amount_to_remove > current_bankroll:
            amount_to_remove = current_bankroll

        current_bankroll -= amount_to_remove
        self.set_bankroll(current_bankroll)

        return amount_to_remove

    # Hand Interaction
    def bet(self, hand_index, amount):
        selected_hand = self.get_hand(hand_index)
        current_bet = self.remove_from_bankroll(amount)

        selected_hand.set_bet(current_bet)
        self.set_hand(hand_index, selected_hand)

    def add_hand(self, hand_obj):
        current_hands = self.get_hands()
        current_hands.append(hand_obj)
        self.set_hands(current_hands)

    def new_hand(self, card_list=[]):
        current_hands = self.get_hands()
        new_hand = Hand()
        hand_name = len(current_hands) + 1
        new_hand.set_name(hand_name)
        new_hand.set_cards(card_list)
        new_hand.set_value()
        
        return new_hand

    def split_hand(self, hand_obj):
        current_hands = self.get_hands()
        current_index = current_hands.index(hand_obj)
        current_hand = self.get_hand(current_index)
        first_card = current_hand.get_card(0)
        second_card = current_hand.get_card(1)
        current_bet = current_hand.get_bet()

        if first_card.get_face() == second_card.get_face():
            second_hand = self.new_hand([current_hand.give_card(second_card)])
            self.add_hand(second_hand)
            
            second_index = len(self.get_hands()) - 1
            self.bet(second_index, current_bet)

            second_hand.set_split(True)
            self.set_hand(second_index, second_hand)
            current_hand.set_split(True)
            self.set_hand(current_index, current_hand)

        self.set_hands(current_hands)

    def check_hand(self, hand_index):
        current_hand = self.get_hand(hand_index)

        # Make sure Hand is Updated
        current_hand.set_natural()
        current_hand.set_bust()

        # Auto-Attempt Ace Switch if Bust
        bust = current_hand.get_bust()
        if bust == True:
            current_cards = current_hand.get_cards()
            for card in current_cards:
                if (card.get_face() == "Ace") and (card.get_value() == 11):
                    current_hand.ace_switch(card)
            current_hand.set_bust()

        self.set_hand(hand_index, current_hand)

        return current_hand 
        
    def clear_hands(self):
        cleared_hands = []
        self.set_hands(cleared_hands)

    # Display Methods
    def column_format(self, column_width, text):
        character_count = len(text)
        space_remaining = column_width - character_count
        whitespace = " " * space_remaining
        formatted_string = text + whitespace

        return formatted_string

    def display_name(self):
        current_display = self.get_display()
        section_name = "Name"
        content_list = []

        entry = f'Player Name: {self.get_name()}'
        content_list.append(entry)

        current_display.set_section(section_name, content_list)
        self.set_display(current_display)

        return section_name
    
    def display_bankroll(self):
        current_display = self.get_display()
        section_name = "Bankroll"
        content_list = []

        entry = f'Current Bankroll: {self.get_bankroll()}'
        content_list.append(entry)

        current_display.set_section(section_name, content_list)
        self.set_display(current_display)

        return section_name   

    def display_hands(self):
        current_display = self.get_display()
        current_hands = self.get_hands()
        
        # Display.show() prints in rows, so hand data needs to be formatted
        # into columns with whitespace. This is SUPER inelegant...
        row_content = []
        column_width = 24

        # Set up Column 1: The Labels
        labels = ["Hand:", "Bet:", "Total:"]
        label_column = []
        for label in labels:
            formatted_text = self.column_format(column_width, label)
            label_column.append(formatted_text)

        # Each Hand needs its own column
        data_columns = []
        for hand_index in range(len(current_hands)):
            current_column = []
            current_hand = self.check_hand(hand_index)

            name = f'{current_hand.get_name()}'
            current_column.append(name)

            bet = f'{current_hand.get_bet()}'
            current_column.append(bet)

            total = f'{current_hand.get_value()}'
            current_column.append(total)

            card_count = 0
            for card in current_hand.get_cards():
                # Add Card Counter labels to the Label column if its not there yet
                card_count += 1
                card_label = f'Card {card_count}:'
                formatted_label = self.column_format(column_width, card_label)
                if formatted_label not in label_column:
                    label_column.append(formatted_label)

                # Add each Card Name and Value to the Hand column
                card_text = f'{card.get_name()} | {card.get_value()}'
                formatted_text = self.column_format(column_width, card_text)
                current_column.append(formatted_text)
            
            data_columns.append(current_column)
        
        # Create Continuous Strings from Each Column
        for row_index in range(len(label_column)):
            row_list = []
            blank_cell = " " * column_width
            row_list.append(label_column[row_index])
            for column in data_columns:
                if row_index < len(column):
                    row_list.append(column[row_index])
                else:
                    # Add Whitespace if there's no data
                    row_list.append(blank_cell)
            # Create a string and add it to row_content
            row_string = "".join(row_list)
            row_content.append(row_string)

        content_order = []
        # Create a new section for each row we created
        for row in row_content:
            section_name = row[0].rstrip()
            current_display.set_section(section_name, row)
            # List these Rows in ORDER for Display.set_order()
            content_order.append(section_name)

        self.set_display(current_display)

        return content_order             

    def display_options(self):
        pass


    def update_display(self):
        current_display = self.get_display()
        display_order = []

        display_order.append(self.display_name())

        display_order.append(self.display_bankroll())

        for section in self.display_hands():
            display_order.append(section)

        # display_order.append(self.display_options())

        current_display.set_order(display_order)
        self.set_display(current_display)


    def new_display(self):
        new_display = Display()
        new_display.set_title("Player Perspective")
        new_display.set_subtitle("Your Turn")
        new_display.set_border_pattern(["~"])
        new_display.set_padding(1)
        new_display.set_width(300)
        new_display.set_height(300)
        self.set_display(new_display)
        self.update_display()
        
    # Turn Methods
    def play_hand(self, hand_obj):
        pass
    
    def play_turn(self):
        pass
        
    def hit(self, hand_obj):
        pass
        
    def stand(self, hand_obj):
        pass