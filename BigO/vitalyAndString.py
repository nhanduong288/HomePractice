'''
2 strings S and T have the same length.
They consist of lowercase English letters, string S is lexicographically smaller than string T.

Find a string that is lexicographically larger than S and smaller than T.
That string should also consist of lowercase English letters and have length equal to S and T

Solutions: using ASCII table order
'''

s = input()
t = input()

new_string = ''
if len(s) == 1:
    if s == t:
        new_string = s
    else:
        new_string += chr(ord(s[0]) + 1)
else:
    for i in range(len(s)):
        if s[i] == t[i]:
            new_string += s[i]
        elif ord(s[i]) < ord(t[i]):
            new_string += s[i]
if ord(s[-1]) == ord(t[-1]):
    new_string = new_string[:len(new_string)-1] + chr(ord(s[-1]) + 1)

print(new_string)
