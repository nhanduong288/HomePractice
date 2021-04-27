'''
Find the smallest positive integer that does not occur in a given array
'''

A = list(map(int, input().split()))

result = 0

if max(A) < 0:
    result = 1
else:
    for i in range(1, max(A)):
        if i not in A:
            result = i
            break
        else:
            result = max(A) + 1

print(result)
