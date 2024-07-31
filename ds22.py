class point :
    def __init__(self,x=0,y=0):
        if isinstance(x, point) :
            self.x , self.y = float(x.x) , float(x.y)
        else:
            self.x = float(x)
            self.y = float(y)
    def __str__(self):
        return "({:.2f},{:.2f})".format(self.x,self.y)
    def distance(self, other):
        if not isinstance(other, point):
            raise TypeError("objet n'est pas de type point")
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    def __eq__(self, other):
        if isinstance(other, point):
            return self.x == other.x and self.y == other.y
        return False
    def __lt__(self, other):
        return self.distance(point()) < other.distance(point())
    def __le__(self,other):
        return self.distance(point()) <= other.distance(point())
class Polygone :
    def __init__(self,V):
        self.__sommets = []
        if len(V) >= 3  :
            if  isinstance(V, list) :
                for i in V :
                    if isinstance(i, point) :
                        self.__sommets.append(i)
                    if isinstance(i, tuple) :
                        if len(i) == 2 : 
                            self.__sommets.append(i)
                        else :
                            ValueError(i," nest pas une point")
            else :
                raise TypeError(V," nest pas une list")
        else :
            raise ValueError(V,"contient moins de 3 points")
    def __str__(self):
        return f"{self.__sommets}"
    def to_file(self,file):
        with open(file,'w') as f :
            for i in self.__sommets :
                f.write("{},{}".format(i.x,i.y))
                f.write('\n')

    def from_file(self,file):
        with open(file) as f :
            for i in f :
                self.__sommets.append('('+str(i)+')')
    def __eq__(self,other):
        if len(self.__sommets) == len(other.__sommets) :
            for i in range(len(self.__sommets)):
                if self.__sommets[i] != other.__sommets[i] :
                    return False
            return True
        return False
    def __call__(self) :
        a = 0
        for i in range(len(self.__sommets)):
            a += point.distance(self.__sommets[i], self.__sommets[i-1])
        return a


pt1 = point()
pt2 = point(0,2)
pt3 = point(1.42,2.3)
pt4 = point(pt3)
print(pt1,pt2,pt3)
print(pt1.distance(pt2))
# print(pt1.distance([0.,2.1]))
print(pt1 == pt2 , pt3 == pt4)
print(pt1 < pt2, pt3 <= pt4)
p1 = Polygone([pt1, pt2, pt3])
p2 = Polygone([pt3, pt1, pt2])
p3 = Polygone([(1.1, 2.1), (3.3, 5.11), (4.0, 2.1)])
p4 = p1
p1.to_file("poly-01.txt")
print(p1,p2,p3, sep= '\n')
print(p1==p2,p2==p3,p3==p1,p4 == p1)
print(p1(),p2())