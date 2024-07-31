class Polycreux :
    __data = {}
    def __init__(self,poly = {}):
        if isinstance(poly, {}):
            self.__data = {}
        elif isinstance(poly, dict) :
            self.__data = {K: v for k,v in poly.items() if v}
        elif isinstance(poly, Polycreux):
            self.__data = poly.__data.copy()
        elif isinstance(poly, list):
            self.__data = {i: poly[i] for i in range(len(poly)-1) if poly[i] }
        else :
            raise TypeError("Poly ne peu pas etre de type list , dict o polycrreux")
    def __repr__(self):
        return "Polycreux({})".format(self.__data)
    def degree(self):
        return max(self.__data.keys() if self.data else None)
    def ajout_monome(self,monome = {}):
        if not monome:
            
            while True :
                try:
                    coeff = float(input("Doner l coefficient de monome : "))
                    exp = int(input("Doner l exp de monome  : "))
                    if coeff != 0  and exp >=0:
                        break
                except ValueError :
                    pass
            self.__data.update({exp: coeff})
        else :
            self.__data.update({k: v for k,v in monome.items() if v})

    def __call__(self,val):
        return sum([v*val**k for k,v in self.__data.items()])
    def __str__(self,other):
        str_ply=''
        poly = list(self.__data.items())
        poly.sort(reverse=True)
        for i, ci in poly:
            if ci == 1 :
                if i == 0 :
                    str_ply += '+ 1'
                else :
                    str_ply += '+ X'
            elif ci > 0 :
                str_ply += '+' + str(ci) + 'X'
            elif ci == -1 :
                if i == 0 :
                    str_ply += '-1'
                else :
                    dstr_ply += '-X'
            else :
                str_ply += str(ci) + 'X'
            if i == 0:
                str_ply = str_ply[:-1]
            elif i > 1 :
                str_ply += '^' + str(i)
            if str_ply[0] == '+':
                str_ply = str_ply[1:]
            
        return str_ply
