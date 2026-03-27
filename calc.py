import random
from dataclasses import dataclass
from datetime import datetime
'''Imports to be used in the code: proccessing data'''

@dataclass
class Timetype:
    '''Ensures variables are correct class types'''
    years: int
    months: int
    days: int
    hours: int
    trate: float
if __name__ != "__main__":
    class Calculator:
        def __init__(self, seed=None):
            '''If seed is chosen ensures predictable randomness'''
            self.rng = random.Random(seed)

        def compute(erate, rate, stars, ft, inch, colours, sibling, wage, age):
            '''Calculates all variables returns as an amount of time'''
            number = random.uniform(1.0,5.0)
            trate = erate + int(rate) / 2
            frate = int(round(trate, 1)*10)
            hrs=(frate+stars+(ft*inch)+colours+sibling+wage-age)*number*360
            yrs=str(round(hrs/8765))
            mnts=str(round((hrs%8765)/730))
            dys=str(round((hrs%8765)%730/24))
            hrs=str(round(((hrs%8765)%730)%24))
            return {"Years":yrs,"Months":mnts,"Days":dys,"Hours":hrs,"trate":trate}
        
        def death_date(yrs, mnts, dys):
            '''Converts the time from compute() into a date'''
            dt = datetime.now()
            years = dt.year + int(yrs)
            months = dt.month + int(mnts)
            days = dt.day + int(dys)
            return years, months, days
    
