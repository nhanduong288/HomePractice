'''
According to rules of the Berland fashion, 
a jacket should be fastened by ALL THE BUTTONS EXCEPT ONLY ONE, 
but not necessarily it should be the last one

1 = fastened, 0 = not fastened

If there is one button, it has to be fastened

If there are more buttons, cannot be more than 1 '0'
'''

n = int(input())
arr = list(map(int, input().split()))

if n == 1 and arr[0] == 0:
    print('NO')
elif n == 1 and arr[0] == 1:
    print('YES')
else:
    if arr.count(0) != 1:
        print('NO')
    else:
        print('YES')

