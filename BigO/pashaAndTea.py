'''
Pasha invited his friends to a tea party.
He has a large teapot with the capacity of w mililiters and 2n tea cups,
    each cup is for one of Pasha's friends.
The i-th cup can hold at most a[i] mililiters of water

Pasha's friends are exactly n boys and n girls.
To please everyone, Pasha decided to pour the water for the tea as follow:
    - Pasha boil the teapot exactly once by pouring there ar most 2 mililiters of water.
    - Pasha pours the same amount of water to each girl.
    - Pasha pours the same amount of water to each boy.
    - If each girl gets x mililiters of water, then each boy gets 2x mililiters of water.

Help Pasha determine the optimum DISTRIBUTION OF CUPS between his friends.
Input: the maximum total amount of water in mililiters that Pasha can pour to his friends
    without violating the coniditions.
'''

# number of Pasha's friends that are boys (= girls), capacity of teapot in mimiliters
n, w = list(map(int, input().split()))
# capacities of tea cups in mililiters
cups = list(map(int, input().split()))

# to be able to pour out the maximum --> give the boys first
# also make sure to use the bigger cups first
cups.sort()

# if the amount of tea for the girls is x, each girl is m --> m <= x
# then the amount for boys is y, each boy is 2m --> 2m <= y --> m <= y/2
# --> biggest value for m is min(x, y/2)

# The maximum amount of tea to be prepared: mn + 2mn = 3mn

m = min(cups[0], cups[n]/2)

# 
print(min(3*m*n, w))