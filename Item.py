from Inventory import Inventory

class Item(Inventory):
    def __init__(self, itemId, value, item_Slot, available_Item):
        super().__init__(itemId, value, item_Slot)
        self.available_Item = available_Item

    def all_Items(self):
        items = {"Bunny Slippers":10, "Nerf-Gun":100, "McMuffin":1000}
        self.item_Slot = items
        self.available_Item = self.item_Slot
    
    def item_Position(self):
        pos = [(3,14),(7,14),(12,1)]
        convertion = []
        keyItem = []
        # print(f"Items Coordinates:")
        for key,value in self.available_Item.items():
            convertion.append(key)
            keyItem.append(value)
            # print(f"{convertion}")
        self.keyItem1 = f"Item: {convertion[0]} Coordinates: {pos[0]} Points: {keyItem[0]}"
        self.keyItem2 = f"Item: {convertion[1]} Coordinates: {pos[1]} Points: {keyItem[1]}"
        self.keyItem3 = f"Item: {convertion[2]} Coordinates: {pos[2]} Points: {keyItem[2]}"
        # print(self.keyItem1)
        # print(self.keyItem2)
        # print(self.keyItem3)
        
# if __name__ == "__main__":

#     fixed_items = Item(333, 30, {"key": 24}, {"it": 411})
#     print(fixed_items._value)
#     print(fixed_items.item_Slot)
#     fixed_items.all_Items()
#     print(fixed_items.available_Item)
#     fixed_items.item_Position()
#     print(fixed_items.keyItem3)
    
