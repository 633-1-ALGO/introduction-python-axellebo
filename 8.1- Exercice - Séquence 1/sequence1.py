# Problème : Etant donné une variable a et b, on demande de mettre la valeur de a dans b et celle de b dans a
# Contraintes : Ne pas utiliser de valeurs numériques.
# Données : les variables a et b

a = 11
b = 42

print("La valeur de a avant modification : ", a)
print("La valeur de b avant modification : ", b)
c = a
a = b
b = c
print("La valeur de a après modification : ", a)
print("La valeur de b après modification : ", b)
