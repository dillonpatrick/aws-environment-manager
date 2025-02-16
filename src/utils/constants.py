import os

""" `CURDIR` is a variable that stores the current working directory path.
The `os.getcwd()` function is used to get the current working directory,
and `replace("\", "/")` is used to replace backslashes with forward slashes in
the path to convert it from a Windows path format to a Unix path format.
"""

CURDIR = os.getcwd().replace("\\", "/")  # windows -> unix path
