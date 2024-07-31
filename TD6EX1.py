def inverse_reel():

    while True:
        try:
            x = int(input("saisir un entier "))
            return 1/x
        except ZeroDivisionError:
            print("ne peut pas divisier par zero")
        except ValueError :
            print("n'est pas un entier")
print(inverse_reel())

