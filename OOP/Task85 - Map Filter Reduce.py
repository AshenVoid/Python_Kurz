from functools import reduce

#Pomocí filter najděte rozlohy v rozmezí 800 až 10000
print("Pomocí filter najděte rozlohy v rozmezí 800 až 10000")
rozlohy = [88984, 345, 579875, 7594, 347985, 955, 545]

vyfiltrovane = list(filter(lambda x: 800 <= x <= 10000, rozlohy))
print(vyfiltrovane)

#Pomocí reduce vynásobte všechny prvky
print("Pomocí reduce vynásobte všechny prvky")
prvky = [4,3,6,7]

vysledek = reduce(lambda x,y: x*y, prvky)
print(vysledek)

#Pomocí reduce najděte nejdelší řetězec v listu
print("Pomocí reduce najděte nejdelší řetězec v listu")

jazyky = ["Python", "Java", "C++", "JavaScript"]
nejdelsi =  reduce(lambda x,y: x if len(x) > len(y) else y, jazyky)
print(nejdelsi)