from collections import Counter

#The groups_per_user function receives a dictionary, which contains group names with the list of users.
#Users can belong to multiple groups.
#Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for groups, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary
			user_groups.setdefault(user, []).append(groups)
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
print("--------------------------------------------------")

#Complete the function digits(n) that returns how many digits the number has.
#For example: 25 has 2 digits and 144 has 3 digits.
#Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.
def digits(n):
	count = 0
	if n == 0:
	  return 1
	while (n / 10 > 0):
		count += 1
		n = n // 10
	return count

print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1
print("--------------------------------------------------")

#This function prints out a multiplication table
#(where each number is the result of multiplying the first number of its row by the number at the top of its column).
#Fill in the blanks so that calling multiplication_table(1, 3) will print out:
#1 2 3
#2 4 6
#3 6 9
def multiplication_table(start, stop):
	for x in range(start, stop+1):
		for y in range(start, stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above
print("--------------------------------------------------")

#The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise.
#Fill in the blanks to make this work correctly.
def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x -= 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x += 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
print("--------------------------------------------------")

#The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2,
#up to and including the maximum that's passed into the function.
#For example, even_numbers(6) returns “2 4 6”.
#Fill in the blank to make this work.
def even_numbers(maximum):
	return_string = ""
	for x in range(maximum+1):
		if x > 0 and x%2 == 0:
			return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed
print("--------------------------------------------------")

#A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom.
#Drew was the first one to note which students arrived, and then Jamie took over.
#After the class, they each entered their lists into the computer
#and emailed them to the professor, who needs to combine them into one,
#in the order of each student's arrival.
#Jamie emailed a follow-up, saying that her list is in reverse order.
#Complete the steps to combine them into one list as follows:
#the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  list1 = list(reversed(list1))
  list2 = list(reversed(list2))
  for things in list1:
    list2.append(things)
  return list2


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
print("--------------------------------------------------")

#Create a staircase
#Input is an integer to represent the number of levels of the staircase
#The top level only has 1 '#' and the bottom level will have the same number of '#' as the number of levels
def staircase(n):
	#start the range at 1 because there will be no level with no steps
	for i in range(1, n+1):
		#top level has 1 '#' at the end with (n-1) number of spaces and so on
		print(' '*(n-i) + '#'*(i))

staircase(8)
print("--------------------------------------------------")

#This is a grading system
#Students receive grades from 1 to 100
#Input's first line is the number of students
#Next lines will be the grades and the program will round up the grades if they satisfy some conditions
#If the grade is below 38, it will be kept as "failing grade"
#If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5
#Other grades will be kept as is
def gradingStudents(grades):
	#Commented out the original solution
	#It works but lengthy
	'''result = []
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
    return result'''
	return [grade if (grade < 38 or grade % 5 < 3) else (grade + (5 - grade % 5)) for grade in grades[1:]]
	print("--------------------------------------------------")

#There are 2 kangaroos in a circus
#x1 = starting point of kangaroo 1
#x2 = starting point of kangaroo 2
#v1 = velocity of kangaroo 1
#v2 = velocity of kangaroo 2
#Return "YES" if at some points 2 kangaroos are at the same place
#Otherwise return "NO"
def kangaroo(x1, v1, x2, v2):
    #The only way for kangaroos to catch up to each other is
    #For them to have different velocities AND 
    #the difference between starting point is the 
    #multiple of the difference between the velocities
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
    	return "Result of kangaroo: YES"
    else:
       	return "Result of Kangaroo: NO"

print(kangaroo(0,3,4,2)) #YES
print(kangaroo(21,6,47,3)) #NO
print(kangaroo(28,8,96,2)) #NO
print(kangaroo(14,4,98,2)) #YES
print(kangaroo(0,2,5,3)) #NO
print("--------------------------------------------------")

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

print("Result of getTotalX: " + str(getTotalX([2,4], [16,32,96]))) #3
print("--------------------------------------------------")

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


print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))
print("--------------------------------------------------")

#Given a chocolate bar, two children, Lily and Ron, are determining how to share it
#s: an array of integers, the numbers on each of the squares of chocolate
#d: an integer, Ron's birth day
#m: an integer, Ron's birth month
#Lily wants to share a contiguous segment of the bar selected such that:
#1. The length of the segment matches Ron's birth month
#2. The sum of the integers on the squares is equal to his birth day
#birhtday function returns an integer denoting the number of ways Lily can divide the bar
def birthday(s, d, m):
	#an array to store all the sums of integers
	result = []
	for i in range(len(s)):
		sums = 0
		#to make sure to not go over array's length
		if len(s) >= (i + m):
			#to calculate the sum of m consecutive integers
			for nums in s[i:i+m]:
				sums += nums
			#only add to result array if it equals to d
			if sums == d:
				result.append(sums)
	return len(result)

print(birthday([1,2,1,3,2], 3, 2)) #2
print(birthday([1,1,1,1,1,1], 3, 2)) #0
print(birthday([4], 4, 1)) #1
print("--------------------------------------------------")

#Given an array of n integers ar = [ar[0], ar[1],...,ar[n-1]]
#and a positive integer k
#Find pairs of (i,j) where i < j and ar[i] + ar[k] % k == 0
def divisibleSumPairs(n, k, ar):
	ar = sorted(ar)
	counter = 0
	for i in range(n):
		for m in range(1, n, 1):
			if i < m and (ar[i] + ar[m]) % k == 0:
				counter += 1
	return counter

print(divisibleSumPairs(6, 3, [1,3,2,6,1,2])) #5
print(divisibleSumPairs(2, 2, [8, 10])) #1
print(divisibleSumPairs(5, 2, [5, 9, 10, 7, 4])) #4
print("--------------------------------------------------")

