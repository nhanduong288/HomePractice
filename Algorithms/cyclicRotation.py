'''
Codility practice

'''
# array A
A = list(map(int, input().split()))
# number of rotations K
K = int(input())

for i in range(K):
    A = [A[-1]] + A[:len(A)-1]

print(A)
