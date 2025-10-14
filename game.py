import random
from dice import Dice
from player import Player
from property import Property

class Game:
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.current_player = 0
        self.running = True

    def next_turn(self):
        player = self.players[self.current_player]
        print(f"\n--- {player.name}'s Turn ---")
        
        if player.in_jail:
            die1, die2, _ = Dice.roll()
            print(f"{player.name} rolled {die1} & {die2} trying to get out of jail...")
            if not player.attempt_jail_exit(die1, die2):
                self.next_player()
                return

        die1, die2, total = Dice.roll()
        print(f"{player.name} rolled {die1} + {die2} = {total}")
        player.move(total)
        space = self.board.spaces[player.position]

        if isinstance(space, Property):
            if not space.is_owned():
                if player.money >= space.price:
                    choice = input(f"Do you want to buy {space.name} for ${space.price}? (y/n): ").lower()
                    if choice == "y":
                        player.buy_property(space)
            elif space.owner != player:
                space.charge_rent(player)

        else:
            print(f"{player.name} landed on {space}")

        self.check_bankruptcy(player)
        self.next_player()

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def check_bankruptcy(self, player):
        if player.money < 0:
            print(f"{player.name} is bankrupt!")
            self.players.remove(player)
            if len(self.players) == 1:
                print(f"{self.players[0].name} wins!")
                self.running = False

    def play(self):
        while self.running:
            self.next_turn()