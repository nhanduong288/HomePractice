'''
Each year, the parade's organisers decide on a fixed trucks for the decorated trucks.
Experience taught them to keep free a side street to be able to bring the trucks into trucks.
The side street is so narrow that no two cars can pass each other.
The love mobile that enters the side street LAST mus necessarily leave FIRST.

You are given the trucks in which the love mobiles arrive. 
Write a program that decides if the love mobiles can be brought into the trucks
    that the organisers want them to be.
'''

# number of love mobiles
n = int(input())
# arbitrary numbers indicate the trucks in which the trucks arrive in the approach street
trucks = []
truck = list(map(int, input().split()))
while truck[0] != 0:
    trucks.append(truck)
    truck = list(map(int, input().split()))
# input end with a number 0


stack = []
result = []
index = 0

for i in range(n-2):
    if trucks[i] > trucks[i+1]:
        stack.append(trucks[i])
    else:
        result.append(trucks[i])

result.append(trucks[-1])

while len(stack) > 0:
    result.append(stack.pop())

if result == sorted(trucks):
    print('yes')
else:
    print('no')
