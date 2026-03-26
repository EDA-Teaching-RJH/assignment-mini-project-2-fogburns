import random
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Timetype:
    years: int
    months: int
    days: int
    hours: int
    trate: float

class Calculator:
    def __init__(self, seed=None):
        self.rng = random.Random(seed)

    def compute(erate, rate, stars, ft, inch, colours, sibling, wage, age):
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
        dt = datetime.now()
        years = dt.year + int(yrs)
        months = dt.month + int(mnts)
        days = dt.day + int(dys)
        return years, months, days