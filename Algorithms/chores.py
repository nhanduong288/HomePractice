'''
Petya and Vasya are brothers.
Today their parents left home and assigned them n chores.
Each chore is characterized by a single paremeter - its complexity.
The complexity of the i-th chore = h[i]

As Petya is older, he wants to take the chores with complexity larger than some value
    x(h[i]>x) to leave to Vasya the chores with complexity less than or equal to x(h[i]<x)
The brothers have decided that Petya will do exactly a chores and Vasya will do exactly
    b chores (a + b = n)

In how many ways can they choose an integer x so that Petya got exactly a chores
    and Vasya got exactly b chores?
'''

# number of chores, number of chores for Petya, number of chores for Vasya
n, a, b = list(map(int, input().split()))
# complexities of the chores
h = list(map(int, input().split()))

h.sort()

# Petya takes the a biggest complexities
Petya = h[n-a:]
Vasya = h[:n-a]

if Petya[0] <= Vasya[-1]:
    print(0)
else:
    print(Petya[0] - Vasya[-1])