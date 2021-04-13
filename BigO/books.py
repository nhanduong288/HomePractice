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
a = list(map(int, input().split()))

index = 0
read_books = max_books = 0

for i in range(n):
    while t < a[i]:
        t += a[index]
        index += 1
        read_books -= 1
    
    t -= a[i]
    read_books += 1
    max_books = max(max_books, read_books)

print(max_books)