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
        old_position = self.position
        self.position = (self.position + steps) % 40
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

    def owns_full_set(self, property_obj, board):
        group_color = property_obj.color
        group_props = [p for p in board.spaces if hasattr(p, "color") and p.color == group_color]
        return all(p in self.properties for p in group_props)

    def build_house(self, property_obj, board):
        if property_obj in self.properties and self.owns_full_set(property_obj, board):
            return property_obj.build_house(self)
        else:
            print(f"{self.name} cannot build a house on {property_obj.name} without owning full set.")
            return False

    def build_hotel(self, property_obj, board):
        if property_obj in self.properties and self.owns_full_set(property_obj, board):
            return property_obj.build_hotel(self)
        else:
            print(f"{self.name} cannot build a hotel on {property_obj.name} without owning full set.")
            return False

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

    def __str__(self):
        props = [
            f"{p.name} (Houses: {p.houses}, Hotel: {'Yes' if p.hotel else 'No'})"
            for p in self.properties
        ]
        return f"{self.name}: ${self.money}, Position {self.position}, Properties: {props}"