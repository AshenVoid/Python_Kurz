class Banka:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.zustatek = 0

    def vklad(self, castka):
        self.zustatek += castka
        print(f"Vloženo: {castka} Kč. Aktuální zůstatek: {self.zustatek} Kč.")

    def vyber(self, castka):
        if castka > self.zustatek:
            print("Nedostatečný zůstatek!")
        else:
            self.zustatek -= castka
            print(f"Vybráno: {castka} Kč. Aktuální zůstatek: {self.zustatek} Kč.")

    def acc_info(self):
        print(f"Jméno: {self.jmeno}, Zůstatek: {self.zustatek} Kč.")

#Vložit 20000
#Vybrat 4000
#Print zůstatek a jméno

acc = Banka("Tomáš Matonoha")
acc.vklad(20000)
acc.vyber(4000)
acc.acc_info()
acc.vyber(17000)
acc.vyber(16000)
acc.acc_info()
