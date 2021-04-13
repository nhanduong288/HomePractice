'''
Alice and Bob start a new game.
They have placed n chocolate bars in a line. 
Alice starts to eat chocolate bars from left to right, and Bob from right to left.
For each chocolate bar the time, needed for the player to consume it, is known (same eating speed).
When the player consumes a chocolate bar, he immediately starts with another.
It is not allowed to eat 2 bars at the same time, to leave the bar unfinished and to make pauses.
If both players start to eat the same bar simutaneously, Bob leaves it to Alice as a true gentleman.

How many bars each of the players will consume?

OUTPUT: a and b where a is the amount of bars consumed by Alice, and b is by Bob
'''
# the amount of bars on the table
n = int(input())
# time (in seconds) needed to consume the bar
t = list(map(int, input().split()))

i, j = 0, n-1
alice = bob = 0

while i <= j:
    if alice + t[i] <= bob + t[j]:
        alice += t[i]
        i += 1
    else:
        bob += t[j]
        j -= 1

print(i, n-i)