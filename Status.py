from Item import Item

class Status(Item):
    def __init__(self, interact):
        self.interact = interact
    
    def cause(self, effect):
        self.interact = effect

        if self.interact == self.interact:
            effect = effect.remove(self.keyItem1)
        else:
            False

    def obstacle(self):
        self.interact = [
            {"burn":print("you've been burned!")},
            {"bite":print("you've been eaten alive!")},
            {"crash":print("you've went out of boundary")},
            ]
