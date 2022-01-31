#liste de courses


#fonction pour afficher le menu
def affichemenu():
    print("Choisissez parmi les options suivantes :")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément à la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")


#fonction pour ajouter un element a notre liste et renvoyer la liste a la fin
def ajoute_elem_liste(elem,liste):
    if not elem in liste:
        liste.append(elem)
        print(f"L'élément {elem} a bien été ajouté à la liste.")
    else:
        print(f"L'élément {elem} est déja present dans la liste")
    
    return liste

#fonction pour retirer un element de notre liste et renvoyer la liste a la fin
def retire_elem_liste(elem,liste):
    if elem in liste:
        liste.remove(elem)
        print(f"L'élément {elem} a bien été retiré de la liste.")
    else:
        print(f"L'élément {elem} n'est pas dans la liste")
    return liste


#fonction pour afficher la liste de courses
def affiche_liste(liste):
    i=1
    if len(liste) > 0:
        for elem in liste:
            print(f"{i}. {elem}")
            i+=1 
    else:
        print("Votre liste est vide.")   


#le programme principal

liste_courses = []
while True:
     
    print("____________________________________________________________________\n")

    affichemenu()

    nombre = input("=> Votre choix : ")
    if not nombre.isdigit():
        continue
    
    nombre = int(nombre)
    if nombre == 1:
        elem = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        liste_courses = ajoute_elem_liste(elem,liste_courses)
    elif nombre == 2:
        elem = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        liste_courses = retire_elem_liste(elem,liste_courses)
    elif nombre == 3:
        print("Voici le contenu de votre liste :")
        affiche_liste(liste_courses)
    elif nombre == 4:
        if len(liste_courses) > 0:
            liste_courses.clear()
            print("Votre liste a été vidée de son contenu.")
        else:
            print("Votre liste est vide.")
    elif nombre == 5:
        print("A bientot !")
        break

        
        
    
        


