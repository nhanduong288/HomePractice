import math

def something(n):
    while n % 2 == 0:
        n = n/2
    print(n)
    if n == 1:
        print("hi")
    print("hey")

def two_power(n):
    while n % 2 == 0 and n != 0:
        n = n / 2
    if n == 1:
        return True
    return False

def sum_divisors(n):
    sum = 0
    div = 1
    if n == 1 or n == 0:
        return n
    else:
        while div < n:
            if n % div == 0:
                sum += div
            else:
                sum += 0
            div += 1
    return sum

def first_and_last(message):
    if message[0] == message[-1]:
        return True
    return False

def upper_lower_case(string):
    new_string = ""
    for i in range(len(string)):
        if i % 2 == 1:
            new_string += string[i].lower()
        else:
            new_string += string[i].upper()
    return new_string

print(upper_lower_case("hello"))

def replace_ending(sentence, old, new):
    print("sup")
    if old in sentence:
        i = sentence.index(old)
        new_sentence = sentence[0:i] + new
        return new_sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
sentence = "It's raining cats and cats"
old = "cats"

l = ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']
l2 = list(enumerate(l))
l3 = []
for index, item in l2:
    if index % 2 == 0:
        l3.append(item)

def skip_elements(elements):
    l = list(enumerate(elements))
    result = []
    for index, item in l:
        if index % 2 ==  0:
            result += item
    return result

#print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))

def pig_latin(text):
    say = ""
    result = ""
    words = text.split(
    )
    for word in words:
        say = word[1:] + word[0] + "ay"
        result += say + " "
    return result

def group_per_user(group_dictionary):
    user_groups = {}
    for groups, users in group_dictionary.items():
        for user in users:
            user_groups.setdefault(user, []).append(groups)
    return user_groups

rand = {"local": ["admin", "userA"], "public": ["admin", "userB"],"administrator": ["admin"]}
print(group_per_user(rand))

def something(n):
    if (n <= 1):
        return 1
    else:
        return something(n - 1) + something(n-1)

print("hey " + str(something(5)))

def isPrime(n):
    x = 2
    while x <= math.sqrt(n):
        if (n % x == 0):
            return False
        return True
        x += 1

print(isPrime(7))


def test(n, arr):
	min_num = arr[0][0]
	max_num = arr[0][1]
	for i in range(1, n):
		if arr[i][0] < min_num:
			min_num = arr[i][0]
		if arr[i][1] > max_num:
			max_num = arr[i][1]
	if [min_num,max_num] in arr:
		print(arr.index([min_num,max_num]) + 1)
	else:
		print(-1)

test(6, [[1,5],[2,3],[1,10],[7,10],[7,7],[10,10]])