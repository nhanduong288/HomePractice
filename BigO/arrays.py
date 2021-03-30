'''
A and B are 2 arrays consisting of integers, sorted in non-decreasing order.

Check whether it is possible to choose K numbers in array A and choose M numbers in array B
so that any number chosen in the first array is strictly less than any number chosen in the second array

Inputs:
- n1: size pf arrays A and B
- k: integer represent the number of elements taken from A and B
- arrA: arrayA
- arrB: arrayB
'''
#TODO: to compare arrayA[:k[0]] with slices of arrayB with k[1] number of integers from arrayB

n = list(map(int, input().split()))
k = list(map(int, input().split()))
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

result = 'YES'

index = 0

# Because the numbers are in non-decreasing order:
# If the last number of arrayA[:k[0]] < the first number of arrayB[len(arrayB)-k[1]:len(arrayB)]
# everything is smaller 
if arrayA[:k[0]][-1] < arrayB[n[1]-k[1]:n[1]][0]:
    result = 'YES'
else:
    result = 'NO'

print(result)
