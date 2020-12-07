class Obstacle:
    def __init__(self, move, interact):
        self.move = move
        self.interact = interact
    
    def board(self):
        x = 15
        y = 15
        self.grid = (x,y)

    def object(self):
        pass
        
    def colliding(self):
        pass
        