'''
Codility practice

Find the maximal count of consecutive zeros that is surrounded at both ends
    in the binary representation of N
'''

n = int(input())

binary = '{0:b}'.format(n)
print(binary)

if binary.count('0') == 0 or binary.count('1') <= 1:
    print(0)
else:
    i, j = 0, 1
    count, max_seq = 0, 1
    while j < len(binary):
        if binary[j] != '1':
            count += 1
            j += 1
        else:
            i = j
            j = i + 1
            count = 0
        max_seq = max(count, max_seq)
    print(max_seq)
