# a small program to demonstrate the use of Regular Expression in Python

import re

# this function is used to find phone numbers within a string
def findPhoneNo(text):
    # phone numbers in the US is formatted to look like 123-456-7890
    # in regular expression \d means digit character
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    
    print(phoneNumRegex.findall(text)) # print all phone numbers

    print(phoneNumRegex.search(text)) # print the first phone number found

findPhoneNo('hello there my phone number is 612-242-9237. if you cannot reach me, call my wife at 612-607-4101')

# trying another matching pattern

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.search('My phone number is 612-242-9237') # will let you know if there is a match
no = phoneNumRegex.search('My phone number is 612-242-9237 and 612-607-4101')
print(no.group()) # return the entire pattern

# another pattern with seperate individual groups inside of it
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNumRegex2.search('My phone number is 612-242-9237')
no2 = phoneNumRegex2.search('My phone number is 612-242-9237')
print(no2.group()) # will do the same thing 
print(no2.group(1)) # return the first group inside the pattern - 612
print(no2.group(2)) #return the second group inside the pattern - 242-9237

# if we wanted the result to include () then use the \( \) character
phoneNumRegex3 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
no3 = phoneNumRegex3.search('My phone number is (612) 242-9237, 612-607-4101')
print(no3.group()) # return the first numer found including the parenthesis

# | is called the pipe character
batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # groups are seperated by the pipe character
bat = batRegex.search('Batmobile lost a wheel')
print(bat.group()) # return the first match - Batmobile

# example of repetition in regex pattern
batRegex2 = re.compile(r'Bat(wo)?man') # the question marks mean that 'wo' can appear in the text 0 or 1 time in order to match the pattern
bat2 = batRegex2.search('The Andventure of Batman')
print(bat2.group()) # return Batman
# it will return Batwoman if the text was 'The Adventure of Batwoman'
# it will return None if the text was 'The Adventure of Batwowowoman' because 'wo' appeared more than once

# another example of ? 
phoneNumRegex4 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
no4 = phoneNumRegex4.search('My phone number is 612-242-9237')
print(no4.group()) # return 612-242-9237
# it will return None if missing area code

# use ? to make area code optional
phoneNumRegex5 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') # area code can appear 0 or once
no5 = phoneNumRegex5.search('My phone number is 242-9237')
print(no5.group()) # return 242-9237

# * character means matching 0 or more times
batRegex3 = re.compile(r'Bat(wo)*man')
bat3 = batRegex3.search('The Adventures of Batwowowowowoman')
print(bat3.group()) # return Batwowowowowoman

# + character means matching 1 or more --> the appearance is no more optional
batRegex4 = re.compile(r'Bat(wo)+man')
bat4 = batRegex4.search('The Aventures of Batwoman')
print(bat4.group())

# {} means matching the exact number of repetition
# {num1, num2} means matching the number of repetition in the range of num1 to num2
haRegex = re.compile(r'(Ha){3}')
ha = haRegex.search('He said "HaHaHa"')
print(ha.group())

''' TO RECAP:
- The ? says the group matches zero or one times
- The * says that group matches zero of more times
- The + says the group matches one or more times
- The curly braces with 2 number smatches a minimum and maximum number ot times
- Leaving out the first or second in the curly braces says there is no minimum or maximum
- Greddy matching match the longest string possible, nongreedy matching match the shortest string possible
- Putting a question mark after the curly braces makes it do a nongreedy match
'''

# other regex characters /d, /D, /w, /W, /s, /S
lyrics = '12 drummers drumming, 11 pipers poping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying,  5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'
xmasRegex = re.compile(r'\d+\s\w+') # 1 or more digits, 1 space, and one or more word letters
print(xmasRegex.findall(lyrics))

# create your own characters with []
vowelRegex = re.compile(r'[aeiouAEIOU]') # the same with r'a|e|i|o|u'
# [a-z] = a to z
print(vowelRegex.findall('Robocops eats baby food.'))

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}') # to match exactly 2 vowels in a row
print(doubleVowelRegex.findall('Robocop eats baby food.')) # return ea and oo

# ^ character means not matching with group
vowelRegex2 = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex2.findall('Robotcop eats baby food.'))

''' TO RECAP:
- The regex method findall() is passed a string, and returns all matches in it, not just the first match
- If the regex has 0 or 1 group, findall() returns a list of strings
- If the regex has 2 or more groups, findall() returns a list of tuples of strings
- \d is digit, \w is word character, \s is space 
- The uppercase \S, \D, \W match characters that are NOT digit, word, space
- You can create your own character with []
- ^ makes it match anything that is not in a group
'''

# ^ character indicates that the match has to occur at the beginning - ^something
# $ character indicates that the match has to occur at the end - something$
# having both ^ and $ means must natch the enitre text
beginWithHelloRegex = re.compile(r'^Hello')
beginWithHello = beginWithHelloRegex.search("Hello there")
print(beginWithHello.group()) # will not work with "He said Hello"

endWithHelloRegex = re.compile(r'Hello$')
endWithHello = endWithHelloRegex.search("He said Hello")
print(endWithHello.group()) # will not work with "Hello there"

allDigitsRegex = re.compile(r'^\d+$') # digits from beginning to the end
allDigits = allDigitsRegex.search('92386450871923465') # there cannot be anything else other than digits within the text
print(allDigits.group())

# . character means matching everything except newline character
atRegex = re.compile(r'.at') # matching anything that has 1 character following with at
# r'.{1,2}at' will return matches with 1 or 2 characters following "at"
print(atRegex.findall('The cat in the har sat on the flat mat.')) # does not return "flat" because there are 2 characters follwing "at"

# .* means matching anything
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') # this means look for the text "First Name: " and "Last Name: " then return whatever comes after that
print(nameRegex.findall('First Name: Al Last Name: Sweigart'))

# use ? for non-greedy find
nonGreedyRegex = re.compile(r'<(.*?>)')
print(nonGreedyRegex.findall("<To Serve Humans> for dinner.>")) # only return <To Serve Humans>

greedyRegex = re.compile(r'<(.*>)')
print(greedyRegex.findall("<To Serve Humans> for dinner.>")) # return the whole thing

''' TO RECAP:
- ^ means the string must start with the pattern, $ means the string must end with the pattern. Both means the entire string must match the pattern
- The . is a wildcard; it matches anything except newlines.
- Pass re.DOTALL as the second argument to re.compile() to make the . match newlines as well
- Pass re.I as the second argument to re.compile() to make the matching case sensitive
'''

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall("Agent Alice gave the secret documents to Agent Bob."))
print(namesRegex.sub('REDACTED', "Agent Alice gave the secret documents to Agent Bob.")) # subsitute all matches with REDACTED

nameRegex2 = re.compile(r'Agent (\w)\w*')
print(nameRegex2.sub(r'Agent \1*****', 'Agent Alice gave the secret documents to Agent Bob.'))
