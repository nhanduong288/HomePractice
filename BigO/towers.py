'''
Little Vasya has received a young builder's kit.
The kit consists of several wooden bars, the length of all of them are known.
The bars can be put one on top of the other if their lengths are the same.

Vasya wants to construct the MINIMAL number of towers from the bars.
Help Vasya to use the bars in the best way possible

OUPUT: 2 numbers -  the height of the largest tower and their total number. Remember that
    Vasya should use all the bars.
'''

# number of bars
n = int(input())
# lengths of the bars
l = list(map(int, input().split()))

largest_tower_height = 0
towers = {}

for m in range(n):
    if l[m] not in towers:
        towers[l[m]] = 0

for key, value in towers.items():
    if l.count(key) > largest_tower_height:
        largest_tower_height = l.count(key)

print(largest_tower_height, len(towers))