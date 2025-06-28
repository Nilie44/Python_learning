#creation du dictionnaire
fruits = {"pomme":"rouge","banane":"jaune","orange":"orange"}

print(fruits)

#ajoute kiwi au dict
fruits["kiwi"] = "vert"
print(fruits)

#Accédez à la valeur correspondant à la clé  banane  et stockez-la dans une variable appelée  couleur_banane  .
couleur_banane = fruits["banane"]
print(couleur_banane)

#Modifiez la valeur associée à la clé  pomme  pour  vert  
fruits["pomme"] = "vert"
print(fruits)

#Supprimez la clé  banane  du dictionnaire  fruits
del fruits["banane"]
print(fruits)

#affichage des clés restantes
cle_restantes = fruits.keys()
print(cle_restantes)