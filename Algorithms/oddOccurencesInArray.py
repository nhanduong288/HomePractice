'''
Codility practice

Print out the element that does not have a pair
'''
# array A
A = list(map(int, input().split()))

result = 0

# using XOR operation
for number in A:
    result ^= number
    print(result)
