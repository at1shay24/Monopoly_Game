class Player:
    def __init__(self, name, money=1500):
        self.name = name
        self.money = money
        self.position = 0
        self.properties = []
        self.in_jail = False

    def move(self, steps):
        old_position = self.position
        self.position = (self.position + steps) % 40

        # Passed 'Go'
        if self.position < old_position:
            self.money += 200
            print(f"{self.name} passed Go and collected $200!")

    def pay(self, amount):
        self.money -= amount

    def receive(self, amount):
        self.money += amount

    def buy_property(self, property_obj):
        if self.money >= property_obj.price:
            self.money -= property_obj.price
            self.properties.append(property_obj)
            return True
        return False
    
    def __str__(self):
        return f"{self.name}: ${self.money}, Position {self.position}, Properties: {[p.name for p in self.properties]}"