import time

def print_pred_a_za(fnc):
    def nahradni_funkce(*args, **kwargs):
        print("Jdeme vykonat funkci")
        start = time.time()
        vysledek =fnc(*args, **kwargs)
        end = time.time()
        print("Job's done")
        print(f"Rozdíl mezi end a start je {(end - start):.2f} sekund")
        return vysledek
    return nahradni_funkce

@print_pred_a_za
def zadej_cislo(nasobek):
    vstup = int(input("Zadej číslo: "))
    print(f"Násobek čísla {vstup} vynásobené číslem {nasobek} je {vstup * nasobek}")

zadej_cislo(5)




















