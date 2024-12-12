platby = [3000, 200, 18, 34444]
ICO = 3455432

for ID, platba in enumerate(platby):
    print(f"Vystavuji fakturu ID {ID} od firmy s IČO {ICO} na částku {platba}")


faktury_k_vystaveni = [
    ["Panasonic", 30000, "Martin Novotný"],
    ["Oracle", 22000, "Petr Lukoš"],
    ["Porsche", 32345, "Ivo Gira"],
    ["Siemens", 2000, "Luboš Šejk"],
]
ico = 3456785
#Vypište
#Faktura ID 0. Vystavuje firma 3456785. Faktura pro Martin Novotný na částku 30000 pro firmu Panasonic

#for ID, faktura in enumerate(faktury_k_vystaveni):
    #print(f"Faktura ID {ID}. Vystavuje firma {ico}. Faktura pro {faktury_k_vystaveni[ID][2]} na částku {faktury_k_vystaveni[ID][1]} pro firmu {faktury_k_vystaveni[ID][0]}")



for ID, f in enumerate(faktury_k_vystaveni):
    a="Faktura ID"
    b=f" {ID}."
    c=" Vystavuje"
    d=f" firma {ico}."
    e=" Faktura pro"
    f1=f" {f[2]}"
    g=" na částku"
    h=f" {f[1]}"
    i=" pro firmu"
    j=f" {f[0]}."
    print(a+b+c+d+e+f1+g+h+i+j)