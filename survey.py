import sys
import cowsay 
import re
from calc import Calculator
import random
import json
'''Import modules, to be used later in code: collect, compute and save data'''

stard={"Capricorn":2.3,"Gemini":3.4,"Saggitarius":4.5,"Cancer":5.6,"Taurus":6.7,"Scorpio":7.8,"Aquarius":8.9,"Aries":9.1,"Leo":10.2,"Libra":11.3,"Pisces":12.4,"Virgo":13.5}
colourd={'Red':2,"Orange":3,"Yellow":4,"Green":5,"Blue":6,"Indigo":7,"Violet":8}
'''Maps starsigns and colours to values, used for calculation'''

names = ["Player","Alex","Sam","Jamie","Jack"] #Used for autofill()
y_l = ["yes", "y"]
n_l = ["no", "n"]
yn_l =[y_l,n_l]

def line():
    '''Prints a line, simplifies code later on to be easily read. Ensures same line is printed each time'''
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^") 
    return

def sys_check():
    '''Checks version of python being used, if under 3.8 it wont run'''
    major = (sys.version_info[0])
    minor = (sys.version_info[1])
    if major < 3 and minor < 8:
        print("This program requires Python 3.8 or higher. Please update your Python version.")
    else:
        print("System check passed. Running on Python ",major,".",minor)

def get_yn(user_input): # Uses input from multiple different functions
    '''Simplifies code, makes other functions easier to read. Used when a yes or no input is required'''
    while True:
        yn_in = user_input.strip().lower()
        if yn_in in (y_l):
            return True # Returns as bool
        elif yn_in in (n_l):
            return False  # Returns as bool
        else:
            print("<-<--<---ERROR--->-->->\n== Simple yes or no ==\n------ TRY AGAIN ------") # Error handling
            return None # Returns as bool
        
def initial_q():
    '''Initial question to start the rest of the script, yes or no only.'''
    while True:
        cowsay.trex("WELCOME!")
        user_input = input("Want to do some epic questionaire? Y/N>> ")
        yn_0 = get_yn(user_input) #uses get_yn()
        if yn_0 == True:
            print("Continuing...")
            break
        elif yn_0 == False:
            print("Exiting...")
            exit()
        else:
            initial_q() # If returns None(invalid input) it returns back to initial question
        break

def rate_q():
    '''Promps user to give a rating of the cosway.trex, numbers only.'''
    while True:
            rat = input("Before we do this, how would you rate this dino out of 10?>>") 
            try:
                rate = int(rat) # Runs if a whole number is input
                if 20 >= rate > 10: # Allowed higher up to a point so script cant be exploited
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
                    print("<-<--<---ERROR--->-->->\n== Not even possible ==\n------ TRY AGAIN ------") # Error handling
                    continue
                return rate
            except ValueError:
                try:
                    rate = float(rat) # Runs if the input has a decimal to give more dialogue
                    print("Okayy pedantic much?. I can tell this will be, Fun.")
                    line()
                except ValueError:
                    print("<-<--<---ERROR--->-->->\n== Dude numbers only ==\n------ TRY AGAIN ------") # Error handling
                    continue
                return rate

def name_q():
    '''Asks user for name, letters only. Used in diologue for user. Also used when giving/saving results of survey'''
    while True:
        name = input("- 1 - Okay whats your name?>>").strip().title() # Unnessacary whitespace is removed and first letter is capitalised if not
        if re.match("^[a-zA-Z]+$", name):
            print("Wavvy bones "+ name +" cool name. alright NEXT QUESTION!")
            line()
        else:
            print("<-<--<---ERROR--->-->->\n== Aa -Zz Only ==\n------ TRY AGAIN ------")  # Error handling
            continue
        return name
    
def age_q(name): # Accessing the name of input from user to be used inside function
    '''Prompts user to give their age, numbers only. Used in calculations and some dialogue options'''
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
                print("<-<--<---ERROR--->-->->\n== Not even possible ==\n------ TRY AGAIN ------") # Error handling
                continue
            return age
        except ValueError:
            print("<-<--<---ERROR--->-->->\n== Dude numbers only ==\n------ TRY AGAIN ------") # Error handling
            continue    

def height_q(name): # Uses defined variables as parameters to be used inside the function
    '''Prompts user of their height in ft and inches, numbers only'''
    while True:
        try:
            ft, inch = map(int, input("- 3 - How tall are you in ft? Invasive question? complain to my boss\n(Show as: eg 6ft 1inch = 6 1)>>").split()) # Maps both variables as integers
            if inch > 12:
                print("<-<--<---ERROR--->-->->\n----- Quit Lying -----\n------ TRY AGAIN ------") # Error handling
                continue
            elif inch <= 0 or inch < 0:
                print("<-<--<---ERROR--->-->->\n- A minus number huh? -\n------ TRY AGAIN ------") # Error handling
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
                print("<-<--<---ERROR--->-->->\n== Dude numbers only ==\n------ TRY AGAIN ------") # Error handling
                continue 
        except ValueError:
                print("<-<--<---ERROR--->-->->\n== Dude numbers only ==\n------ TRY AGAIN ------") # Error handling
                continue
        return ft, inch
    
