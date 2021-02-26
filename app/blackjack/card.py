class Card:
    def __init__(self):
        self.name = None
        self.suit = None
        self.face = None
        self.value = None
                
    def __repr__(self):
        return f'< Card | {self.face} | {self.suit} >'

    # Getters and Setters
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
        
    def set_suit(self, suit):
        self.suit = suit
        
    def get_suit(self):
        return self.suit
    
    def set_face(self, face):
        self.face = face
        
    def get_face(self):
        return self.face
    
    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    # Card Action Methods
    def valuate(self):
        if self.face == "Ace":
            self.value = 11
        elif isinstance(self.face, int):
            self.value = self.face
        else:
            self.value = 10