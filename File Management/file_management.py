
def main():
    print("Vyberte akci se souborem: ")
    print("1 - Číst soubor")
    print("2 - Přidávat k souboru")
    print("3 - Vytvořit nebo přepsat soubor")


    volba = input("Co chcete se souborem? (1/2/3): ")


    if volba not in ["1", "2", "3"]:
        print("Neplatná volba, ukončuji program.")
        quit()


    nazev_souboru = input("Zadejte název souboru včetně přípony: ")

    try:    #test try bloku pro odchycení možných errorů
        if volba == "1":
            cist_soubor(nazev_souboru)
        elif volba == "2":
            pridavat_do_souboru(nazev_souboru)
        elif volba == "3":
            prepsat_soubor(nazev_souboru)
    except FileNotFoundError:
        print(f"Soubor '{nazev_souboru}' není nalezen.")
    except Exception as e:
        print(f"Došlo k chybě: {e}")


def cist_soubor(nazev_souboru):
    with open(nazev_souboru, "r", encoding="utf-8") as soubor:
        obsah = soubor.read()
        print("Obsah souboru:")
        print(obsah)


def pridavat_do_souboru(nazev_souboru):
    text = input("Zadejte text, který chcete přidat: ")
    with open(nazev_souboru, "a", encoding="utf-8") as soubor:
        soubor.write(text + "\n")
    print("Text byl úspěšně přidán.")


def prepsat_soubor(nazev_souboru):
    text = input("Zadejte text, který chcete uložit: ")
    with open(nazev_souboru, "w", encoding="utf-8") as soubor:
        soubor.write(text + "\n")
    print("Soubor byl úspěšně přepsán.")


if __name__ == "__main__":
    main()