def colour_q():
    '''Prompts user for their favourite colour, letters only'''
    while True:
        try:
            colour = str(input("- 4 - Choose ur most favourite rainbow colour \n--->Red   Orange   Yellow   Green   Blue   Indigo   Violet<--- >>")).strip().title() # Takes away unnessacary whitespace and titles input
            if not re.match("^[a-zA-Z]+$", colour):
                print("<-<--<---ERROR--->-->->\n==== Aa -Zz Only ====\n------ TRY AGAIN ------") # Error handling
                continue
            elif colour not in colourd: # References the dictionary at top of code
                print("<-<--<---ERROR--->-->->\n---- Dude, ROYGBIV ----\n------ TRY AGAIN ------") # Error handling
                continue
            else:
                print("Ahaaahh..I usedd to see colours like that too my dude")
                line()
        except ValueError:
            print("<-<--<---ERROR--->-->->\n==== Aa -Zz Only ====\n------ TRY AGAIN ------") # Error handling
        return colour
    
def sibling_q():
    '''Prompts user of the amount of siblings they have, numbers only. Used in calculation'''
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
                print("<-<--<---ERROR--->-->->\n== Not even possible ==\n------ TRY AGAIN ------") # Error handling
                continue
        except ValueError:
                print("<-<--<---ERROR--->-->->\n== Dude numbers only ==\n------ TRY AGAIN ------") # Error handling
                continue
        return sib

def job_q(name, age): # Uses defined variables as parameters to be used inside the function
    '''Prompts user for vage job info, yes or no and float/int only. Used in calculation'''
    while True:
        user_input = (input("- 6 - You worked a day in ur life? Y/N>>")) 
        yn_1 = get_yn(user_input)
        if yn_1 == True:
            print("Oh nice I like seeing a contributing member of society")
            line()
            try: # Only happens if they say yes in the get_yn() function
                wage = float(input("- 6.5 - How much do/did you make an hour?>>")) 
                if wage >= 15:
                    print("Okayy if u say so I mean I cant force u to tell the truth..")
                    line()
                else:
                    print("Hard life "+ name + " bro, GET UR MONEY UP")
                    line()
            except ValueError:
                print("<-<--<---ERROR--->-->->\n== Dude numbers only ==\n------ TRY AGAIN ------")# Error handling
                continue
            return wage, yn_1
        elif yn_1 == False:
            wage = 0
            print("Wow at the big age of "+ str(age) + " still nothing to show for it..")
            line()
            return wage, yn_1

def star_q():
    '''Prompts user of their starsign, letters only . Used for calculaion'''
    while True:
        try:
            sta = str(input("- 7 - Okay lets get atrological whats your star sign?>>"))
            star = sta.strip().title()
            if not re.match("^[a-zA-Z]+$", star): # Uses re module for easy filters
                print("<-<--<---ERROR--->-->->\n==== Aa -Zz Only ====\n------ TRY AGAIN ------") # Error handling
                continue
            elif star not in stard:
                print("<-<--<---ERROR--->-->->\n--- Is that a sign? ---\n------ TRY AGAIN ------") # Error handling
                continue
            else:
                print("Oo.. I hear bad things from your.. type. Moving on")
                line()
                break
        except ValueError:
            print("<-<--<---ERROR--->-->->\n==== Aa -Zz Only ====\n------ TRY AGAIN ------") # Error handling
            continue
    return star

def erate_q(rate, name): # Uses defined variables as parameters to be used inside the function
    '''Prompts user for a final rating of survey, numbers only 0-20. Used in calculation'''
    while True:
        rate_2 = input("Okay now you have seen whats what, whats the rating now out of 10??>>")
        try:
            erate = int(rate_2)
            if erate > 10 and rate > 10:
                print("Okay stayin stupid I feel you")
                line()
            elif erate + rate >= 10:
                print("Hell yeah I knew I could sway ya")
                line()
            elif erate > 10 and rate < 10:
                print("Nice "+name+", this test definately dummed you down abit")
                line()
            elif 10 >= erate >= 7:
                print("Ayy I appreciate it "+name)
                line() 
            elif 7 > erate >= 4:
                print("Oh pretty average guess I aint worth it HUH??")
                line()
            elif 4 > erate >= 1:
                print("Oh well.. It is what it is")
                line()
            elif erate == 0:
                print("You will regret this...")
                line()
            else:
                print("<-<--<---ERROR--->-->->\n== Not even possible ==\n------ TRY AGAIN ------") # Error handling
                continue
            return erate
        except ValueError:
            try:
                erate = float(rate_2)
                if isinstance(erate, float) and isinstance(rate, float): # Asks if erate and rate are float
                    print("Okayyy dude you dont have to be so serious.. Seriously get some friends")
                elif isinstance(erate, float) and isinstance(rate, int): # Asks if erate is float and rate is float
                    print("Hmm weirdly specific but okay")
            except ValueError:
                print("<-<--<---ERROR--->-->->\n==== Dude numbers only ====\n------ TRY AGAIN ------") # Error handling
                continue
            return erate