def migratoryBirds(arr):
	arr = sorted(arr)
	hold = arr[0]
	for num in arr:
		if arr.count(num) > arr.count(hold):
			hold = num
	return hold

print(migratoryBirds([1,1,1,4,4,4,5,3])) #1
print(migratoryBirds([1,1,4,4,4,5,3])) #4
print("--------------------------------------------------")

#The programmer day every year is the 256th day
#Leap year will have 29 days for February other than 28 days
#In Russia 1700-2700, people use Julian calendar then transition to Gregoria
#The transition year is 1918 where the day after 01/31 is 02/14
#In Julian calendar, leap year is the year that is divisible by 4
#In Gregorian calendar, lear year is the year that
#either: divisible by 400 or divisible by 4 and not by 100
def dayOfProgrammer(year):
	months = []
	sum_of_days = 0
	month = 0
	day = 0
	#Set up the months based on years
	if year >= 1700 and year <= 1917:
		if year % 4 == 0:
			months = [31,29,31,30,31,30,31,31,30,31,30,31]
		else:
			months = [31,28,31,30,31,30,31,31,30,31,30,31]
	if year >= 1919:
		if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
			months = [31,29,31,30,31,30,31,31,30,31,30,31]
		else:
			months = [31,28,31,30,31,30,31,31,30,31,30,31]
	if year == 1918:
		months = [31, 15, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	
	#256th day of the year will fall randomly inside a month
	#Keep adding days of months together when it has not reached 256
	for i in range(len(months)):
		if sum_of_days < 256:
			day = 256 - sum_of_days
			sum_of_days += months[i]
			month = i + 1

	print(str(day) + "." + "{:02d}".format(month) + "." + str(year))

dayOfProgrammer(2017) #13.09.2017
dayOfProgrammer(2016) #12.09.2016
dayOfProgrammer(1800) #12.09.1800
dayOfProgrammer(1919) #13.09.1919
dayOfProgrammer(1918) #26.09.1918
print("--------------------------------------------------")

#Bill and Anna went out to eat
#bill is an array of prices of what were ordered
#Anna did not eat the item at index k
#b is the money Bill asked Anna to pay
#If Bill was right print "Bon Appetit"
#If he was not, print the difference that Bill needed to refund to Anna
def bonAppetit(bill, k, b):
	total = 0
	share = 0
	for i in range(len(bill)):
		if i != k:
			total += bill[i]
	share = total / 2
	if share == b:
		print("Bon Appetit")
	else:
		print(int(abs(share - b)))

bonAppetit([3,10,2,9], 1, 12) #5
bonAppetit([72,53,60,66,90,62,12,31,36,94], 6, 288) #6
bonAppetit([40,39,97,5,2,84,35,93,59,39], 2, 198) #Bon Appetit
print("--------------------------------------------------")

#Given the n number of socks
#and an array ar of their serial number
#Determine how many pairs of socks with matching serial number there are
def sockMerchant(n, ar):
	#Create a new pair to contain all the socks with at least 2 counts
	#which means they will at least 1 pair
	have_pair = []
	result = 0
	for num in ar:
		if ar.count(num) >= 2:
			have_pair.append(num)
	#From the array have_pair of all socks that have more than a pair
	#Create another list with no duplicate item
	have_pair = list(dict.fromkeys(have_pair))
	#Use the serial number to determine how many pairs there are
	for socks in have_pair:
		if ar.count(socks) % 2 == 0:
			result += ar.count(socks) / 2
		else:
			result += (ar.count(socks) - 1) / 2
	print(int(result))

sockMerchant(9, [10,20,20,10,10,30,50,10,20]) #3
sockMerchant(7, [1,2,1,2,1,3,2]) #2
print("--------------------------------------------------")

#Teacher asks students to open book to a page
#The students can either open from the front or the back
#Students always turn 1 page at a time
#Given n is the number of pages that the book has
#p is the page to turn to
#the minimum number of pages that must be turned in order to arrive at page p
def pageCount(n, p):
	print(int(min(p//2, n//2 - p//2)))

pageCount(6,2) #1
pageCount(5,4) #0
pageCount(6,5) #1
print("--------------------------------------------------")

#An avid hiker keeps records of his/her hikes
#Every uphill step is recorded as U
#Every downhill step is recorded as D
#A mountain is a sequence of consecutive steps above sea level, 
#starting with a step up from sea level and ending with a step down to sea level.
#A valley is a sequence of consecutive steps below sea level, 
#starting with a step down from sea level and ending with a step up to sea level.
#Given the steps and path, return the number of times the hiker went to a valley
def countingValleys(steps, path):
	seaLevel = valley = 0
	for ways in path:
		for way in ways:
			if way == 'U':
				seaLevel += 1
			else:
				seaLevel -= 1
		
			if way == 'U' and seaLevel == 0:
				valley += 1

	return valley

print(countingValleys(8, ['UDDDUDUU'])) #1
print(countingValleys(12, ['DDUUDDUDUUUD'])) #2
print("--------------------------------------------------")


def getMoneySpent(keyboards, drives, b):
	max_budget = 0
	if keyboards[0] + drives[0] <= b:
		max_budget = keyboards[0] + drives[0]
	for keyboard in keyboards:
		for drive in drives:
			if keyboard + drive >= max_budget and keyboard + drive <= b:
				print("max budget: " + str(max_budget))
				max_budget = keyboard + drive
				return max_budget
			else:
				return -1

print(getMoneySpent([10,2,3], [3,1], 9))