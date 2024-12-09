nested_list = [
    [1, 2, [3, 4, [5, 6, 5], 5], 5],
    [7, 8, [5, 9, 5, 5]],
    [10, [11, 5 ,6], 12]
]

vysledek = nested_list[0][2][2].count(5)
assert vysledek == 2, "Chybný výsledek"
print("Good job!")


jmena = ["Jura", ["Eliška"], "Katka"]
# ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]]
jmena[1].insert(1, "Ruda")
jmena.insert(2, "Božka")
#jmena.append(["Michal", "Liza"])   - Možnost i takhle
jmena.insert(4, ["Michal", "Liza"])

vsechny_jmena = ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]]
assert jmena==vsechny_jmena, f"Chyba, vyšlo {jmena}, ale mělo vyjít {vsechny_jmena} "
print("Gratuluji")




vsechny_jmena = ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]] #Tento řádek neupravujte
#pomocí příkazu .pop(index) odeberte vsechny_jmena, tak aby obsahovala pouze:
# ["Jura", ["Eliška"], "Katka"]
vsechny_jmena[1].pop(1)
vsechny_jmena.pop(2)
vsechny_jmena.pop(3) #Po odstranění hodnoty na indexu 2 se hodnota na 4. indexu mění na hodnotu na 3. indexu
#   ŘÁDKY níže neupravujte
jmena = ["Jura", ["Eliška"], "Katka"]
assert jmena==vsechny_jmena, f"Chyba, vyšlo {vsechny_jmena}, ale mělo vyjít {jmena} "
print("Gratuluji")


vsechny_jmena = ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]] #Tento řádek neupravujte
#pomocí příkazu .remove(x) odeberte vsechny_jmena, tak aby obsahovala pouze:
# ["Jura", ["Eliška"], "Katka"]

vsechny_jmena[1].remove("Ruda")
vsechny_jmena.remove("Božka")
vsechny_jmena.remove(["Michal", "Liza"])

#   ŘÁDKY níže neupravujte
jmena = ["Jura", ["Eliška"], "Katka"]
assert jmena==vsechny_jmena, f"Chyba, vyšlo {vsechny_jmena}, ale mělo vyjít {jmena} "
print("Gratuluji")






vsechny_jmena = ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]] #Tento řádek neupravujte
#pomocí příkazu .clean() promažte vnořené listy tak, aby vsechny_jmena obsahovala pouze:
# ["Jura", [], "Božka", "Katka", []]
vsechny_jmena[1].clear()
vsechny_jmena[4].clear()
#   ŘÁDKY níže neupravujte
jmena = ["Jura", [], "Božka", "Katka", []]
assert jmena==vsechny_jmena, f"Chyba, vyšlo {vsechny_jmena}, ale mělo vyjít {jmena} "
print("Gratuluji")




puvodni_list = [1,4,9,[5,2],6] #Nesahat na toto
# Použijte dva příkazy .reverse() tak ať dostanete: [6, [2, 5], 9, 4, 1]
puvodni_list.reverse()
puvodni_list[1].reverse()
#Na řádky níže nesahat
assert puvodni_list == [6, [2, 5], 9, 4, 1], f"Chyba, má vyjít [6, [2, 5], 9, 4, 1], ale vyšlo {puvodni_list}"
print("Správně!!")



sportka = [3,5,8,1] #Nesahat
#Použijte příkaz insert, sort, reverse a pop, a získejte [8, 4, 3, 1]
#sportka.pop(1)
#sportka.insert(1, 4)
#sportka.sort(reverse=True)

sportka.insert(1, 4)
sportka.sort()
sportka.reverse()
sportka.pop(1)

assert [8, 4, 3, 1] == sportka, f"Má vyjít [8, 4, 3, 1] a vyšlo {sportka}"
print("Výhra!!!!")




