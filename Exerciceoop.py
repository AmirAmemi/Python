class Rectangele :
    def __init__(self,a,b):
        if a > b:
            a = a + b 
            b = a - b 
            a = a - b
        self.a = a
        self.b = b
    def perimetre(self):
        return 2*(self.a+self.b)
    def surface(self):
        return self.a*self.b
class Parllelepipede(Rectangele):
    def __init__(self,a,b,c):
        Rectangele.__init__(self, a, b)
        self.c = c
    def Volume(self):
        return self.a*self.b*self.c
        

class CompteBancaire :
    def __init__(self,numeroCompte,nom,solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde
    def Versement(self,verr) : 
        return sold + verr
    def 

