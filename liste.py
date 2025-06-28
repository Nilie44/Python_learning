fruits = ["pomme", "banane", "orange"]

print(fruits)

#ajout de kiwi a la liste
fruits.append("kiwi")
print (fruits)

#suppression de orange
fruits.remove("orange")
print (fruits)

#modification du second élément de la liste
fruits[1] = "ananas"
print (fruits)

#longueur de la liste
longueur = len(fruits)

print (f"la longueur de la liste est: {longueur}")

#trie de la liste
fruits.sort()
print (fruits)
