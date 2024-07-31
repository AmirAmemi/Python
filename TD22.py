# Exercice 1
# 1
class Fraction:
    def __new__(self,a,b):
        if type(a) != int or type(b) != int:
            raise TypeError(a,"et",b,"Il faut que deux entiers")
        elif b <= 0:
            raise ZeroDivisionError("Dénominateur il faut que strictement positif")
        else:
            self.numerator = a
            self.denominator = b
    def __reduce(self, a, b):
        """
        This private method normalizes the fraction to its irreducible form
        by dividing both numerator and denominator by their greatest common divisor.
        """
        def pgcd(a, b):
            while b:
                a = b
                b = a%b
            return a
        
        divisor = pgcd(a, b)
        self.numerator //= divisor
        self.denominator //= divisor
    def __str__()
d = Fraction(5,3)
print(d)
        