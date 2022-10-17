#On écrit les commentaires comme ça

# 1 - Répéter une opération sur toutes les veleurs d'un tableau:
# "pour chaque élément i de [0, 1, 2], affiche ("valeur": i)"
for i in [0, 1, 2]:
    print("valeur :", i)
print("Fin")
# ( équivalent de [0,1,2].foreach(i=> print("valeur :", i)) )

# 2 - Les listes:

# lister des nombres dans un intervalle (range) donné:
liste = list(range(8,16));
print(liste)

# lister des nombres, à partir de 1, jusqu'à 10, de 2 en 2
listImpaire = list(range(1,10,2))
print(listImpaire)

