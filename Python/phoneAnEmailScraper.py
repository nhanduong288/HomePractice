#! python3

import re, pyperclip

# TODO: Create a regex for phone numbers
re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

((\d\d\d) | (\(\d\d\d)))?         # area code (optional)
(\s|-)                            # first seperator
\d\d\d                            # first 3 digits
-                                 # seperator                         
\d\d\d\d                          # last 4 digits
extension (optional)
((ext(\.)?\s | x)                 # extension word-part (optional)
 (\d{2,5}))?                      # extention number_part (optional)
''', re.VERBOSE)

# TODO: Create a regex for email addresses
# TODO: Get the text off the clipboard
# TODO: Extract the email/phone from this text
# TODO: Copy the extracted email/phone to the clip board


