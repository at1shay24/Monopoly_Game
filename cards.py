import random
class Card:
    def __init__(self, description, effect):
        self.description = description
        self.effect = effect

    def apply(self, player, game):
        print(f"Card drawn: {self.description}")
        self.effect(player, game)

class CardDeck:
    def __init__(self, cards):
        self.cards = cards
        random.shuffle(self.cards)

    def draw(self):
        card = self.cards.pop(0)
        self.cards.append(card)
        return card

# ===== CHANCE CARDS ===== #
chance_cards = [
    Card("Advance to Go (Collect $200)", lambda p, g: (setattr(p, "position", 0), p.receive(200))),
    Card("Go to Jail", lambda p, g: (setattr(p, "position", 10), setattr(p, "in_jail", True))),
    Card("Pay poor tax of $15", lambda p, g: p.pay(15)),
    Card("Bank pays you dividend of $50", lambda p, g: p.receive(50)),
    Card("Advance to Rajouri Garden", lambda p, g: setattr(p, "position", 21)),
    Card("Advance to Kirti Nagar", lambda p, g: setattr(p, "position", 26)),
    Card("Go back 3 spaces", lambda p, g: setattr(p, "position", (p.position - 3) % 40)),
    Card("Your building loan matures, collect $150", lambda p, g: p.receive(150)),
    Card("Pay school fees of $50", lambda p, g: p.pay(50)),
    Card("Advance to West Delhi Mall", lambda p, g: setattr(p, "position", 37)),
    Card("Advance to nearest Utility", lambda p, g: setattr(p, "position", 12)),
    Card("Advance to nearest Railroad", lambda p, g: setattr(p, "position", 5)),
    Card("Take a trip to Tilak Nagar", lambda p, g: setattr(p, "position", 24)),
    Card("Pay poor tax of $100", lambda p, g: p.pay(100)),
    Card("You have been elected Chairman, collect $50", lambda p, g: p.receive(50)),
    Card("Speeding fine $15", lambda p, g: p.pay(15))
]

# ===== COMMUNITY CHEST CARDS ===== #
community_chest_cards = [
    Card("Doctor's fees – Pay $50", lambda p, g: p.pay(50)),
    Card("From sale of stock you get $45", lambda p, g: p.receive(45)),
    Card("Go to Jail", lambda p, g: (setattr(p, "position", 10), setattr(p, "in_jail", True))),
    Card("You inherit $100", lambda p, g: p.receive(100)),
    Card("Life insurance matures, collect $100", lambda p, g: p.receive(100)),
    Card("Pay hospital fees $100", lambda p, g: p.pay(100)),
    Card("Receive $25 consultancy fee", lambda p, g: p.receive(25)),
    Card("You won a beauty contest, collect $10", lambda p, g: p.receive(10)),
    Card("Bank error in your favor, collect $200", lambda p, g: p.receive(200)),
    Card("Pay school fees $50", lambda p, g: p.pay(50)),
    Card("You are assessed for street repairs, pay $40", lambda p, g: p.pay(40)),
    Card("Receive $50 for services", lambda p, g: p.receive(50)),
    Card("Holiday fund matures, collect $100", lambda p, g: p.receive(100)),
    Card("Pay poor tax $15", lambda p, g: p.pay(15)),
    Card("Receive $20 for winning second prize", lambda p, g: p.receive(20)),
    Card("Go back 3 spaces", lambda p, g: setattr(p, "position", (p.position - 3) % 40))
]

chance_deck = CardDeck(chance_cards)
community_chest_deck = CardDeck(community_chest_cards)