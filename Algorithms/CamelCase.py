'''
Source: Big-O
'''

# input string
s = input()

result = 1

for letter in s:
    if letter.isupper():
        result += 1

print(result)
