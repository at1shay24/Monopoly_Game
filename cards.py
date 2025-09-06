import random
class Card:
    def __init__(self, description, effect, is_get_out_of_jail=False):
        self.description = description
        self.effect = effect
        self.is_get_out_of_jail = is_get_out_of_jail  
    def apply(self, player, game):
        print(f"Card drawn: {self.description}")
        if self.is_get_out_of_jail:
    
            player.get_out_of_jail_cards.append(self)
        else:
            self.effect(player, game)

class CardDeck:
    def __init__(self, cards):
        self.cards = cards
        random.shuffle(self.cards)

    def draw(self):
        card = self.cards.pop(0)
        self.cards.append(card)  
        return card

chance_cards = [
    Card("Advance to Go (Collect $200)", lambda p, g: (setattr(p, "position", 0), p.receive(200))),
    Card("Go to Jail", lambda p, g: (setattr(p, "position", 10), setattr(p, "in_jail", True))),
    Card("Pay poor tax of $15", lambda p, g: p.pay(15)),
    Card("Bank pays you dividend of $50", lambda p, g: p.receive(50)),
    Card("Get Out of Jail Free", lambda p, g: None, is_get_out_of_jail=True),
]
community_chest_cards = [
    Card("Doctor's fees – Pay $50", lambda p, g: p.pay(50)),
    Card("From sale of stock you get $45", lambda p, g: p.receive(45)),
    Card("Go to Jail", lambda p, g: (setattr(p, "position", 10), setattr(p, "in_jail", True))),
    Card("You inherit $100", lambda p, g: p.receive(100)),
    Card("Get Out of Jail Free", lambda p, g: None, is_get_out_of_jail=True),
]