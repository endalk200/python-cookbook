"""
File Finder.
@author: endalk200

This scripts searchs a given directory recursively to find a specified file
"""
import os
import time

def find_file(top, file_name):
    for path, dirs, files in os.walk(top):
        for __filename__ in files:
            if __filename__ == file_name:
                print(f"Found the file at {os.path.join(path, __filename__)}")

if __name__ == '__main__':
    find_file(os.getcwd(), "README.md")
