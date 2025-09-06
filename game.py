from board import board
from property import Property
from player import Player
from dice import Dice
from cards import chance_deck, community_chest_deck, CardDeck

class Game:
    def __init__(self, players):
        self.players = players
        self.current_turn = 0
        self.board = board
        self.chance_deck = CardDeck(chance_deck.cards)
        self.community_chest_deck = CardDeck(community_chest_deck.cards)

    def next_turn(self):
        player = self.players[self.current_turn]

        print(f"\n--- {player.name}'s turn ---")
        total, (die1, die2) = Dice.roll()
        print(f"{player.name} rolled {die1} + {die2} = {total}")

        if player.in_jail:
            freed = player.attempt_jail_exit(die1, die2)
            if not freed:
                print(f"{player.name} remains in Jail.")
                self.end_turn()
                return

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

        elif tile == "Chance":
            card = self.chance_deck.draw()
            card.apply(player, self)
        elif tile == "Community Chest":
            card = self.community_chest_deck.draw()
            card.apply(player, self)

        elif tile == "Go to Jail":
            player.go_to_jail()

        else:
            print(f"{player.name} landed on {tile}")

        self.end_turn()

    def end_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)


if __name__ == "__main__":
    p1 = Player("Alice")
    p2 = Player("Bob")

    game = Game([p1, p2])

    for _ in range(15):
        game.next_turn()