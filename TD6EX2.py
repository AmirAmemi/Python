def saisir_entier():
    x = int(input("donner un entier dans l'intervalle 10 .. 99  \n " ))
    if x > 99 :
        raise Exception("Entier trop grand")
    elif x < 10 :
        raise Exception("Entier trop petit")
    elif type(x) != int :
        raise ValueError()
    return x
a= True
while  a :
    try:
        y = saisir_entier()
        print("l'entier est",y)
        a = False
    except Exception as err : 
        print(err)
        a = True
    except ValueError :
        print("La valeur introduit n'est pas un entier")
        a = True