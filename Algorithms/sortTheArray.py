'''
A programmer likes arrays a lot.
You are given an array a consisting of n DISTINCT integers.

The size of a is too small and you want a bigger array.
You will be given one only if you can answer one question:
    Is it possible to sort the array a (in increasing order) by reversing 
    EXACTLY ONE segment of a?
'''

# size of arrayA
n = int(input())
# the array of distinct numbers
arr = list(map(int, input().split()))

sorted_arr = sorted(arr)
# leftmost and rightmost index of the different segment
l, r = 0, 0
# different segment
segment = []

for i in range(n):
    if arr[i] != sorted_arr[i]:
        l = i
        break

for m in range(n-1, -1, -1):
    if arr[m] != sorted_arr[m]:
        r = m
        break

segment = arr[l:r+1]
segment.reverse()

if arr[:l] + segment + arr[r+1:] == sorted_arr:
    print('yes')
    print(l+1, r+1)
else:
    print('no')
