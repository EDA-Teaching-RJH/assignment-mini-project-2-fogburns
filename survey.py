import sys
import cowsay

y_l = ["yes", "y"]
n_l = ["no", "n"]
yn_l =[y_l,n_l]

def line():
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^") 
    return

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
        
def initial_q():
    while True:
        cowsay.trex("WELCOME!")
        user_input = input("Want to do some epic questionaire? Y/N>> ")
        yn_0 = get_yn(user_input)
        if yn_0 == True:
            print("Continuing...")
            break
        elif yn_0 == False:
            print("Exiting...")
            exit()
        else:
            initial_q()
        break

def rate_q():
    while True:
            rat = input("Before we do this, how would you rate this dino out of 10?>>") 
            try:
                rate = int(rat)
                if 20 >= rate > 10:
                    print("Wow big number, I got hope for you")
                    line()
                elif 10 >= rate >= 7:
                    print("Nice dude I like the excitement cool lets do this")
                    line()
                elif 7 > rate >= 4:
                    print("Okok I think I can get that number up. Lemme work")
                    line()
                elif 4 > rate >= 0:
                    print("Oh and you have seen better?. Yeah think next time")
                    line()
                else:
                    print("<-<--<---ERROR--->-->->\n== Not even possible ==\n------ TRY AGAIN ------")
                    continue
                return rate
            except ValueError:
                try:
                    rate = float(rat)
                    print("Okayy pedantic much?. I can tell this will be, Fun.")
                    line()
                except ValueError:
                    print("<-<--<---ERROR--->-->->\n== Dude numbers only ==\n------ TRY AGAIN ------")
                    continue
                return rate


initial_q()
sys_check()
rate_q()