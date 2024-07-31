# Exercice 1
def inverse_reel():
    while True:
        try:
            return 1/int(input("Donner un entier "))
        except ZeroDivisionError :
            print("L'entier doit etre differant de zero ")
        except ValueError :
            print("Vous avez saisir un reel n'est un entier")


# Exercice 2
def saisir_entier():
    while True :
        try:
            x = int(input("Donner un entier entre 10 et 99 \n"))
            if x < 10 :
                raise Exception("Entier trop petit : il doit etre superieur a 10")
            elif x > 100 :
                raise Exception("Entier trop grand : il doit etre inferieur a 100")
            elif not isinstance(x, int):
                raise ValueError("La valeur introduit n'est pas un entier ")
            return x
        except Exception as err:
            print(err)
        except ValueError as err:
            print(err)


# Exercice 3 
def saisir_reel():
    while True:
        try :
            return float(input("donner un reel ").replace(',', '.'))
            
        except ValueError as err :
            print(err)

# Exercice 5
def est_sous_chaine(ch1,ch2,pos=0):
    assert  isinstance(ch1, str) and  isinstance(ch2, str) ,'les chaines soit des chaine de caractere'
    assert isinstance(pos, int) , 'pos doit un entier'
    assert len(ch1) < len(ch2) , 'length de ch2 doit superieur a length ch1'
    if ch1 in ch2 :
        pos = ch2.find(ch1)
    assert 0 < pos < (len(ch2)-len(ch1)) , ' pos doit etre entre 0 et length de ch2 - length de ch1'
    return pos
print(est_sous_chaine("GHASSEN" ,"AmirGHASSENamemi"))
