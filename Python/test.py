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
    #The only way for kangaroos to catch up to each other is
    #For them to have different velocities AND 
    #the difference between starting point is the 
    #multiple of the difference between the velocities
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    else:
        return "NO"
        
print(kangaroo(0,3,4,2)) #YES
print(kangaroo(21,6,47,3)) #NO
print(kangaroo(28,8,96,2)) #NO
print(kangaroo(14,4,98,2)) #YES
print(kangaroo(0,2,5,3)) #NO

#Finding the total number of integers BETWEEN 2 sets a and b
#that satisfy these conditions:
#1. The elements of the first array are all factors of the integer being considered
#2. The integer being considered is a factor of all elements of the second array
def getTotalX(a, b):
    counter = 0
    #all function returns True only if everything is True
    for i in range(max(a), min(b)+1):
        if all([i % numsa == 0 for numsa in a]):
            if all([numsb % i == 0 for numsb in b]):
                counter += 1
    return counter

s = [1, 2, 1, 3, 2]
s = sorted(s)
print(s.count(1))

#Given an array of scores 
#The first score will be the bar to pass (either highest or lowest)
#breakingRecords will return the number of times that the "highest" or "lowest" score was surpassed
def breakingRecords(scores):
    high_counter = 0
    low_counter = 0
    #The first score is atomatically the "highet" or "lowest" score to start with
    high = low = scores[0]
    for score in scores:
        #If a lower score is found, counter increases and make it the "lowest"
        if score < low:
            low_counter += 1
            low = score
        #If a higher score is found, counter increases and make it the "highest"
        if score > high:
            high_counter += 1
            high = score
    return high_counter, low_counter

print(breakingRecords([10,5,20,20,4,5,2,25,1]))

def nameSuggestions(name):
    result = []
    name = name.lower()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'.upper()
    for alphabet in alphabets:
        if alphabet != name[0]:
            result.append(alphabet + name[1:])
    return result

def alternativeCaseTransform(sentence):
    result = ""
    for i in range(len(sentence)):
        if i%2 == 1: 
            result += sentence[i].lower()
        else: 
            result += sentence[i].upper()
    return result

print(alternativeCaseTransform("helloo my name is Nhan"))

#to determine if a given string is a permuation of a palindrome
def palindromePermutation(s):
    s = s.lower()
    result = False
    count = 1
    if len(s)%2 == 0: 
        for letter in s:
            if s.count(letter)%2 == 0:
                result = True
    elif len(s)%2 == 1:
        for letter in s:
            if s.count(letter)%2 == 1:
                count += 1
        if count <= 1:
            result = True
    return result

print(palindromePermutation("nhan duong"))
matrix = [[1,0,2], [2,3,4]]
position = []
for i in range(len(matrix)):
    if 0 in matrix[i]:
        position.append(i)
        position.append(matrix[i].index(0))

a = [3,5,2,1,4]
a.sort(reverse=True)
n = 2
for i in range(len(a) - 1):
    if a[i] >= n and a[i+1] < n:
        a.insert(a.index(a[i]), n)
        break
print(a)