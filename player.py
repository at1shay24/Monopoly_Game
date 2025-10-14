from property import Property

class Player:
    def __init__(self, name, money=1500):
        self.name = name
        self.money = money
        self.position = 0
        self.properties = []
        self.in_jail = False
        self.jail_turns = 0

    def move(self, steps):
        if self.in_jail:
            print(f"{self.name} is in Jail and cannot move!")
            return
        old_pos = self.position
        self.position = (self.position + steps) % 40
        if self.position < old_pos:  # Passed Go
            self.money += 200
            print(f"{self.name} passed Go and collected $200!")

    def pay(self, amount):
        self.money -= amount

    def receive(self, amount):
        self.money += amount

    def buy_property(self, prop):
        if self.money >= prop.price:
            self.money -= prop.price
            self.properties.append(prop)
            prop.owner = self
            print(f"{self.name} bought {prop.name}")
            return True
        return False

    def owns_full_set(self, prop, board):
        group = prop.color
        group_props = [p for p in board.spaces if hasattr(p, "color") and p.color == group]
        return all(p in self.properties for p in group_props)

    def go_to_jail(self):
        self.in_jail = True
        self.jail_turns = 0
        self.position = 10
        print(f"{self.name} has been sent to Jail!")

    def attempt_jail_exit(self, die1, die2):
        if die1 == die2:
            self.in_jail = False
            self.jail_turns = 0
            print(f"{self.name} rolled doubles and is free from Jail!")
            return True
        else:
            self.jail_turns += 1
            if self.jail_turns >= 3:
                self.pay(50)
                self.in_jail = False
                self.jail_turns = 0
                print(f"{self.name} paid $50 after 3 turns and is free from Jail!")
                return True
        return False