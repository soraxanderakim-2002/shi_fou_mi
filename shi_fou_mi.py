import random

liste=["pierre", "ciseau", "feuille"]


while True:
   
        
    ordi = random.choice(liste)
    
    shi = input("entrer votre choix parmis le element de la liste:(pierre, ciseau, feuille ) ").lower()
    
    if shi not in liste :
       print("Choix invalide. Réessayez.")
       continue  
    
    print( "votre choix : "+ shi + ". le choix de lordi : "+ ordi)
    
    if shi == ordi :
       print("egaliter !!")
    
    elif (shi == "pierre" and ordi == "ciseau") :
        print("vous avez gagner genial !!")
        continue
        
    elif (shi == "ciseau" and ordi == "feuille") :
         print("vous avez gagner genial !!")
         continue
         
    elif (shi == "feuille" and ordi == "pierre") :
         print("vous avez gagner !!! ")   
         continue
    
    else :
         print("l'ordi a gagner vous etes null !!!")
    
    random.shuffle(liste)
    print(liste)
    
    print("si vous souhaiter quitter la partie en 'q' si vous souhaiter continuer entre 'c' ")
    
    choix = input("quel choix avez vous fait : 'q' pour quitter ou 'c' pour continuer ").lower()
    
    if choix == "q":
       break
    
    elif choix == "c":
         continue
         
