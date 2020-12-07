from Item import Item
from Obstacle import Obstacle

class Player(Item, Obstacle):

    def __init__(self, inventory_Id, inventory_value, inventory_Slot, available_Item, move, interact):
        Item.__init__(self, inventory_Id, inventory_value, inventory_Slot, available_Item)
        self.move = move
        self.interact = interact
        name = input("Enter Name:")
        self.name = print(f"Hi {name}, We're going on an adventure!")
        start = input("unless that's alright with you? [Yes/No]")
        self.start = print(f"{start}...")

    def inventory_Item(self, pack, item):
        Item.inventory_Item(self, pack, item)

    def fixed_Position(self):
        Item.fixed_Position(self)

    def pick_Up(self):
        pass

if __name__ == "__main__":
    bob = Player(333, 30, {"another_Slot":100}, {"available_Slot":100},"","")
    # print(bob._value)
    # print(bob.inventory_Slot)
    # print(bob.available_Item)
    # bob.inventory_Item("",1)
    # bob.fixed_Position()
    bob.name
    bob.start