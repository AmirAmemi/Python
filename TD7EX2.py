# Question 1 
def saisir_membre():
    nom = input("Entrez le nom du membre : ")
    prenom = input("Entrez le prénom du membre : ")
    adresse = input("Entrez l'adresse du membre : ")
    cpost = input("Entrez le code postal du membre : ")
    num_tele = input("Entrez le numéro de téléphone du membre : ")
    
    membre = {"Nom": nom, "Prenom": prenom, "Adresse": adresse, "Cpost": cpost, "NumTele": num_tele}
    return membre

# Question 2
from pickle import dump,load 
def enregister(membre):
    try:
        a = membre
        with open("membres.bin","wb") as file1:
            dump(a,file1)
    except IOError as err :
        print(err)
#enregister(saisir_membre())

# Question 3
def liste_membre():
    try :
        with open('membres.bin',"rb") as file :
            a=load(file)
            print(a)
    except IOError as err:
        print(err)


# Question 4      
def r_membre(nom):
    with open('membres.bin', 'rb') as fichier:
        try:
            while True:
                membre =load(fichier)
                if membre["Nom"] == nom:
                    print(membre)
        except EOFError as err:
            print(err)

# Question 5
def r_membre(Cpost):
    with open('membres.bin', 'rb') as fichier:
        try:
            while True:
                membre =load(fichier)
                if membre["Cpost"] == Cpost:
                    print(membre["Nom"],membre["Prenom"])
        except EOFError as err:
            print(err)
