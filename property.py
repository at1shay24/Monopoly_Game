class Property:
    def __init__(self, name, price, base_rent, house_cost=50):
        self.name = name
        self.price = price
        self.base_rent = base_rent
        self.owner = None
        self.houses = 0
        self.hotel = False
        self.house_cost = house_cost

    def is_owned(self):
        return self.owner is not None

    def buy(self, player):
        if not self.is_owned() and player.money >= self.price:
            player.money -= self.price
            player.properties.append(self)
            self.owner = player
            return True
        return False

    def build_house(self, player):
        if self.owner == player and not self.hotel:
            if self.houses < 4: 
                if player.money >= self.house_cost:
                    player.money -= self.house_cost
                    self.houses += 1
                    print(f"{player.name} built a house on {self.name}. Total houses: {self.houses}")
                    if self.houses == 4:
                        print(f"{self.name} now has 4 houses and is eligible for a hotel upgrade!")
                    return True
        return False

    def build_hotel(self, player):
        if self.owner == player and self.houses == 4 and not self.hotel:
            if player.money >= self.house_cost * 2:
                player.money -= self.house_cost * 2
                self.houses = 0
                self.hotel = True
                print(f"{player.name} upgraded {self.name} to a HOTEL!")
                return True
        else:
            print(f"{self.name} cannot be upgraded to a hotel yet (needs 4 houses first).")
        return False
    
    def get_rent(self):
        if self.hotel:
            return self.base_rent * 5
        return self.base_rent + (self.houses * (self.base_rent // 2))

    def charge_rent(self, player):
        if self.is_owned() and self.owner != player:
            rent_amount = self.get_rent()
            player.pay(rent_amount)
            self.owner.receive(rent_amount)
            print(f"{player.name} paid ${rent_amount} rent to {self.owner.name} for {self.name}")