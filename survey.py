import sys
import cowsay
import re

colourd={'Red':2,"Orange":3,"Yellow":4,"Green":5,"Blue":6,"Indigo":7,"Violet":8}
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

def name_q():
    while True:
        name = input("- 1 - Okay whats your name?>>").strip().title()
        if not re.match("^[a-zA-Z]+$", name):
            print("<-<--<---ERROR--->-->->\n== Aa -Zz Only ==\n------ TRY AGAIN ------")
            continue
        else:
            print("Wavvy bones "+ name +" cool name. alright NEXT QUESTION!")
            line()
        return name
    
def age_q(name):
    while True:
        try:
            age = int(input("- 2 - How old are you "+ str(name) +"?>>")) 
            if 80 >= age >= 65:
                print("And you operated this machine? Impressive but I wouldnt hold out "+ name)
                line()
            elif 65 > age >= 35:
                print("Oh would never had guessed, still paying off debt? GOODLUCK")
            elif 35 >= age >= 20:
                print("Okayy golden age huh? Hows it feel?.. Yeah we can move on.")
                line()
            elif 20 > age >= 8:
                print("Still tryna make it in life? Goodluck I uh.. Believe in. You, yeah..")
                line()
            elif 8 > age >= 4:
                print("Okay then " + name + " a abit young to be playing this but sure")
            elif age < 4 and age >= 0:
                print("It does not look good lying about your age like that.. Try again")
                continue
            else:
                print("<-<--<---ERROR--->-->->\n== Not even possible ==\n------ TRY AGAIN ------")
                continue
            return age
        except ValueError:
            print("<-<--<---ERROR--->-->->\n== Dude numbers only ==\n------ TRY AGAIN ------")
            continue    

def height_q(name):
    while True:
        try:
            ft, inch = map(int, input("- 3 - How tall are you in ft? Invasive question? complain to my boss\n(Show as: eg 6ft 1inch = 6 1)>>").split())
            if inch > 12:
                print("<-<--<---ERROR--->-->->\n----- Quit Lying -----\n------ TRY AGAIN ------")
                continue
            elif inch <= 0 or inch < 0:
                print("<-<--<---ERROR--->-->->\n- A minus number huh? -\n------ TRY AGAIN ------")
                continue
            try:
                if ft >=6 and 12 >= inch >= 7:
                    print("Go back to the zoo u damn FREAK!")
                    line()
                elif ft == 7 and 12 >= inch >= 0:
                    print("Glad im behind a screen right now.")
                elif ft == 6 and 7 > inch >= 0:
                    print("Alr alr no need to brag")
                    line()
                elif ft == 5 and 11 >= inch >= 10:
                    print("Unlucky Bro...")
                    line()
                elif ft == 5 and 9 >= inch >= 5 :
                    print("Pretty average stuff so far")
                    line()
                elif 5 == ft and 4 >= inch >= 0:
                    print ("Hah troubles reaching the shelves "+ name +"?")
                    line()
                elif 4 > ft >= 0 and 12 >= inch >= 0:
                    print("Okay sure buddy.. Too late to change now.")
                    line()
            except ValueError:
                print("<-<--<---ERROR--->-->->\n== Dude numbers only ==\n------ TRY AGAIN ------")
                continue 
        except ValueError:
                print("<-<--<---ERROR--->-->->\n== Dude numbers only ==\n------ TRY AGAIN ------")
                continue
        return ft, inch
    
def colour_q():
    while True:
        try:
            colour = str(input("- 4 - Choose ur most favourite rainbow colour \n--->Red   Orange   Yellow   Green   Blue   Indigo   Violet<--- >>")).strip().title() 
            if not re.match("^[a-zA-Z]+$", colour):
                print("<-<--<---ERROR--->-->->\n==== Aa -Zz Only ====\n------ TRY AGAIN ------")
                continue
            elif colour not in colourd:
                print("<-<--<---ERROR--->-->->\n---- Dude, ROYGBIV ----\n------ TRY AGAIN ------")
                continue
            else:
                print("Ahaaahh..I usedd to see colours like that too my dude")
                line()
        except ValueError:
            print("<-<--<---ERROR--->-->->\n==== Aa -Zz Only ====\n------ TRY AGAIN ------")
        return colour
    
def sibling_q():
    while True:
        try:
            sib = int(input("- 5 - How many brothers and sisters u got on this earth?>>"))
            if 20 >= sib > 4:
                print("Damn your mumma tryna build an army? aint judging brother..")
                line()
            elif 4 >= sib >= 1:
                print("Yeah thats pretty average you aint cool")
                line()
            elif sib == 0:
                print("Bro I dont even know what to tell ya, make some friends I guess lol")
                line()
            else:
                print("<-<--<---ERROR--->-->->\n== Not even possible ==\n------ TRY AGAIN ------")
                continue
        except ValueError:
                print("<-<--<---ERROR--->-->->\n== Dude numbers only ==\n------ TRY AGAIN ------")
                continue
        return sib

def job_q(name, age):
    while True:
        user_input = (input("- 6 - You worked a day in ur life? Y/N>>")) 
        yn_1 = get_yn(user_input)
        if yn_1 == True:
            print("Oh nice I like seeing a contributing member of society")
            line()
            try:
                wage = float(input("- 6.5 - How much do/did you make an hour?>>")) 
                if wage >= 15:
                    print("Okayy if u say so I mean I cant force u to tell the truth..")
                    line()
                else:
                    print("Hard life "+ name + " bro, GET UR MONEY UP")
                    line()
            except ValueError:
                print("<-<--<---ERROR--->-->->\n== Dude numbers only ==\n------ TRY AGAIN ------")
                continue
            return wage, yn_1
        elif yn_1 == False:
            wage = 0
            print("Wow at the big age of "+ str(age) + " still nothing to show for it..")
            line()
            return wage, yn_1

initial_q()
sys_check()
rate_q()
name = name_q()
age = age_q(name)
ft, inch = height_q(name)
colour = colour_q()
sibling = sibling_q()
wage, yn_1 = job_q(name, age)

print(name,age,ft,inch,colour,sibling,wage,yn_1)