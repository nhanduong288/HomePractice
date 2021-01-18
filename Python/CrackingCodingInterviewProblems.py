#Function to determine if a string has all unique characters
def isUnique(str):
    #if any character repeats, return False
    for i in range(len(str)):
        for m in range(1, len(str)):
            if str[i] == str[m]:
                return False
        return True

#Check if one the strings is permutation of the other
def checkPermutation(str1, str2):
    #if 2 strings have the same length and have the same characters then it's True
    if len(str1) == len(str2):
        for letter1 in str1:
            if letter1 in str2:
                return True
    return False


#replace spaces with %20
def URLify(s):
    result = ""
    #remove front and back spaces
    s = s.strip()
    #replace spaces with "%20"
    for i in range(len(s)):
        if s[i] == " ":
            result += "%20"
        else:
            result += s[i]
    return result

#to determine if a string is a palindrome permutation
def palindromePermutation(s):
    result = False
    count = 0
    #if the length of the string is even and the number of characters is even
    #it's True
    if len(s)%2 == 0:
        for letter in s:
            if s.count(letter)%2 == 0:
                result = True
    #if the length of the string is odd
    #there should only be one character to be alone (that'd be the letter in the middle of the palindrome)
    elif len(s)%2 != 0:
        for letter in s:
            if s.count(letter)%2 != 0:
                count += 1
        if count <= 1:
            result = True
    return result

#to check if 2 strings a one or zero edits away from each other
def oneAway(s1, s2):
    count = 0
    #keep count of the characters that do not appear in both strings
    #if there are more than 1 character like that 
    #it's False
    for letter in s1:
        if letter not in s2:
            count += 1
    if count > 1:
        return False
    return True

#to do string comprehension
def stringComprehension(s):
    result = ""
    count = 0
    for letter in s:
        for i in range(len(s)):
            count += 1
            if i+1 >= len(s) or s[i+1] != s[i]:
                result += s[i] + str(count)
                count = 0
        return result

#to rotate a matrix 90 degree
def rotateMatrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

print([[1,2,3], [4,5,6], [7,8,9]])
print(rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
