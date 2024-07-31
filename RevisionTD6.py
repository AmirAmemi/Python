def inverse_reel():
    try:
        x = float(input("donner x "))
        return 1/x
    except ZeroDivisionError:
        print("ne peut pas divise par 0")
    except TypeError :
        print('x doit etre une reel')




def saisir_entier():
    try:
        n=int(input("donner n"))
        if n > 100 :
            raise Exception("l'entier doit inf a 100")
        elif n < 10 :
            raise Exception ("l'entier doit etre sup a 10")
    except Exception as e :
        print(e)





def saisir_reel():
    x = input()
    L = x.split(",")
    if float(x) == True:
        return float(x)
    elif len(L)==2 :
        if int(ch[0]) and int(ch[1]):
            return float(ch[0]+'.'+ch[1])

print(saisir_reel())