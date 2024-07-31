class Fraction:
    def __init__(self,a=0,b=1):
        if type(a) != int or type(b) != int :
            raise TypeError(a,"et",b,"soinet des entiers")
        elif b <= 0 :
            raise ZeroDivisionError(b,"soit une entier strictement positif")
        self.a = a
        self.b = b
        self.__reduce()

    def __reduce(self):
        d = self.__pgcd(self.a,self.b)
        self.a //= d
        self.b //= d

    def __pgcd(self,a,b):
        while b :
            a , b = b , a % b 
        return a

    def __str__(self):
        if self.b == 1:
            return str(self.a)
        return str(self.a )+ "/" + str(self.b)

    def __repr__(self):
        return f"Fraction({self.a},{self.b})"

    def __eq__(self,other):
        if type(other) != Fraction:
            return False
        return self.a == other.a and self.b == other.b

    def __lt__(self,other):
        if type(other) != Fraction :
            raise TypeError(other,"n'est pas de type fraction")
        return self.a * other.b < self.b * other.a 

    def __add__(self,other):
        if type(other) != Fraction :
            raise TypeError(other,"n'est pas de type fraction")
        a = self.a*other.b+self.b*other.a 
        b = self.b*other.b
        return(a,b)
        
    def __sub__(self,other):
        if type(other) != Fraction :
            raise TypeError(other,"n'est pas de type fraction")
        a = self.a*other.b-self.b*other.a
        b = self.b*other.b
        return Fraction(a,b)
    def __mul__(self,other):
        if type(other) != Fraction :
            raise TypeError(other,"n'est pas de type fraction")
        a = self.a * other.a
        b = self.b * other.b
        return Fraction(a,b)
    def __truediv__(self,other):
        if type(other) != Fraction :
            raise TypeError(other,"n'est pas de type fraction")
        a = self.a * other.b
        b = self.b * other.a
        return Fraction(a, b)
    def to_int(self):
        return self.a//self.b
    def to_float(self):
        return float(self.a) / self.b
    def to_bool(self):

        return self.a != 0
    def to_complex(self):
        return complex(self.float())
    def to_round(self, n=0):
        return round(self.to_float(),n)

a = Fraction(8, 7)
b = Fraction(35, 14)
print(a,b)
