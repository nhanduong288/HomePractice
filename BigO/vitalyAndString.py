'''
2 strings S and T have the same length.
They consist of lowercase English letters, string S is lexicographically smaller than string T.

Find a string that is lexicographically larger than S and smaller than T.
That string should also consist of lowercase English letters and have length equal to S and T

Solutions: using ASCII table order
'''
# TODO: do something with z

s = input()
t = input()

new_string = ''

for i in range(len(s)):
    if s[i] == 'z':
        new_string += 'a'
    else:
        new_string += s[i]
        
if new_string < t[:-1]:  
    new_string = new_string + chr(ord(s[-1]) + 1) 
else:
    if ord(t[-1]) - ord(s[-1]) <= 1:
        new_string = 'No such string'
    else:
        new_string = new_string + chr(ord(s[-1]) + 1)

print(new_string)
