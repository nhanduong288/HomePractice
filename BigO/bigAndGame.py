'''
Bear Limak likes watching sports on TV. He is going to watch a game today.
The game lasts 9090 minutes and there are no breaks.
Each minute can be either interesting or boring.
If 15 consecutive minutes are boring then Limak immediately turns TV off.
There will be N interesting minutes T1, T2,..., Tn.

Calculate for how many minutes Limak will watch the game.

Steps:
- sort the list
- if the first integer is more than 15 --> he does not watch the game
- if there is only one integer:
    - if it is less than 15: total minutes watched = number + 15
    - if it is bigger than 15: total minutes watched = 15
- if an interger is bigger than the previous one by 15 --> total minutes watched = the previous one + 15
- if there is no integer is bigger than the previous one by 15 --> total minutes watched = the last integer
'''
# TODO: fix the last else statement

n = int(input())
arr = list(map(int, input().split()))
result = 0

arr.sort()
if n == 1:
    if arr[0] > 15:
        result = 15
    else:
        result = arr[0] + 15
else:
    if arr[0] > 15:
        result = 15
    else:
        for i in range(0,n-1):
            if arr[i+1] - arr[i] > 15:
                result = arr[i] + 15
                break
            else:
                if arr[i+1] + 15 <= 90:
                    result = arr[i+1] + 15
                else:
                    result = 90
print(result)
