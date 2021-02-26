class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        self.name = f'{self.face.upper}_of_{self.suit.upper}'
        self.value = 0
        
        self.valuate()
        
    def __repr__(self):
        return f'< Card | {self.face} | {self.suit} >'
        
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
    
    def valuate(self):
        if self.face == "A":
            self.value = 11
        elif isinstance(self.face, int):
            self.value = self.face
        else:
            self.value = 10