from random import randint
class Point :

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    def __str__(self):
        return "({:.2f}, {:.2f})".format(self.__x , self.__y)
        
class Polygone :
    def __init__(self, points):
        self.__sommets = points.copy()
    def __len__(self):
        return len(self.__sommets)
    def __getitem__(self, key):
        return self.__sommets[key]
    def __setitem__(self, key, val):
        self.__sommets[key] = val
n = 20
Xpts = [randint(-200, 200) for i in range(n)]
Ypts = [randint(-200, 200) for i in range(n)]
P1 = Polygone([Point(x, y) for x, y in zip(Xpts, Ypts)])
# print(P1[0])
# print(P1[1])
# for i in range(len(P1)):
#     print(P1[i])
# for p in P1:
#     print(p)
print(P1)