'''
George has prepared M problems.
Problems are numbered from 1 to M
George estimates the i-th problem's complexity by integer B(i)

To make a round good, it needs to be N problems there.
At least one problem with complexity EXACTLY A1, EXACTLY A2,..., EXACTLY An

George can simplify any problem with complexity C to any positive integer complexity D (C >= D),
by changing limits of the input data

Find out the minimum number of problems in addition to the M to make a good round.
Note: George can come up with a new problem of any complexity
'''
# minimal number of problems in a good round and number of problems George's prepared
n, m = list(map(int, input().split()))
# the requirements for the complexity of the problems in a good round 
a = list(map(int, input().split()))
# the complexities of the problems prepared by George
b = list(map(int, input().split()))

# counter = satisfied complexites
counter = i = 0

# if b[j] > a[i] --> complexity can be used --> increase i, j, and count
# if b[j] < a[i] --> increase j to look for another complexity
for j in range(m):
    if i >= n:
        break

    if b[j] >= a[i]:
        counter += 1
        i += 1

print(n-counter)
