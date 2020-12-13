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

#Create a staircase
#Input is an integer to represent the number of levels of the staircase
#The top level only has 1 '#' and the bottom level will have the same number of '#' as the number of levels
def staircase(n):
	#start the range at 1 because there will be no level with no steps
	for i in range(1, n+1):
		#top level has 1 '#' at the end with (n-1) number of spaces and so on
		print(' '*(n-i) + '#'*(i))

staircase(8)
