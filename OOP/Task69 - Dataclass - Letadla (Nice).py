from dataclasses import dataclass

@dataclass
class Letadlo:
    kapacita: int
    dolet: int
    rychlost: int



@dataclass
class Zamestnanec:
    vek: int
    plat: int
    naletano: int

    def __str__(self):
        return f"Zaměstnanec ve věku {self.vek} let s platem {self.plat} Kč, který nalétal {self.naletano} hodin."

@dataclass
class Aerolinie:
    pocet_letadel: int
    pocet_zamestnancu: int
    pocet_incidentu: int

    def __str__(self):
        return f"Aerolinka má {self.pocet_letadel} letadel, {self.pocet_zamestnancu} zaměstnanců a za sebou {self.pocet_incidentu} incidentů."


boeing737 = Letadlo(250, 3500, 750)  # kapacita, dolet, rychlost
kapitan = Zamestnanec(40, 200000, 2000)  # věk, plat, nalétáno na stroji
smartwings = Aerolinie(30, 400, 1)  # počet letadel, zaměstnanců, počet incidentů

print(boeing737)
print(kapitan)
print(smartwings)


