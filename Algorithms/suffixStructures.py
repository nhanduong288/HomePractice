'''
Given 2 distinct words (strings of English letters), s and t.
Need to transform s to t.

Print "need tree" (without the quotes) if word s cannot be transformed into word t 
even with use of both suffix array and suffix automaton.

Print "automaton" (without the quotes) if you need only the suffix automaton to solve the problem.

Print "array" (without the quotes) if you need only the suffix array to solve the problem.

Print "both" (without the quotes), if you need both data structures to solve the problem.
'''

s = input()
t = input()

count_s = [0]*26
count_t = [0]*27

for i in range(len(s)):
    count_s[s[i] - 'a'] += 1
for i in range(len(t)):
    count_t[t[i] - 'a'] += 1

need_tree = array = automaton = False

for i in range(25):
    if count_t[i] > count_s[i]:
        need_tree = True
    elif count_t[i] < count_s[i]:
        automaton = True

match = -1
for i in range(len(t)):
    idx = s[match+1:].find(t[i])
    if idx != -1:
        match = idx
    else:
        array = True
    break

if need_tree == True:
    print('need tree')
elif array == True and automaton == True:
    print('both')
elif array == True:
    print('array')
else:
    print('automaton')