def salaire_mensuel(salaire_annuel):
    return salaire_annuel/12
     

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel/4
   
    
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire/heures_travaillees
    

mon_salaire_annuel = float(input("entrez votre salaire annuel\n"))
mes_heures_travaillees = float(input("entrez le nombre d'heure de travail par semaine\n"))



calcul_salaire_mensuel=salaire_mensuel(mon_salaire_annuel)

calcul_salaire_hebdomadaire=salaire_hebdomadaire(mon_salaire_annuel)

calcul_salaire_horaire=salaire_horaire(calcul_salaire_hebdomadaire,mes_heures_travaillees)

#affichage
print("Votre salaire horaire est de", calcul_salaire_horaire, "euros. Votre salaire hebdomadaire est de",calcul_salaire_hebdomadaire, "euros et enfin votre salaire mensuel est de",calcul_salaire_mensuel )