
nombres = input("saisisez une liste de nombres séparer par les virgules:\n")

## Séparer l'ensemble des nombres et les insérer dans une liste
liste=nombres.split(',')

#affichage de la liste
print ("Liste des nombres:",liste)

# A ce stade liste est une liste de chaînes de caractères
# Convertir chaque élément de la liste en entier
liste_entiers = []

for nombre in liste:
    nombre_entiers = int(nombre)
    liste_entiers.append(nombre_entiers)

#affichage de la liste des entiers
print ("Liste des nombres entier:",liste_entiers)

#calcule de la somme des nombres de la liste
somme = 0
for nombre in liste_entiers:
    somme = nombre + somme
    
print("somme des nombres:",somme)

#moyenne des elt de la liste

moyenne = somme / len(liste_entiers)

print("la moyenne est:",moyenne)

#affichage du nombre de nombres supérieure a la moyenne
compteur = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        compteur += 1
        
print("le nombre de nombre superieure à la moyenne est:", compteur) 