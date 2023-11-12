from Deck import create_deck

# Creating a Poker deck

deck = create_deck()

import random

# remove two cards from the deck

def draw(deck):
    if 2 > len(deck):
        print("Error: Empty deck")
        return None
    
    selected_elements = random.sample(deck, 2)
    
    for element in selected_elements:
        deck.remove(element)
    
    return selected_elements

