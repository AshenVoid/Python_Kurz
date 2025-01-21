from dataclasses import dataclass

@dataclass
class Polozka:
    nazev : str
    cena :  int
    na_skladu : bool
    ve_sleve : bool

    def __repr__(self):
        return f"{self.nazev} : {self.cena}Kč"

nakup = [Polozka("Banán", 30, True, False),
         Polozka("Kolo", 1000, False, False),
         Polozka("Monitor", 2300, False, True),
         Polozka("Jahoda", 40, True, True),
         Polozka("Stůl", 500, True, True),
         Polozka("Dům", 300000, True, False)
         ]

print("Položky ve slevě: ")
polozky_ve_sleve = list(filter(lambda polozka: polozka.ve_sleve, nakup))
print(polozky_ve_sleve)

print("Položky pod 50 Kč: ")
polozky_pod_50_kc = list(filter(lambda polozka: polozka.cena < 50, nakup))
print(polozky_pod_50_kc)

print("Na skladu za více než 400 Kč: ")
polozky_skladem_a_drazsi_nez_400 = list(filter(lambda polozka: polozka.na_skladu and polozka.cena > 400, nakup))
print(polozky_skladem_a_drazsi_nez_400)