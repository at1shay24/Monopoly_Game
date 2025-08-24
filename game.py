from player import Player
from property import Property
from board import Board
from dice import Dice
class Game:
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.current_turn = 0

    def next_turn(self):
        player = self.players[self.current_turn]
        steps, dice_values = Dice.roll()
        print(f"{player.name} rolled {dice_values} → moving {steps} steps")
        
        player.move(steps)
        tile = self.board.spaces[player.position]

        if isinstance(tile, Property):
            if not tile.is_owned():
                bought = tile.buy(player)
                if bought:
                    print(f"{player.name} bought {tile.name}")
            else:
                tile.charge_rent(player)
                print(f"{player.name} paid {tile.rent} rent to {tile.owner.name}")

        self.current_turn = (self.current_turn + 1) % len(self.players)

player1 = Player("Alice")
player2 = Player("Bob")
board = Board()

game = Game([player1, player2], board)

for _ in range(4):
    game.next_turn()
    print(player1.name, player1.money, [p.name for p in player1.properties])
    print(player2.name, player2.money, [p.name for p in player2.properties])