# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."
liste_mot = texte.split()
cpt = 0
texte_def = ""

for mot in liste_mot:
    if mot.__contains__("exemple"):
        cpt = cpt+1
    elif mot.__contains__("est"):
        mot = "représente"
    else:
        cpt = cpt+0
    texte_def = texte_def+mot+" "
print(texte_def)
print(cpt)

