'''
Valera's got T free minutes to read.
He took N books and estimated the time he needs to read it.
Books are numbered from 1 to N.
Valera needs A(i) minutes to read i-th book

Valera chooses an ARBITRARY book with number i and read the books one by one.
He reads each book to the end --> he doesn't start the book if he doesn't have enough time to finish it.

Print the maximum number of books he can read
'''
# number of books and the number of free minutes
n, t = list(map(int, input().split()))
# number of minutes Valera needs to finish the books
A = list(map(int, input().split()))

count = [0]*20
i, j, diff = 0,0,0

while j < n:
    if count[A[j]] == 0: 
        diff += 1
    count[A[i]] += 1
    if diff == k:
        break
    j += 1

while i < n:
    if count[A[i]] == 1:
        diff -= 1
    count[A[i]] -= 1
    if diff < k:
        i = i - 1
        break

print(j+1, i+1)