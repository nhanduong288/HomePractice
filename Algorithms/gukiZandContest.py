'''
Professor GukiZ decided to prepare a new programming contest.

In total, n students will attend, and before the start, every one of them has
    some positive integer rating.
Students are indexed from 1 to n. 
Let's denote the rating of i-th student as a[i].
At the end, every student will end up with some positive integer position.

GukiZ thinks that each student will take place equal to
    1 + number of students with strictly higher rating then his or her.
In particular, if student A has rating strictly lower then student B,
    A will get the strictly better position than B, and if two students have
    equal ratings, they will share the same position.

Help GukiZ and determine the position after the end of the contest.
'''

# number of students
n = int(input())
# ratings
a = list(map(int, input().split()))

sorted_a = sorted(a, reverse=True)
ratings = {}
ratings[sorted_a[0]] = 1

for i in range(1, n):
    if sorted_a[i] != sorted_a[i-1]:
        ratings[sorted_a[i]] = len(sorted_a[:i]) + 1

for num in a:
    print(ratings[num], end=' ')