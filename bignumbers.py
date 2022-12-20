def million(n): return int(n*(10**6))
def billion(n): return int(n*(10**9))
def trillion(n): return int(n*(10**12))
def quadrillion(n): return int(n*(10**15))
def quintillion(n): return int(n*(10**18))
def sextillion(n): return int(n*(10**21))
def septillion(n): return int(n*(10**24))
def octillion(n): return int(n*(10**27))
def nonillion(n): return int(n*(10**30))
def decillion(n): return int(n*(10**33))
def undecillion(n): return int(n*(10**36))
def duodecillion(n): return int(n*(10**39))
def tredecillion(n): return int(n*(10**42))
def quattuordecillion(n): return int(n*(10**45))
def quindecillion(n): return int(n*(10**48))
def sexdecillion(n): return int(n*(10**51))

class Infinity:
    def __init__(self): pass
    def __lt__(self,a): 
        return False
    def __le__(self,a):
        if type(a) == type(self):
            return True
        return False
    def __eq__(self,a):
        if type(a) == type(self):
            return True
        return False
    def __gt__(self,a): 
        if type(a) == type(self):
            return False
        return True
    def __ge__(self,a):
        return True
    def __str__(self):
        return "Infinity "
    def __add__(self,a):
        return self
    def __div__(self,a):
        return self
    def __idiv__(self,a):
        return self
    def __iadd__(self,a):
        return self
    
    
class NegativeInfinity:
    def __init__(self): pass
    def __lt__(self,a): 
        if type(a) == type(self):
            return False
        return True
    def __le__(self,a):
        return True
    def __eq__(self,a):
        if type(a) == type(self):
            return True
        return False
    def __gt__(self,a): 
        return False
    def __ge__(self,a):
        if type(a) == type(self):
            return True
        return False
    def __str__(self):
        return "-Infinity "
    def __add__(self,a):
        return self 