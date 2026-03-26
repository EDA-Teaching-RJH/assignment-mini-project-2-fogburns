import sys

def sys_check():
    major = (sys.version_info[0])
    minor = (sys.version_info[1])
    if major < 3 and minor < 8:
        print("This program requires Python 3.8 or higher. Please update your Python version.")
    else:
        print("System check passed. Running on Python ",major,".",minor)