def print_vetsi(cislo1, cislo2):
    if cislo1 > cislo2:
        print(f"Větší číslo je: {cislo1}")
    elif cislo2 > cislo1:
        print(f"Větší číslo je: {cislo2}")
    else:
        print("Obě čísla jsou stejná.")


while True:
    cislo1 = int(input("Číslo 1 pro porovnání: "))
    cislo2 = int(input("Číslo 2 pro porovnání: "))
    print_vetsi(cislo1, cislo2)

    pokracovat = input("Chcete porovnat další čísla? (ano/ne): ").strip().lower()
    if pokracovat != "ano":
        print("Konec programu.")
        break
