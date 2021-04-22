'''
Given is an ordered deck of N cards numbered 1 to N with card 1 at the top and card N
    at the bottom.
The following operation is performed as long as there are at least 2 cards in the deck:
    Throw away the top card and move the card that is now on the top of the deck to the 
    bottom of the deck.
Your task is to find the sequence of discarded cards and the last, remaining card.
'''

decks = []
d = int(input())
while d != 0:
    decks.append(d)
    d = int(input())

for cards in decks:
    discarded = []
    deck = []

    for i in range(cards):
        deck.append(i+1)

    while len(deck) > 1:
        discarded.append(deck[0])
        deck.append(deck[1])
        deck = deck[2:]

    if len(discarded) >= 1:
        print('Discarded cards:', ', '.join(str(card) for card in discarded))
    else:
        print('Discarded cards:')

    print('Remaining card: ' + str(deck[0]))
