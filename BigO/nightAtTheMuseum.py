'''
Embosser is a special devise that allows to "print" the text of a plastice tape.
Text is printed sequentially, character by character.
The device consists of a wheel with a lowercase English letters written in a circle, static pointer to the current letter and a button that print the chosen letter.
At one move it's allowed to rotate the alphabetic wheel one step clockwise or counterclockwise
Initially, static pointer points to letter 'a'

Our hero is afraid that some exhibits may become alive and start to attack him, so he wants to print the names as fast as possible. Help him, 
for the given string find the minimum number of rotations of the wheel required to print it

If there is one letter --> return 0 since there is no rotation needs to be done

​​If there are more letters:
There are 26 characters in the English alphabet
If 2 letters are more than 13 characters away from each other, count counterclockwise
'''

s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# we always have to start at a
s = 'a' + s
rotation = 0

for i in range(len(s)-1):
    if abs(alphabet.index(s[i]) - alphabet.index(s[i+1])) <= 13:
        rotation += abs(alphabet.index(s[i]) - alphabet.index(s[i+1]))
    else:
        rotation += 26 - abs(alphabet.index(s[i]) - alphabet.index(s[i+1]))
print(rotation)
