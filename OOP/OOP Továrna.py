

class Tovarna:
    def __init__(self, nazev):
        self.nazev = nazev
        self.workers = 0
        self.knowhow = []

    def worker_count(self, new_count):
        self.workers = new_count

    def add_HR(self):
        self.workers += 4

    def add_shift(self):
        self.workers += 30

    def exchange_knowhow(self, company):
        self.knowhow.extend(company.knowhow)
        company.knowhow = self.knowhow



rolex = Tovarna("Rolex")
rolex.worker_count(40)
rolex.add_HR()
rolex.add_shift()
rolex.add_shift()
rolex.knowhow.append("Cistota")
print(f"Továrna na {rolex.nazev} má {rolex.workers} zaměstnanců.")


ikea = Tovarna("Ikea")
ikea.add_shift()
ikea.knowhow.append("Preciznost")

rolex.exchange_knowhow(ikea)
print(rolex.knowhow)
print(ikea.knowhow)