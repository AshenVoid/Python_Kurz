class Zamestnanec:
    def __init__(self, jmeno, prijmeni, plat):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.plat = plat

    def pridat_plat(self, kolik_pridat):
        self.plat += kolik_pridat

    def printit(self):
        print(f"Zaměstnanec {self.jmeno} příjmením {self.prijmeni} má plat {self.plat} Kč.")

    def zmena_jmena(self, nove_jmeno):
        self.jmeno = nove_jmeno

    def zmena_prijmeni(self, nove_prijmeni):
        self.prijmeni = nove_prijmeni

petr = Zamestnanec("Petr", "Novák", 60000)
petr.pridat_plat(5000)
petr.printit() #Zaměstnanec Petr příjmením Novák má plat 65000 Kč

lenka = Zamestnanec("Lenka", "Nováková", 55000)
lenka.pridat_plat(11000)
lenka.printit()
lenka.zmena_jmena("Emma")
lenka.zmena_prijmeni("Platinová")
lenka.printit()