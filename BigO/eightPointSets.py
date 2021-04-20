'''
Gerald thinks that any decent eight point set must consist of all pairwise
    intersections of 3 distinct integer vertical straight lines and 3 distinct
    integer horizontal straight lines, except for THE AVERAGE of these nine points.
In other words, there must be 3 integers x1, x2, x3 and 3 more integers y1, y2, y3,
    such that x1 < x2 < x3, y1 < y2 < y3 and the 8 point set consists of all points
    (x[i],y[i])(1 <= i, j <= 3) except for point (x2, y2)

You have a set of eight points. Find out if Gerald can use this set.
'''

points = []
for i in range(8):
    points.append(list(map(int, input().split())))\

xs = []
ys = []

for i in range(len(points)):
    if points[i][0] not in xs:
        xs.append(points[i][0])
    if points[i][1] not in ys:
        ys.append(points[i][1])

if len(xs) != 3 or len(ys) != 3:
    print('ugly')
    exit(0)

xs.sort()
ys.sort()

for m in range(3):
    for n in range(3):
        if m == n == 1:
            continue
        if [xs[m],ys[n]] in points:
            continue
        else:
            print('ugly')
            exit(0)

print('respectable')