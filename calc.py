import random

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
    