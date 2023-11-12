from Draw import draw
from Add_players import players
from Deck import create_deck

deck = create_deck()
n = 4
num_players = players(n)

def fill_player_hands(num_players, deck):
    for player, hand in num_players.items():
        draw_cards = draw(deck)
        if draw_cards is not None:
            hand.extend(draw_cards)

