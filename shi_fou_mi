import random

liste=["pierre", "ciseau", "feuille"]


while True:
   
        
    ordi = random.choice(liste)
    
    shi = input("entrer votre choix parmis le element de la liste:(pierre, ciseau, feuille ) ").lower()
    
    if shi not in liste :
       print("Choix invalide. Réessayez.")
       continue  
    
    print(shi, ordi)
    
    if shi == ordi :
       print("egaliter !!")
    
    elif (shi.lower() == "pierre" and ordi.lower() == "ciseau") :
        print("vous avez gagner genial !!")
        continue
        
    elif (shi.lower() == "ciseau" and ordi.lower() == "feuille") :
         print("vous avez gagner genial !!")
         continue
         
    elif (shi.lower() == "feuille" and ordi.lower() == "pierre") :
         print("vous avez gagner !!! ")   
         continue
    
    else :
         print("l'ordi a gagner vous etes null !!!")
    
    random.shuffle(liste)
    print(liste)
    
    print("si vous souhaiter quitter la partie en 'q' si vous souhaiter continuer entre 'c' ")
    
    choix = input("quel choix avez vous fait : 'q' pour quitter ou 'c' pour continuer ").lower()
    
    if choix.lower() == "q":
       break
    
    elif choix.lower() == "c":
         continue
        
