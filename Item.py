from Inventory import Inventory

class Item(Inventory):
    def __init__(self,item_Name, item_Location ,itemId, value, item_Slot):
        super().__init__(itemId, value, item_Slot)
        self.item_Name = item_Name
        self.item_Location = item_Location

    def 
        
