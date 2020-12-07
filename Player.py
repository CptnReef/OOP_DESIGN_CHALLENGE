from Item import Item
from Obstacle import Obstacle

class Player(Item, Obstacle):
    def __init__(self, move, interact):
        self.move = move
        self.interact = interact

    def Player_Mission(self):
        Item.fixed_Position(self)