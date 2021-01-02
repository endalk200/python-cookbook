"""
sys module: System-specific parameters and functions

This module provides access to some variables used or maintained by the 
interpreter and to functions that interact strongly with the interpreter.
It is always available.
"""

import sys

# The operating systems information
print(f"platform: {sys.platform}")

# Python version, date of compilation and compiler name
print(f"python version: {sys.version}")
# return python version only in more concise manner use this api to extract
# python version number
print(f"python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
