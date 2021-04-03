'''
Vanya uses n distinct passwords for sites at all.
Vanya will enter passwords in order of NON-DECREASING their lengths,
and he will enter passwords of same length in ARBITRARY order.

Entering any passwords takes 1 SECOND for Vanya. 
If Vanya enters wrong password k times, next try is in 5 SECONDS
Vanya makes each try IMMEDIATELY after that

Determine how many seconds in BEST and WORST case will Vanya need
'''

n, k = list(map(int, input().split()))
passwords = []
for i in range(n):
    passwords.append(input())
correct_password = input()

sameLength = True
result = []
wrong_passwords = []
worst = 1
best = 0
longer_passord_counter = 0

# we don't care about passwords that are longer than the correct password
for password in passwords:
    if len(password) > len(correct_password):
        longer_passord_counter += 1

# passwords that are shorter then correct password
for password in passwords:
    if len(password) < len(correct_password):
        wrong_passwords.append(password)


# check if all the passwords have the same length
for i in range(n-1):
    if len(passwords[i]) != len(passwords[i+1]):
        sameLength = False

# if passwords have the same length, best case is first try, worst is last try
if sameLength:
    best = 1
    # -1 because last one is correct password
    worst = int((n - 1)/k)*5 + n
    result.append(best)
    result.append(worst)

# if passwords don't have the same length
# best case is the first try after trying all shorter passwords
# worst case if last try
else:
    best = int(len(wrong_passwords)/k)*5 + len(wrong_passwords) + 1
    # -1 because last one is correct password
    worst = int((n-longer_passord_counter - 1)/k)*5 + n-longer_passord_counter
    result.append(best)
    result.append(worst)

print(result[0], result[1])
