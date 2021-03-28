'''
A and B are 2 arrays consisting of integers, sorted in non-decreasing order.

Check whether it is possible to choose K numbers in array A and choose M numbers in array B
so that any number chosen in the first array is strictly less than any number chosen in the second array

Inputs:
- n1, n2: size pf arrays A and B
- k, m: integer represent the number of elements taken from A and B
- arrA: arrayA
- arrB: arrayB
'''

n1 = list(map(int, input().split()))
k = list(map(int, input().split()))
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

result = ''

# if every number in B is bigger than every number in A, it's a YES
if min(arrayB) > max(arrayA):
    result = 'YES'

print(result)