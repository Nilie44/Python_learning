

nombre1= input("veillez entrer le premier nombre\n")

nombre2 = input("veillez entrer le deuxième\n")

#première structure conditionnelle
# isnumeric() permet de vérifier si la chaîne de caractères est un nombre
if not nombre1.isnumeric() and not nombre2.isnumeric():
    print("Erreur: les deux nombres doivent être des nombres entiers")
    raise SystemExit("Fin du programme")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

operation = input("Entrez l'opération souhaitée ['+', '-', '*' ou '/']:\n")

if operation not in ["+","-","*","/"]:
  
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    raise SystemExit("Fin du programme")

if operation == "+":
    resultat=nombre1 + nombre2
elif operation == "-":
    resultat=nombre1 - nombre2
elif operation == "*":
    resultat=nombre1*nombre2
elif operation == "/":
    #verifier que le nombre2 n'est pas nulle pour la division
    
    if nombre2 == 0:
        print("entrez un nombre différent de ZERO\n")
        raise SystemExit("Fin du programme")
    
    resultat = round(nombre1/nombre2, 2)

#affichage

print(f"le resultat de l'operétion est:{round(resultat,2)}")