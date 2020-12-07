from Inventory import Inventory

class Item(Inventory):
    def __init__(self, inventory_Id, inventory_value, inventory_Slot, available_Item):
        super().__init__(inventory_Id, inventory_value, inventory_Slot)
        self.available_Item = available_Item

    def inventory_Item(self, pack, item):
        super().inventory_Item( pack, item) 
        self.available_Item = {"Bunny Slippers":10, "Nerf-Gun":100, "McMuffin":1000}
        self.inventory_Slot = self.available_Item
        return self.check_Inventory(self.available_Item)
        
    def fixed_Position(self):
        print("____________________________________________________")
        print(f"\nFixed Items:\n")
        pos = {"Item no.1":(3,14),"Item no.2":(7,14),"Item no.3":(12,1)}
        self.inventory_Item("",1)
        print("____________________________________________________")
        print(f"\nItems Coordinates:\n")
        for i,j in pos.items():
            print(f"{i} Coordinates: {j}")
        print("____________________________________________________")

        
if __name__ == "__main__":

    set_items = Item(333, 30, {"item_Slot":100}, {"available_Slot":100})
    # print(set_items._Inventory__inventory_Id)
    # print(set_items._value)
    # print(set_items.available_Item)
    # print(set_items.inventory_Slot)
    # print(set_items.inventory_Item("overrided",220))
    set_items.fixed_Position()
    
