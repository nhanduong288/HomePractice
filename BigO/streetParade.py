'''
Each year, the parade's organisers decide on a fixed order for the decorated trucks.
Experience taught them to keep free a side street to be able to bring the trucks into order.
The side street is so narrow that no two cars can pass each other.
The love mobile that enters the side street LAST mus necessarily leave FIRST.

You are given the order in which the love mobiles arrive. 
Write a program that decides if the love mobiles can be brought into the order
    that the organisers want them to be.
'''

# number of love mobiles
n = int(input())
# arbitrary numbers indicate the order in which the trucks arrive in the approach street
order = list(map(int, input().split()))
# input end with a number 0


stack = []
result = []
index = 0

for i in range(n-1):
    if order[i] > order[i+1]:
        stack.append(order[i])
    else:
        result.append(order[i])

result.append(order[-1])

while len(stack) > 0:
    result.append(stack.pop())

if result == sorted(order):
    print('yes')
else:
    print('no')