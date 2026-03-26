import sys

y_l = ["yes", "y"]
n_l = ["no", "n"]
yn_l =[y_l,n_l]

def sys_check():
    major = (sys.version_info[0])
    minor = (sys.version_info[1])
    if major < 3 and minor < 8:
        print("This program requires Python 3.8 or higher. Please update your Python version.")
    else:
        print("System check passed. Running on Python ",major,".",minor)

def get_yn(user_input):
    while True:
        yn_in = user_input.strip().lower()
        if yn_in in (y_l):
            return True
        elif yn_in in (n_l):
            return False  
        else:
            print("<-<--<---ERROR--->-->->\n== Simple yes or no ==\n------ TRY AGAIN ------")
            return None