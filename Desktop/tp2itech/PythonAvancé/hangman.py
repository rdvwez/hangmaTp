import random

mylistofwords=("crevette", "tableau", "radiateur", "soleil", "mouette", "arsenal")
mywordindex=random.randint(0, len(mylistofwords)-1)

# Tirage au sort d'un mot, il sera ensuite accessible avec : mylistofwords[mywordindex]
mot = mylistofwords[mywordindex]
save = mot

# Nombre de coups autorises
nbtries=10

# Liste des lettres trouvees
mylistofhandledletters=[]
long = 0
taille = len(mot) #taille de mot recuperé aleatoirement


# afficheur de ======================================================
def afficher(result,nbr):
     # Affiche le mot avec les lettres deja connues (et des '_" pour les lettres manquantes")
    print(result) 
             
    #   Affiche il reste nbtries   
    print("il reste {} essai{}".format(nbr,"" if nbr <= 1 else "s")) 
    

# debut du programme ===================================================  
while nbtries != 0 : # Revient a while nbtries != 0:
    lettre =  input("Choisissez une lettre : ")
    # if lettre in mot: # Si la lettre est dans le mot (if gne in blop):  
    
    if lettre in mot:
        if long == 0:
            for let in mot: 
                if lettre == let: 
                    mylistofhandledletters.append(lettre)
                    position = mot.index(lettre)
                    mot = list(mot)
                    mot[position] = "*"
                else:
                    mylistofhandledletters.append("_")  
            long =1
            
        else:
            position = mot.index(lettre)
            mylistofhandledletters[position] = lettre
            mot[position] = "*"
        resultat = "".join(mylistofhandledletters)
        # nbtries -= 1 
        # afficher(resultat,nbtries)
    
    if resultat == save:
        print("Bravo le veau !")
        nbtries =0
    else:
        
        nbtries -= 1 
        afficher(resultat,nbtries)
        