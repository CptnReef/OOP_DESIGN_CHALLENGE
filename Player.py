from Item import Item
from Obstacle import Obstacle

class Player(Item, Obstacle):

    def __init__(self, inventory_Id, inventory_value, inventory_Slot, available_Item, x,y,name,start,move,carry):
        Item.__init__(self, inventory_Id, inventory_value, inventory_Slot, available_Item)
        Obstacle.__init__(self, carry)
        self.check_Inventory(self.carry)
        
    def inventory_Item(self, pack, item):
        Item.inventory_Item(self, pack, item)

    def fixed_Position(self):
        Item.fixed_Position(self)

    def player_Move(self):
        self.inventory_Item("",1)
        print(" [W]up [S]down [A]left [D]right [I]check_items [Q]search_items")
        Obstacle.player_Move(self)
        
# if __name__ == "__main__":
#     bob = Player(333, 30, {"another_Slot":100}, {"available_Slot":100}, 1,1,"","","",{})
    # print(bob._value)
    # print(bob.inventory_Slot)
    # print(bob.available_Item)
    # bob.inventory_Item("",1)
    # bob.fixed_Position()
    # bob.player_Move()
    # bob.player_Move()