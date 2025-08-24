import random
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
            player.buy_property(self.name, self.price)
            self.owner = player
            return True
        return False

    def charge_rent(self, player):
        if self.is_owned() and self.owner != player:
            player.pay(self.rent)
            self.owner.receive(self.rent)
class Board:
    def __init__(self):
        self.spaces = [None] * 40
        self.spaces[0] = "Go"
        self.spaces[10] = "Jail"
        self.spaces[20] = "Free Parking"
        self.spaces[30] = "Go To Jail"

    def place_property(self, index, property_obj):
        if 0 <= index < len(self.spaces):
            self.spaces[index] = property_obj

    def get_space(self, index):
        return self.spaces[index]

class Game:
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.current_turn = 0

    def roll_dice(self):
        return random.randint(1, 6) + random.randint(1, 6)

    def next_turn(self):
        player = self.players[self.current_turn]
        steps = self.roll_dice()
        player.move(steps)
        tile = self.board.spaces[player.position]

        if isinstance(tile, Property):
            if not tile.is_owned():
                bought = tile.buy(player)
                if bought:
                    print(f"{player.name} bought {tile.name}")
            else:
                tile.charge_rent(player)

        self.current_turn = (self.current_turn + 1) % len(self.players)

player1 = Player("Alice")
boardwalk = Property("Boardwalk", 400, 50)
boardwalk.buy(player1)
print(player1.money, player1.properties)