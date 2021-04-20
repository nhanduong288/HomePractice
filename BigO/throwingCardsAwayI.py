'''
Given is an ordered deck of N cards numbered 1 to N with card 1 at the top and card N
    at the bottom.
The following operation is performed as long as there are at least 2 cards in the deck:
    Throw away the top card and move the card that is now on the top of the deck to the 
    bottom of the deck.
Your task is to find the sequence of discarded cards and the last, remaining card.
'''
import queue

decks = []
deck = int(input())
while deck != 0:
    decks.append(deck)
    deck = int(input())

discarded = []
remained = []

for num in decks:
    q = queue.Queue()
    for i in range(num):
        q.put(i+1)

    index = 0
    while index < num:
