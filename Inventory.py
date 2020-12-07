from random import randint

class Inventory:
    def __init__(self, inventory_Id, inventory_value, inventory_Slot):
        self.__inventory_Id = randint(100, inventory_Id)
        self._value = inventory_value
        self.inventory_Slot = dict(inventory_Slot)
    
    def inventory_Item(self, pack, item):
        self.inventory_Slot[pack] = item

    def check_Inventory(self,slot):
        slot = self.inventory_Slot
        for i,j in slot.items():
            print(f"Item: {i}, Quality: {j}.")
        return slot
    
# if __name__ == "__main__":
#     bag = Inventory(999, 101, {"pouch":99})

#     print(bag._Inventory__inventory_Id)
#     bag.inventory_Item("bag",21)
#     bag.inventory_Item("satchel",18)
#     print(bag.inventory_Slot)
#     bag.check_Inventory(bag.inventory_Item)