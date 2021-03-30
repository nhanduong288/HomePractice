'''
2 strings S and T have the same length.
They consist of lowercase English new_string[i]s, string S is lexicographically smaller than string T.

Find a string that is lexicographically larger than S and smaller than T.
That string should also consist of lowercase English new_string[i]s and have length equal to S and T

Solutions: using ASCII table order
'''

s = input()
t = input()

new_string = list(s)

for i in range(len(new_string)-1,-1,-1):
    if new_string[i] == 'z':
        new_string[i] = 'a'
    else:
        new_string[i] = chr(ord(new_string[i]) + 1)
        break

new_string = ''.join(new_string)

if new_string == t:
    print('No such string')
else:
    print(new_string)