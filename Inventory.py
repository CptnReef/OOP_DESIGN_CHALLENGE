from random import randint

class Inventory:
    def __init__(self, itemId, value, item_Slot):
        self.__itemId = randint(100, itemId)
        self._value = value
        self.item_Slot = dict(item_Slot)
    
    def inventory_Item(self, item, quality):
        self.item_Slot[item] = quality

    def check_Item(self):
        slot = self.item_Slot.items()
        for i,j in slot:
            print(f"Item: {i}, PowerLevel: {j}.")
    
# if __name__ == "__main__":
#     bag = Inventory(999, 100, {"pouch":100})

#     print(bag._Inventory__itemId)
#     bag.inventory_Item("bag",10)
#     bag.inventory_Item("satchel",1)
#     print(bag.item_Slot)
#     bag.check_Item()

