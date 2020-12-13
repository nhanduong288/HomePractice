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
    '''result = []
    for i in range(0, len(grades)):
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
    return result'''
    return [grade if (grade < 38 or grade % 5 < 3) else (grade + (5 - grade % 5)) for grade in grades[1:]]

print(gradingStudents([4, 73, 67, 38, 33]))

def countApplesAndOranges(s, t, a, b, apples, oranges):
    result_app = []
    result_ora = []
    result = []
    counter_app = 0
    counter_ora = 0
    for distance in apples:
        result_app.append(a+distance)
    for distance in oranges:
        result_ora.append(b + distance)
    for nums in result_app:
        if nums >= s and nums <= t:
            counter_app += 1
    for nums in result_ora:
        if nums >= s and nums <= t:
            counter_ora += 1
    result.append(counter_app)
    result.append(counter_ora)
    for things in result:
        print(things)

def kangaroo(x1, v1, x2, v2):
    if (x1 > x2 and v1 > v2) or (x2 > x1 and v2 > v1):
        return "NO"
    elif (x1 == x2 and v1 < v2) or (x1 == x2 and v2 < v1):
        return "NO"
    elif (v1 == v2 and x1 < x2) or (v1 == v2 and x2 < x1):
        return "NO"
    elif (x1 < x2 and (x1 / x2) < (v1 / v2)) or (x2 < x1 and (x2 / x1) < (v2 / v1)):
        return "NO"
    else:
        return "YES"

print(abs(0/4)!= abs(4/2))
print(kangaroo(0,3,4,2))
print(kangaroo(21,6,47,3))