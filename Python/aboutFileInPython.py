# from Automate Boring Stuff with Python
# learning how to work with files

# os module
import os

# to have a string of file path
# use os.path.join to make sure it works on NOT JUST windows
path = os.path.join('folder1', 'folder2', 'folder3', 'file.png')
print(path)