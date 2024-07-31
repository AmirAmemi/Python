# Exercice 1 
# Question 1
def saisir_message():
    L1 = input("donner la ligne 1 ")
    L2 = input("donner la ligne 2 ")
    L3 = input("donner la ligne 3 ")
    L4 = input("donner la ligne 4 ")
    try:
        with open("message.txt",mode="w") as File :
            File.write(L1 +"\n")
            File.write(L2 +"\n")
            File.write(L3 +"\n")
            File.write(L4 +"\n")
    except IOError as err:
        print(err)

# Question 2 
def lire_message():
    try:
        with open("message.txt","r") as file:
            file.read()
    except IOError as err:
        print(err)

# Question 3 
def fcopie(f1,f2):
    try:
        with open(f1,"r") as file1,open(f2,"w") as file2 :
            file2.write(file1.read().upper())
    except IOError as err:
        print(err)
saisir_message()


# Question 4
def ligne_plus_longue(f):
    try:
        with open(f,mode="r") as file :
            Lignes = file.readlines()
            Lmax = Lignes[0]
            for i in range(1,len(Lignes)): 
                if len(Lignes[i]) > len(Lmax) :
                    Lmax = Lignes[i]
            print(Lmax) 
    except IOError as err :
        print((err))


# Question 5
def extraction(f1,f2):
    try:
        with open(f1,"r") as file1,open(f2,"w") as file2 :
            Lignes = file1.readlines()
            for i in range(1,len(Lignes)): 
                if Lignes[i].startswith("e"):
                    file2.write(Lignes[i])
    except IOError as err:
        print(err)


# Question 6
def fusion(f1,f2,fresultat):
    try:
        with open(f1,"r") as file1, open(f2,"r") as file2, open(fresultat,"w") as filefinal :
            Lignes1 = file1.readlines()
            Lignes2 = file2.readlines()
            minf = min(len(Lignes1),len(Lignes2))
            for i in range(minf):
                filefinal.write(Lignes1[i] + Lignes2[i] )
            for i in range(minf,len(Lignes1)):
                filefinal.write(Lignes1[i])
            for i in range(minf,len(Lignes2)):
                filefinal.write(Lignes2[i])

    except IOError as err:
        print(err)


# Question 7
def format_file(f1,f2):
    try:
        with open(f1,"r") as file1, open(f2,"w") as file2 :

            for ligne in file1:
                for i in range(0,len(ligne),30):
                    if i > len(ligne) - 31 :
                        file2.write(ligne[i:i+30])
                    else :
                        file2.write(ligne[i:i+30] + '\n')
    except IOError as err:
        print(err)
format_file("castello.txt","Hello.txt")

# Exercice 2 

# Question 1 
def saisir_membre():
    membre = dict()
    membre['Nom'] = input('donner le nom du membre')
    membre['PreNom'] = input('donner le PreNom du membre')
    membre['Cpost'] = input('donner le Cpost du membre')
    membre['Numtele'] = input('donner le Numtele du membre')
    return membre

# Question 2
from pickle import dump,load
def enregistrer_membre():
    newm = saisir_membre()
    try: 
        with open('membre.bin','ab') as file :
            dump(newm, file)

    except IOError as err :
        print(err)

# Question 3
def liste_membre():
    try:
        with open('membre.bin','rb') as file :
            while True :
                try :
                    membre = load(file)
                    print(membre)
                except EOFError :
                    pass
    except IOError as err:
        print(err)
liste_membre()