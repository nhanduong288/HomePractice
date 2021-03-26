# to find a pair of integers that sums to a number

def sumPair(l, s):
    # using hash/dictionary
    dict = {}
    for num in l:
        if num not in dict:
            dict[num] = 1
    for key in dict:
        if (s-key) in dict:
            return [key, s-key]
    return None

print(sumPair([6,3,5,2,1,7], 100))