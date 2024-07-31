def saisir_reel():
    while True:
        try:
            nombre = input("Entrez un nombre réel : ")
            # Remplacer la virgule par un point
            nombre = nombre.replace(",", ".")
            # Convertir en float
            nombre = float(nombre)
            return nombre
        except ValueError:
            print("La valeur saisie n'est pas un nombre réel valide. Veuillez réessayer.")
l = list(nombre)
a=saisir_reel()
print(a)
y=True
while y :
    for i in range(len(l)):
        if type(l[i]) != int :
            if l[i] != ',':
                raise Exception("vous avez lkksf")
                y = True
            else :
                y= false
