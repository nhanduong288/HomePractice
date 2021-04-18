'''
Petya's parents went on a business trip for a whole year
He should water their favourite flower all year, each day, in the morning,
    in the afternoon and in the evening.
If he fulfulls the parents' task in the i-th month of the year, then the flower
    will grow by a[i] centimeters, and if he doesn't water the flower in the i-th
    month, then the flower won't grow this month. 
Petya also knows that try as he might, his parents won't believe that he has been
    watering the flower if it grows stricly less than by k centimeters.

Help Petya choose the minimum number of months when he will water the flower, given
    that the flower should grow no less than by k centimeters
'''

k = int(input())
# centimeters in months
centimeters = list(map(int, input().split()))

growth, count = 0, 0
# minimum number of months = water in the months that the flower grows the most
centimeters.sort(reverse=True)
print(centimeters)

if k == 0:
    count = 0
elif sum(centimeters) < k:
    count = -1
else:
    for i in range(len(centimeters)):
        if growth < k:
            count += 1
            growth += centimeters[i]

print(count)