def check_colour(colour): 
    '''Returns colours as a number for calculation'''
    return colourd.get(colour, 0)

def check_star(star):
    '''Returns starsigns as a number for calculation'''
    return stard.get(star, 0.0)

def auto_fill():
    '''If user decides to auto fill, returns all variables randomly'''
    seed = None
    if seed is not None:
        random.seed(seed) # Sets no value to seed to remove predictable randomness
    return {"rate": random.randint(1, 10),
        "name": random.choice(names),
        "age": random.randint(18, 40),
        "ft": random.randint(4, 6),
        "inch": random.randint(0, 11),
        "colour": random.choice(list(colourd.keys())),
        "siblings": random.randint(0, 6),
        "job": "Yes",
        "wage": round(random.uniform(8.0, 25.0), 2),
        "star": random.choice(list(stard.keys())),
        "erate": random.randint(1, 10)}

def save_r(results):
    '''Saves results to a file'''
    filename = "results.json" # Name of file to which the results are saved to
    try:
        with open(filename, 'w', newline='') as file:
            json.dump(results, file, indent=4)
            print("Results saved successfully!")
            print(f"Results saved to {filename}")
    except ValueError:
        print("An error occurred while saving the results.\n", ValueError) # If error occurs it will explain what happened and prompt you to try again
        keep_r(results)

def keep_r(name,age,ft,inch,colour,sibling,yn_1,wage,star,trate,yrs,mnts,dys,hrs,days,months,years):
    '''Prompts user to save result, if yes returns as a dictionary formatted for a file'''
    while True:
        user_input = input("Would you want to keep the results? Y/N>>")
        yn_2 = get_yn(user_input)
        if yn_2 == True:
            print("Saving results...")
            results = {"Name: ":name,
                    "Age: ":age,
                    "Height: ":f"{ft}ft {inch}inch",
                    "Colour: ":colour,
                    "Siblings: ":sibling,
                    "Job: ":f"{yn_1},Wage: ,{wage}/Hour",
                    "Starsign: ":star,
                    "Rating: ":trate,
                    "Time left: ":f"{yrs} years, {mnts} months, {dys} days, {hrs} hours",
                    "Death date: ":f"{days}/{months}/{years}"}
            save_r(results)
            exit()
        elif yn_2 == False:
            print("Returning...")
            exit()

def main():
    '''Gains all values for variables, prints them for the user and decides the order or functions'''
    initial_q()
    sys_check()
    user_input = input("Auto fill survey? Y/N>> ")
    yn_2 = get_yn(user_input)
    if yn_2 == True:
        data = auto_fill()
        rate = data["rate"]
        name = data["name"]
        age = data["age"]
        ft = data["ft"]
        inch = data["inch"]
        colour = data["colour"]
        sibling = data["siblings"]
        yn_1 = data["job"]
        wage = data["wage"]
        star = data["star"]
        erate = data["erate"]
    elif yn_2 == False:
        rate = rate_q()
        name = name_q()
        age = age_q(name)
        ft, inch = height_q(name)
        colour = colour_q()
        sibling = sibling_q()
        wage, yn_1 = job_q(name, age)
        star = star_q()
        erate = erate_q(rate, name)
    stars = check_star(star)
    colours = check_colour(colour)
    time = Calculator.compute(erate, rate, stars, ft, inch, colours, sibling, wage, age)
    hrs = time["Hours"]
    dys = time["Days"]
    mnts = time["Months"]
    yrs = time["Years"]
    trate = time["trate"]
    death_date = Calculator.death_date(yrs, mnts, dys)
    days = death_date[2]
    months = death_date[1]
    years = death_date[0]

    cowsay.trex("RESULTS")
    print("Consent: Yes")
    print("-1- Name: "+ name)
    print("-2- Age: "+str(age))
    print("-3- Height: "+str(ft)+"ft,"+str(inch)+"inch")
    print("-4- Fav colour: "+colour)
    print("-5- Siblings: "+str(sibling))
    print("-6- Job?: "+str(yn_1)+"           -6.5- Wage: "+str(wage)+"/Hour")
    print("-7- Starsign: "+star)
    print("-8- Rating: "+str(trate)+"/10")
    print("-9- You will die in: "+yrs+" years, "+mnts+" months, "+dys+" days, and "+hrs+" hours")
    print("-10- Death date: ", days,"/",months,"/",years)
    keep_r(name,age,ft,inch,colour,sibling,yn_1,wage,star,trate,yrs,mnts,dys,hrs,days,months,years)
main()