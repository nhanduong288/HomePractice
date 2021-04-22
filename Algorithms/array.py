'''
Array A consists of N integers.

Find a minimal by inclusion segment [L,R] (1 <= L <= R <= N) such, that among numbers A(L), A(L+1),...,A(R) there are exactly K distinct numbers

Segment [L,R] (1 <= L <= R <= N; L,R are integers) of length M = R - L + 1, satisfying the given property, is called the minimal by inclusion,
if there is no segment [X,Y] satisfying the property and less then M in length, such that
1 <= L <= X <= Y <= R <= N. 
Note that the segment [L,R] doesn't have to be the minimal in length among all segments, satisfying the given property

Output:
- Print a space-separated pair of integers L and R (1 <= L <= R <= N) such, that the segment
[L,R] is the answer to the problem.
- If the sought segment does not exist, print '-1 -1' without the quotation mark
'''

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

s = set(a)
if len(s) < k:
    print(-1,-1)
else:
    count = [0] * n
    i, j, diff = 0, 0, 0

    while (j < n):
        '''print('j: ' + str(j) + ' --> ' + 'a[j]: ' + str(a[j]) + ' --> ' + 'count[a[j]]: ' + str(count[a[j]]) + ' --> ' + 'pj: ' +
              str(count) + ' --> ' + 'diff: ' + str(diff))'''
        if count[a[j]] == 0:
            diff += 1
        count[a[j]] += 1
        if diff == k:
            break
        j += 1

    #print('-----------------------------------------------')

    while i < n:
        '''print('i: ' + str(i) + ' --> ' + 'a[i]: ' + str(a[i]) + ' --> ' + 'count[a[i]]: ' + str(count[a[i]]) + ' --> ' + 'pi: ' +
              str(count) + ' --> ' + 'diff: ' + str(diff))'''
        if count[a[i]] == 1:
            diff -= 1
        count[a[i]] -= 1
        if (diff < k):
            break
        i += 1

    print(i+1,j+1)
