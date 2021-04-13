'''
There are n guilty people in a line
The i-th  of them holds a claw with length L[i].
The bell rings and every person kills some of peole IN FRONT of him.
All people kill others at THE SAME TIME.
Namely, the i-th person kills the j-th person if and only if j < i and j >= i - L[i]

Given lengths of the claws.
Find the total number of alive people after the bell rings.
'''
n = int(input())
a = list(map(int, input().split()))

dead_people = 0
# position of the last one killed
j = n - 1

#iterate from the back because people kill ones in front of them
for i in range(n-1, -1, -1):
    j = min(i,j)
    last_kill_pos = max(0, i-a[i])

    if j > last_kill_pos:
        dead_people += (j - last_kill_pos)
        j = last_kill_pos

print(n - dead_people)
