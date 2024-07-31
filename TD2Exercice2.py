class Temperature:
    def __init__(self,V=0,ttype="C"):
        V = float(V)
        if ttype == "C":
            self.V = V
        elif ttype == "K":
            self.V = V-273.15
        elif ttype == "F":
            self.V = (V-32)/1.8

        else:
            raise ValueError(ttype,"est n'est pas de type 'C','K' ou 'F'")
    
    
    def __str__(self):
            return '{:.2f} C, {:.2f} K, {:.2f} F'.format(self.V,self.kelvin,self.fahrenheit)
    @property
    def celsius(self):
        return self.V
    @celsius.setter
    def celsius(self,V):
        self.V = V
    @property
    def kelvin(self):
        return self.V+273.15
    @kelvin.setter
    def kelvin(self,V):
        self.V = V - 273.15
    @property
    def fahrenheit(self):
        return 1.8*self.V+32
    @fahrenheit.setter
    def fahrenheit(self,V):
        self.V = (V-32)/1.8

    def __eq__(self, other):
        return self.V == other.V 
    def __lt__(self, other):
        return self.V < other.V 
    def __ge__(self, other):
        retrun self.V <= other.V
t1 = Temperature()
t2 = Temperature(18.9)
t3 = Temperature(10, ttype='C')
t4 = Temperature(273.15, ttype='K')
t5 = Temperature(32 , ttype='F')

print("t1 = ",t1)
print("t2 = ",t2)
print("t3 = ",t3)
print("t4 = ",t4)
print("t5 = ",t5)

t1.celsius = 13
t2.kelvin = 333
t3.fahrenheit = 95

print(t1.fahrenheit,t2.kelvin,t3.celsius)

print(t4 == t5 ,t4 != t5, t1 == t2, t1 != t2)
print(t4<t5, t1<t2,t2>t1,t4>t5)




