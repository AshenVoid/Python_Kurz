import random

vyherni_cislo = random.randint(1,100)

tipovane_cislo = int(input("Tipni si na jaké číslo myslím: "))

while vyherni_cislo != tipovane_cislo:
    if tipovane_cislo < vyherni_cislo:
        print("Číslo je vyšší")
    else:
        print("Číslo je nižší")
    tipovane_cislo = int(input("Tipni si znovu: "))
print(f"Vyhráls, číslo bylo skutečně {vyherni_cislo}!")