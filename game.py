import random
from player import Player
from property import Property

class Game:
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.current_player_index = 0
        self.running = True

    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)

    def next_turn(self):
        player = self.players[self.current_player_index]
        print(f"\n--- {player.name}'s Turn ---")

        if player.in_jail:
            die1, die2 = self.roll_dice()
            print(f"{player.name} rolled {die1} and {die2} trying to get out of jail...")
            if not player.attempt_jail_exit(die1, die2):
                self.next_player()
                return

        die1, die2 = self.roll_dice()
        steps = die1 + die2
        print(f"{player.name} rolled {die1} and {die2} → moving {steps} spaces.")
        player.move(steps)

        space = self.board.spaces[player.position]

        if isinstance(space, Property):
            if not space.is_owned():
                print(f"{space.name} is unowned and costs ${space.price}.")
                if player.money >= space.price:
                    choice = input(f"Do you want to buy {space.name}? (y/n): ").lower()
                    if choice == 'y':
                        space.buy(player)
                        print(f"{player.name} bought {space.name}!")

            elif space.owner != player:
                space.charge_rent(player)

            else:
                # Player owns it, maybe build a house or hotel
                if player.owns_full_set(space, self.board):
                    print(f"You own all properties of {space.color}! You can build on {space.name}.")
                    action = input("Build (house/hotel/none)? ").lower()
                    if action == "house":
                        player.build_house(space, self.board)
                    elif action == "hotel":
                        player.build_hotel(space, self.board)
                else:
                    print(f"You don't own all {space.color} properties yet.")

        else:
            print(f"{player.name} landed on a non-property space: {space}")

        self.check_bankruptcy(player)
        self.next_player()

    def check_bankruptcy(self, player):
        if player.money < 0:
            print(f"{player.name} is bankrupt and out of the game!")
            self.players.remove(player)
            if len(self.players) == 1:
                print(f"\n🏆 {self.players[0].name} wins the game!")
                self.running = False

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play(self):
        while self.running:
            self.next_turn()