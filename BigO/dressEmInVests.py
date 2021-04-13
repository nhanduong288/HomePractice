'''
Two-dimensional has regular army of N people.
Each soldier registered himself and indicated the desired size of the bullet vest: 
    the i-th soldier indicated size A[i]
The command staff assumes that the soldiers are comfortable in any vests 
    with sizes from Ai - X to Ai - Y (X,Y > 0)

The two-dimensional kingdom has M vests at its disposal, the j-th vest's size equla B[j]

Task: equip with vests as many soldiers as possible, each vest can only be used once.
The i-th soldier can put on the j-th vest, if A[i] - X <= B[j] <= A[i] + Y

'''

# number of soldiers, number of vests, and 2 numbers that specify the soldiers' unpretentiousness
n, m, x, y = list(map(int, input().split()))
# desired sizes of vests
a = list(map(int, input().split()))
# sizes of available vests
b = list(map(int, input().split()))

vests = []
i = j = 0

while i < n and j < m:
    if a[i] - x <= b[j] <= a[i] + y:
        vests.append((i+1, j+1))
        i += 1
        j += 1
    # if the vest is too big for soldier i, find someone bigger to fit in
    elif a[i] - x > b[j]:
        j += 1
    # if the vest is too small for soldier i, find another bigger vest
    elif a[i] + y < b[j]:
        i += 1

print(len(vests))
for vest in vests:
    print(vest[0], vest[1])