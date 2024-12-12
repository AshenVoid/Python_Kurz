
# Funkce na vykreslování plátna
def vykreslit_platno(platno):
    for radek in platno:
        print("".join(radek))

# Inicializace plátna
sirka = int(input("Zadejte šířku plátna: "))
vyska = int(input("Zadejte výšku plátna: "))
platno = [["." for _ in range(sirka)] for _ in range(vyska)]

while True:
    # Volba obrazce
    print("\nVyberte obrazec:")
    print("1 - Čtverec")
    print("2 - Obdélník")
    print("3 - Pyramida")
    print("4 - Diamant")
    print("5 - Kruh")
    volba = int(input("Vaše volba: "))

    # Parametry obrazce
    if volba == 1:
        strana = int(input("Zadejte stranu čtverce: "))
    elif volba == 2:
        a = int(input("Zadejte šířku obdélníku: "))
        b = int(input("Zadejte výšku obdélníku: "))
    elif volba == 3:
        velikost = int(input("Zadejte velikost pyramidy: "))
    elif volba == 4:
        velikost = int(input("Zadejte velikost diamantu: "))
    elif volba == 5:
        r = int(input("Zadejte poloměr kruhu: "))
    else:
        print("Neplatná volba, zkuste to znovu.")
        continue

    # Souřadnice
    x = int(input("Zadejte X souřadnici: "))
    y = int(input("Zadejte Y souřadnici: "))

    # Vykreslení obrazce
    if volba == 1:
        i = 0
        while i < strana:
            j = 0
            while j < strana:
                if 0 <= y + i < vyska and 0 <= x + j < sirka:
                    platno[y + i][x + j] = "#"
                j += 1
            i += 1
    elif volba == 2:
        i = 0
        while i < b:
            j = 0
            while j < a:
                if 0 <= y + i < vyska and 0 <= x + j < sirka:
                    platno[y + i][x + j] = "#"
                j += 1
            i += 1
    elif volba == 3:
        i = 0
        while i < velikost:
            j = -i
            while j <= i:
                if 0 <= y + i < vyska and 0 <= x + j < sirka:
                    platno[y + i][x + j] = "#"
                j += 1
            i += 1
    elif volba == 4:
        i = 0
        while i < velikost:
            j = -i
            while j <= i:
                if 0 <= y + i < vyska and 0 <= x + j < sirka:
                    platno[y + i][x + j] = "#"
                if 0 <= y - i < vyska and 0 <= x + j < sirka:
                    platno[y - i][x + j] = "#"
                j += 1
            i += 1
    elif volba == 5:
        i = -r
        while i <= r:
            j = -r
            while j <= r:
                if i**2 + j**2 <= r**2:
                    if 0 <= y + i < vyska and 0 <= x + j < sirka:
                        platno[y + i][x + j] = "#"
                j += 1
            i += 1

    # Vykreslit plátno
    vykreslit_platno(platno)

    # Další obrazec?
    dalsi = input("Chcete vykreslit další obrazec? (ano/ne): ").strip().lower()
    if dalsi != "ano":
        break
