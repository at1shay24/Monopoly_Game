from board import board
from property import Property
from player import Player
from dice import Dice

class Game:
    def __init__(self, players):
        self.players = players
        self.current_turn = 0
        self.board = board

    def next_turn(self):
        player = self.players[self.current_turn]

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
                tile.charge_rent(player)
                print(f"{player.name} paid ${tile.rent} rent to {tile.owner.name}")
        elif isinstance(tile, str):
            print(f"{player.name} landed on {tile}")

        self.current_turn = (self.current_turn + 1) % len(self.players)


if __name__ == "__main__":
    # Example test game
    p1 = Player("Alice")
    p2 = Player("Bob")

    game = Game([p1, p2])

    for _ in range(10):
        game.next_turn()