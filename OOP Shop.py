class Polozka:
    #třída položka má atributy název a cena
    def __init__(self, nazev, cena, skladem):
        self.nazev = nazev
        self.cena = cena
        self.skladem = skladem

class Kosik:
    def __init__(self):
        self.polozky = []

    def pridat_polozku(self, polozka):
        #Přidá položku do košíku, pouze když je skladem.
        if polozka.skladem > 0:
            self.polozky.append(polozka)
            polozka.skladem -= 1 #Snížení zásob o 1
            print(f"Položka {polozka.nazev} byla přidána do košíku za {polozka.cena} Kč.")
        else:
            print(f"Položka '{polozka.nazev}' není skladem a nemůže být přidána do košíku.")

    def vypsat_polozky(self):
        #Vypíše všechny položky v košíku, jejich četnost a celkovou cenu.
        if not self.polozky:
            print("Košík je prázdný.")
            return

        print("Obsah košíku:")
        celkova_cena = 0
        pocty_polozek = {}
        # Počítání výskytů položek
        for polozka in self.polozky:
            if polozka.nazev in pocty_polozek:
                pocty_polozek[polozka.nazev]['pocet'] += 1
            else:
                pocty_polozek[polozka.nazev] = {'pocet': 1, 'cena': polozka.cena}

        # Výpis položek a celková cena
        for nazev, data in pocty_polozek.items():
            pocet = data['pocet']
            cena = data['cena']
            print(f"{pocet}x {nazev} - {pocet * cena} Kč")
            celkova_cena += pocet * cena
        print(f"Celková cena: {celkova_cena} Kč.")


maslo = Polozka("Máslo", 80, 5)
chipsy = Polozka("Chilli&Lime", 34, 1)
propiska = Polozka("Propiska", 45, 0)

Pavel = Kosik()
Pavel.pridat_polozku(maslo)
Pavel.pridat_polozku(maslo)
Pavel.pridat_polozku(chipsy)
Pavel.pridat_polozku(maslo)
Pavel.pridat_polozku(chipsy)
Pavel.pridat_polozku(propiska)

Pavel.vypsat_polozky()
maslo.cena = 40 #50% off
Pavel.vypsat_polozky()

