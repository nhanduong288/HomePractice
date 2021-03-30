n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

min_num = arr[0][0]
max_num = arr[0][1]

for i in range(1, n):
    if arr[i][0] < min_num:
        min_num = arr[i][0]
    if arr[i][1] > max_num:
        max_num = arr[i][1]

if [min_num,max_num] in arr:
    print(arr.index([min_num,max_num]) + 1)
else:
    print(-1)
