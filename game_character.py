class GameCharacter:         
    def __init__(self, name): 
        self.name = name 
        self.level = 1 
         
    def greet(self): 
        print(f"Hello, I'm {self.name}, level {self.level}")
