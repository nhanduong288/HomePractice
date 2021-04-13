# find 2 numbers in a sorted array that sum to a target
def twoSum(arr, tar):
    left = 0
    right = len(arr)-1
    
    while left < right:
        if arr[left] + arr[right] == tar:
            return [arr[left], arr[right]]
        elif arr[left] + arr[right] < tar:
            left += 1
        elif arr[left] + arr[right] > tar:
            right -= 1
    return [-1,-1]

#print(twoSum([-1,1,2,3,5], 5))

# find 3 numbers in a sorted array that sum to a target
def threeSum(arr, tar):
    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            if arr[i] + arr[left] + arr[right] == tar:
                return [arr[i], arr[left], arr[right]]
            elif arr[i] + arr[left] + arr[right] <  tar:
                left += 1
            elif arr[i] + arr[left] + arr[right] > tar:
                right -= 1
    return [-1,-1,-1]

#print(threeSum([1,2,4,5,12], 19))

# square each value in a sorted array and return the ouput in sorted order
def squareArray(arr):
    left, right = 0, len(arr)-1
    # going from the bottom because the array is sorted
    index = len(arr)-1
    final = [x for x in arr]

    while index >= 0:
        print('index: ' + str(index) + ' --> ' + 'left: ' + str(left)  + ' ' + 'right: ' + str(right) + ' --> ' + 'final: ' + str(final))
        
        if abs(arr[left]) >= abs(arr[right]):
            final[index] = arr[left]**2
            left += 1
        else:
            final[index] = arr[right]**2
            right -=1

        index -= 1
    return final
print(squareArray([-5,-1,2,3]))