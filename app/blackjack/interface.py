from .player import Player

class Interface:
    def __init__(self):
        self.name = None

    def __repr__(self):
        return f'< Interface | Name: {self.name} >'

    # Getters and Setters
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def input_count(self, object_name):
        response = input(f"How many {object_name.title()}s? [Integer]\n")
        return int(response)

    def input_name(self, object_type):
        response = input(f'What is the name of the new {object_type.title()}? [Text]\n')
        return response