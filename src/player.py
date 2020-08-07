# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, inventory):
        self.location = location
        self.inventory = inventory

    def setLocation(self, location):
        self.location = location

    def addItem(self, item):
        self.inventory.append(item)

    def dropItem(self, item):
        index = self.inventory.index(item)
        self.inventory.pop(index)

    def checkBag(self):
        if len(self.inventory) > 0:
            print("Your bag contains:")
            for item in self.inventory:
                print(item.name)
        else:
            print("Your bag is empty")

