import numpy as np
class PolyCreux:
    __data ={}
    def __init__(self, poly={}):
        if poly == {}:
            self.__data = {}
        elif isinstance(poly, dict):
            self.__data = {k: v for k, v in poly.items() if v != 0}
        elif isinstance(poly, PolyCreux):
            self.__data = poly.__data.copy()
        elif isinstance(poly, list):
            self.__data = {}
            for i, coeff in enumerate(poly):
                if coeff != 0:
                    self.__data[i] = coeff
        else:
            raise TypeError("poly n'es pas de type 'list or'dict")

    def __repr__(self):
        return f"PolyCreux({self.__data})" 
    def degree(self):
        coeffs = list(self.__data.values())
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs = coeffs[:-1]
        deg = len(coeffs) - 1
        return deg
    def ajout_monome(self,a=0):
        try :
            a = int(input("donner le coefficient de le monome"))
            b = int(input("donner le degree de le monome"))
            if a == 0 :
                pass
            elif b in self.__data.keys():
                self.__data[b] = self.__data[0] + a
            else :
                self.__data[b] = a
        except ValueError as err :
            print(err)
    def __call__(self,x):
        reslt = 0
        for i,j in self.__data.items():
            reslt += j*x**i
        return reslt
    def __add__(self,other):
        poly = {}
        for key in self.__data.keys():
            if key in other.__data.keys():
                poly[key] = self.__data[key]+other.__data[key]
            else :
                poly[key] = self.__data[key]
        for key in other.__data.keys():
            if not (key in other.__data.keys()):
                poly[key] = other.__data[key]
        return PolyCreux(poly) 
    def __mul__(self,other):
        poly = {}
        if self.__data == {} or other.__data == {} :
            return poly
        else:
            for key1 in self.__data.keys():
                for key2 in other.__data.keys():
                    poly[key1+key2] = self.__data[key1]*other.__data[key2]
        return PolyCreux(poly)
    def __pow__(self,n):
        if not isinstance(n, int) or n < 0 :
            raise ValueError("n doit etre un entier positif")
        elif n==0 :
            return {0:1}
        rslt = self.__data
        for i in range(1,n):
            rslt *= self.__data
        return rslt
    def deriv(self):
        poly = {}
        for key in self.__data.keys():
            if key != 0:
                poly[key-1] = self.__data[key]*key
        return PolyCreux(poly) 
    def __eq__(self,other):
            return self.__data == other.__data
    def __str__(self):
        if self.__data =={}:
            return str(0)
        else:
            dic = dict(sorted(self.__data.items(), reverse=True))
            b = list(dic.keys())[0]
            a = str(dic[b])+'X^'+str(b)+'+'
            c = list(dic.keys())[-1]
            if b == 0:
                return str(dic[b])
            else :
                del dic[b]
                for key in dic:
                    if key == c :
                        if dic[key] == 1 :
                            a += 'X^'+str(key)
                        else:
                            a += str(dic[key])+'X^'+str(key)
                    elif key == 1:
                        a += str(dic[key])+'X' +'+'
                    elif dic[key] == 1:
                        a += 'X^'+str(key) +'+'
                    else:
                        a +=  str(dic[key])+'X^'+str(key)+'+'
                return a
    @property
    def __item__(self,i):
        if i in range(self.__data.degree()+1):
            return self.__data[i]
        else:
            raise Exception(i,"it is more then the degree of ",self.__data)
    @__item__.setter
    def __item(self,i,v):
        if i in range(self.__data.degree()+1):
            self.__data[i] = v
        else:
            raise Exception(i,"it is more then the degree of ",self.__data)
        
    




a = PolyCreux({43:2,22:3.14,0:2.1})
b = PolyCreux({10:3,5:1,1:1})
c = PolyCreux({0:3})
d = PolyCreux()
e = PolyCreux([3,0,1,7])
print(a,b,c,d,e,a+b,a+d,a==b,a*b,a*d,a.deriv())
print("jlfhkqsdjhfksjdhfqjksdhsqkjhksjdh    = ",e(2))






