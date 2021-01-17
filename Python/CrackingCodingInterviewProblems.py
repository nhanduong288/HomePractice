#Function to determine if a string has all unique characters
def isUnique(str):
    for i in range(len(str)):
        for m in range(1, len(str)):
            if str[i] == str[m]:
                return False
        return True

'''print(isUnique("aab")) #false
print(isUnique("abc")) #true
print(isUnique("nhan")) #false
print(isUnique("san")) #true'''

#Check if one the strings is permutation of the other
def checkPermutation(str1, str2):
    if len(str1) == len(str2):
        for letter1 in str1:
            if letter1 in str2:
                return True
    return False

'''print(checkPermutation("ABC", "BCA")) #true
print(checkPermutation("ABCC", "CCBA")) #true
print(checkPermutation("AABC", "ABC")) #false
print(checkPermutation("NHAN", "NHAAN")) #false
print(checkPermutation("ABC", "ABC")) #true
print(checkPermutation("AAAAA", "AAAAAC")) #false'''

#replace spaces with %20
def URLify(s):
    result = ""
    s = s.strip()
    for i in range(len(s)):
        if s[i] == " ":
            result += "%20"
        else:
            result += s[i]
    return result

print(URLify("nhan duong   "))
print(URLify("Mr John Smith"))

cd 