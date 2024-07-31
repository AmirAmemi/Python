# Question 1
def saisir_message():
    try:
        Ligne1 = input("donner la ligne 1 ")
        Ligne2 = input("donner la ligne 2 ")
        Ligne3 = input("donner la ligne 3 ")
        Ligne4 = input("donner la ligne 4 ")
        with open("message.txt","w") as file :
            file.write(Ligne1+'\n')
            file.write(Ligne2+'\n')
            file.write(Ligne3+'\n')
            file.write(Ligne4+'\n')
    except IOError as err:
        print(err)

# Question 2
def lire_message():
    try:
        with open("message.txt") as file :
            print(file.read())
    except IOError as err :
        print(err)


# Question 3
def fcopier(f1,f2):
    try:
        with open(f1) as file1,open(f2,"w") as file2:
            file2.write((file1.read()).upper())
    except IOError as err:
        print(err)

# Question 4
def ligne_plus_lounge(f):
    try:
        with open(f) as file:
            Lignes = file.readlines()
            maxligne = Lignes[0]
            for ligne in range(1,len(Lignes)):
                if len(maxligne) < len(Lignes[ligne]):
                    maxligne = Lignes[ligne]
            print(maxligne)
    except IOError as err :
        print(err)

# Question 5 
def extraction(f1,f2):
    try:
        with open(f1) as file1,open(f2,"w") as file2 :
            Lignes = file1.readlines()
            for i in range(len(Lignes)):
                if Lignes[i].startswith("e"):
                    file2.write(Lignes[i])
    except IOError as err :
        print(err)


# Question 6 
def fusion(f1,f2,frslt):
    try:
        with open(f1) as file1,open(f2) as file2,open(frslt,"w") as file3:
            Lignes1 = file1.readlines()
            Lignes2 = file2.readlines()
            a = min(len(Lignes1),len(Lignes2))
            for i in range(a):
                file3.write(Lignes1[i] + Lignes2[i])
            for i in range(a , len(Lignes1)):
                file3.write(Lignes1[i])
            for i in range(a , len(Lignes2)):
                file3.write(Lignes2[i])
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






