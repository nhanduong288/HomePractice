'''
Source: Codeforces
'''
k, n, w = list(map(int, input().split()))

money_needed = 0

for i in range(w):
    money_needed += k * (i+1)

if money_needed - n <= 0:
    print(0)
else:
    print(money_needed - n)
