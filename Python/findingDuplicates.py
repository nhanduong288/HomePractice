# to find duplicates in a list

def findingDuplicates(l):
    elements = {}
    for num in l:
        if num not in elements:
            elements[num] = 1
        else:
            return True
    return False

print(findingDuplicates([3,5,4,2,6])) # False
print(findingDuplicates([1,2,2,3,4,5])) # True