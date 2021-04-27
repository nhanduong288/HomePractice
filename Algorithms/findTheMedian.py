'''
Source: Secret
'''

# number of numbers
n = int(input())
# list of numbers
numbers = list(map(int, input().split()))

numbers.sort()
print(numbers[int(len(numbers)/2)])
