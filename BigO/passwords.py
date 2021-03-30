'''
Vanya uses n distince passwords for sites at all.
Vanya will enter passwords in order of NON-DECREASING their lengths,
and he will enter passwords of same length in ARBITRARY order.

Entering any passwords takes 1 SECOND for Vanya. 
If Vanya enters wrong password k times, next try is in 5 SECONDS
Vanya makes each try IMMEDIATELY after that

Determine how many seconds in BEST and WORST case will Vanya need
'''

n, k = int(input())
passwords = []
for i in range(n):
    passwords.append(input())

flag = True
result = []

# check if all the passwords have the same length
for i in range(n-1):
    if len(passwords[i]) != len(passwords[i+1]):
        flag = False

# if passwords have the same length, best case is first try, worst is last try
if flag:
    
# if passwords don't have the same length

