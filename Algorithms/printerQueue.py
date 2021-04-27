'''
Source: UVA

'''
# number of test cases:
cases = int(input())

result = []

for i in range(cases):
    # number of jobs, position of your job
    # priorities of the jobs
    n, m = list(map(int, input().split()))
    p = list(map(int, input().split()))

    if p[m] == max(p):
        result.append(1)
    else:
        if p[m] <= min(p):
            result.append(len(p)-1)
        else:
            temp = p[m]
            p.sort(reverse=True)
            result.append(p.index(temp) + 1)

for num in result:
    print(num)
