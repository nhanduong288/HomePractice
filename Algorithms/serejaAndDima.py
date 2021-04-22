'''
Seraja and Dima play a game.
The players have n cards in a row.
Each card contains a number, all numbers on the cars are distinct.
The players take turns, Sereja moves first.
Each turn, a player can take one card: either leftmost or rightmost one.
Game ends when there is no more cards.
The player who has the maximum sum of numbers on his cards by the end of the game, wins.

Sereja and Dima are being greedy. Each of them chooses the card with the larger number during his move.

Calculate the final score.
'''

# number of cards on the table
n = int(input())
# numers on the cards (distinct numbers)
cards = list(map(int, input().split()))

# Sereja goes first --> scores[0] --> Dima: scores[1]
scores = [0,0]
# To mark the player
player = 0
i, j = 0, n-1

while i <= j:
    if cards[i] > cards[j]:
        scores[player] += cards[i]
        i += 1
    else:
        scores[player] += cards[j]
        j -= 1
    player = 1 - player

print(scores[0], scores[1])