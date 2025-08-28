class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

    def is_owned(self):
        return self.owner is not None

    def buy(self, player):
        if not self.is_owned() and player.money >= self.price:
            player.money -= self.price
            player.properties.append(self)
            self.owner = player
            return True
        return False
    
    def charge_rent(self, player):
        if self.is_owned() and self.owner != player:
            player.pay(self.rent)
            self.owner.receive(self.rent)