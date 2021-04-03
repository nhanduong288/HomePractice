n, k = map(int, input().split())
cnt = [0] * 101

for _ in range(n):
    s = input()
    cnt[len(s)] += 1

password = input()
best_time = worst_time = 0

for i in range(len(password)):
    best_time += cnt[i]

worst_time = best_time + cnt[len(password)] - 1

best_time += (best_time // k) * 5
worst_time += (worst_time // k) * 5

print(best_time + 1, worst_time + 1, sep=' ')