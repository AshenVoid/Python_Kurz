lide = ["Ruda", "Petr", "Pavla", "Petra"]

#OG
def porovnej_delku_jmen(jmeno1, jmeno2):
    return len(jmeno1) > len(jmeno2)

#Lambda
porovnej_delku_jmen_lambda = lambda jmeno1, jmeno2: len(jmeno1) > len(jmeno2)
print(porovnej_delku_jmen_lambda(lide[2], lide[1]))

#OG
def jsou_indexy_stejne(list_polozek):
    return list_polozek[2] == list_polozek[3]

#Lambda
jsou_indexy_stejne_lambda = lambda list_polozek: list_polozek[2] == list_polozek[3]
print(jsou_indexy_stejne_lambda(lide))