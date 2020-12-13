def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order
    result = list(reversed(list2))
    result.extend(list(reversed(list1)))
    return result

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

string = "hello there i'am testing some codes I found online!"
string2 = "".join(char for char in string if char.isalnum()).lower()


def compareTriplets(a, b):
    resulta = 0
    resultb = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            resulta += 0
            resultb += 0
            print(resulta, resultb)
        elif a[i] > b[i]:
            resulta += 1
            resultb += 0
            print(resulta, resultb)
        elif a[i] < b[i]:
            resulta += 0
            resultb += 1
            print(resulta, resultb)
    return [resulta, resultb]

a = [[1,2,3], [4,5,6], [9,8,9]]
for things in a:
    print(things)

'''print(a[0][0], a[1][1], a[2][2])
print(a[0][2], a[1][1], a[2][0])'''

leftright = 0
rightleft = 0

num = format(5, '.6f')

def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    nums = len(arr)
    for num in arr:
        if num > 0:
            pos += 1
        if num < 0:
            neg += 1
        if num == 0:
            zer += 1
    print(format(pos/nums, '.6f') + '\n' + format(neg/nums, '.6f') + '\n' + format(zer/nums, '.6f'))

def staircase(n):
    for i in range(1, n+1):
        print(' ' * (n-i) + '#' * (i))

staircase(6)

def gradingStudents(grades):
    result = []
    for i in range(1, len(grades)):
        if grades[i] >= 0 and grades[i] <= 100:
            if grades[i] < 38 or grades[i] % 5 == 0:
                result.append(grades[i])
            else:
                if (grades[i] + 3) % 5 != 0:
                    if (grades[i] + 1) % 5 == 0:
                        result.append(grades[i] + 1)
                    elif (grades[i] + 2) % 5 == 0:
                        result.append(grades[i] + 2)
                else:
                    result.append(grades[i])
    return result

print(gradingStudents([4, 73, 67, 38, 33]))
