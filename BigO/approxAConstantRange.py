''' ***
Xellos had to measure the intensity of an effect that slowly approached equilibrium.
To do so: choosing a sufficiently large number of consecutive data points that seems as 
    constant as possible and taking their average.

Given a sequence of N data points, there aren't any big indexumps 
    between consecutive data points 
    --> for each i < i < N, it's guaranteed that |A[i+1]| - A[i] <= 1
A range [L,R] of data points is said to be almost constant if the difference
    between the largest and the smallest value in that range is at most 1.
    Let M be the maximum and m the minimum value of A[i] for L < i <R.
    The range [L,R] is almost constant if M-m <= 1

Find the length of the longest constant range
'''
# the number of data points (2 <= N <= 100000)
n = int(input())
# N integers (1 <= A[i] <= 100000)
a = list(map(int, input().split()))

fre = [0] * (10**5 + 1)
diff = 0
index = 0
longest_range = 0

for i in range(n):
    if fre[a[i]] == 0:
        diff += 1
    fre[a[i]] += 1

    while index < n and diff > 2:
        if fre[a[index]] == 1:
            diff -= 1
        fre[a[index]] -= 1
        index += 1

    longest_range = max(longest_range, i - index + 1)

print(longest_range)
