class Player:
    def __init__(self, name, money=1500):
        self.name = name
        self.money = money
        self.position = 0
        self.properties = []

    def move(self, steps):
        self.position = (self.position + steps) % 40

    def pay(self, amount):
        self.money -= amount

    def receive(self, amount):
        self.money += amount

    def buy_property(self, property_name, price):
        if self.money >= price:
            self.money -= price
            self.properties.append(property_name)
            return True
        return False