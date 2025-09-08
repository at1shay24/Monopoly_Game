from board import board
from property import Property
from player import Player
from dice import Dice
from cards import chance_deck, community_chest_deck


class Game:
    def __init__(self, players):
        self.players = players
        self.current_turn = 0
        self.board = board

    def next_turn(self):
        player = self.players[self.current_turn]
        print(f"\n--- {player.name}'s Turn ---")

        if player.in_jail:
            total, (die1, die2) = Dice.roll()
            print(f"{player.name} rolled {die1} + {die2} = {total} (trying to leave Jail)")
            freed = player.attempt_jail_exit(die1, die2)
            if not freed:
                print(f"{player.name} remains in Jail.")
                self.current_turn = (self.current_turn + 1) % len(self.players)
                return
            else:
                player.move(total)

        else:
            total, (die1, die2) = Dice.roll()
            print(f"{player.name} rolled {die1} + {die2} = {total}")
            player.move(total)

        tile = self.board.get_space(player.position)

        if isinstance(tile, Property):
            if not tile.is_owned():
                bought = tile.buy(player)
                if bought:
                    print(f"{player.name} bought {tile.name} for ${tile.price}")
            else:
                if tile.owner != player:
                    tile.charge_rent(player)
                else:
                    if not tile.hotel:
                        choice = input(f"{player.name}, do you want to build on {tile.name}? (house/hotel/none): ").strip().lower()
                        if choice == "house":
                            player.build_house(tile)
                        elif choice == "hotel":
                            player.build_hotel(tile)

        elif isinstance(tile, str):
            print(f"{player.name} landed on {tile}")

            if tile == "Go To Jail":
                player.go_to_jail()

            elif tile == "Chance":
                card = chance_deck.draw()
                card.apply(player, self)

            elif tile == "Community Chest":
                card = community_chest_deck.draw()
                card.apply(player, self)

            elif tile == "Income Tax":
                tax = min(200, int(player.money * 0.1))
                player.pay(tax)
                print(f"{player.name} paid ${tax} in Income Tax")

            elif tile == "Luxury Tax":
                player.pay(100)
                print(f"{player.name} paid $100 in Luxury Tax")

        self.current_turn = (self.current_turn + 1) % len(self.players)


if __name__ == "__main__":
    p1 = Player("Alice")
    p2 = Player("Bob")

    game = Game([p1, p2])

    for _ in range(15):
        game.next_turn()