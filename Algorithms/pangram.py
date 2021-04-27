'''
Source: Codeforces
'''

# length of the string
l = int(input())
# string
s = input()

s = s.lower()
d = {}

for letter in s:
    if letter not in d:
        d[letter] = 1

print(d)

if len(d) < 26:
    print('NO')
else:
    print('YES')
