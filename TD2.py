class Fraction:
    def __init__(self, a=0, b=1):
        if not isinstance(a, int) or type(b) != int:
            raise TypeError("Les deux paramètres doivent être des entiers.")
        elif b <= 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être nul ou negatif.")
        self.a = a
        self.b = b
        self.__reduce()

    def __reduce(self):
        d = self.__pgcd(self.a,self.b)
        self.a //= d
        self.b //= d

    def __pgcd(self,a,b):
        while b:
            a, b = b, a % b
        return a

    def __str__(self):
        if self.b == 1:
            return str(self.a)
        return str(self.a) + "/" + str(self.b)

    def __repr__(self):
        return f"Fraction({self.a}, {self.b})"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __add__(self, other):
        if type(other) != Fraction:
            raise TypeError("Le paramètre doit être une fraction.")
        a = self.a * other.b + other.a * self.b
        b = self.b * other.b
        return Fraction(a, b)

    def __sub__(self, other):
        if type(other) != Fraction:
            raise TypeError("Le paramètre doit être une fraction.")
        a = self.a * other.b - other.a * self.b
        b = self.b * other.b
        return Fraction(a, b)

    def __mul__(self, other):
        a = self.a * other.a
        b = self.b * other.b
        return Fraction(a, b)

    def __truediv__(self, other):
        a = self.a * other.b
        b = self.b * other.a
        return Fraction(a, b)

    def to_int(self):
        return int(self.a / self.b)

    def to_float(self):
        return float(self.a) / self.b

    def to_bool(self):
        return self.a != 0

    def to_complex(self):
        return complex(self.to_float())

    def to_round(self, n=0):
        return round(self.to_float(), n)

# Question 7) Si on utilise les opérateurs de comparaison !=, >, <= et >=, 
# Python utilise les méthodes ne, gt, le, et ge respectivement. Comme nous 
# n'avons pas défini ces méthodes dans la classe Fraction, Python utilise les méthodes par défaut, 
# qui comparent les objets par leur adresse mémoire. Par conséquent, ces opérateurs ne fonctionneront pas correctement 
# avec les objets de la classe Fraction. Pour que ces opérateurs fonctionnent correctement,il faudrait définir les méthodes
#  correspondantes dans la classe Fraction.

a = Fraction(1,7)
b = Fraction(8,5)
print(a,b)
print(Fraction())
# print(Fraction("a","b"))
# print(Fraction(a,0))
print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(str(a))
print(a.to_int())
print(a.to_float())
print(a.to_bool())
print(a.to_complex())
print(a.to_round(3))


