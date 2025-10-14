from dice import Dice
from player import Player
from property import Property
from board import board
from cards import chance_deck, community_chest_deck

class Game:
    def __init__(self, players):
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
            if space == "Chance":
                card = chance_deck.draw()
                card.apply(player, self)
            elif space == "Community Chest":
                card = community_chest_deck.draw()
                card.apply(player, self)
            elif space == "Go":
                player.receive(200)
                print(f"{player.name} landed on Go and collected $200!")
            elif space == "Income Tax":
                player.pay(200)
                print(f"{player.name} paid $200 income tax.")
            elif space == "Luxury Tax":
                player.pay(75)
                print(f"{player.name} paid $75 luxury tax.")
            elif space == "Jail":
                print(f"{player.name} is just visiting Jail.")
            elif space == "Go To Jail":
                player.go_to_jail()
            elif space == "Free Parking":
                print(f"{player.name} landed on Free Parking. Nothing happens.")

        self.check_bankruptcy(player)
        self.next_player()

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def check_bankruptcy(self, player):
        if player.money < 0:
            print(f"{player.name} is bankrupt!")
            self