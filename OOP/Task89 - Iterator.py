class NaVelkeZnaky:
    def __init__(self, seznam):
        self.seznam = seznam
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.seznam):
            raise StopIteration
        slovo = self.seznam[self.index].capitalize()
        self.index += 1
        return slovo

for velke in NaVelkeZnaky(["alice", "bety", "cecilie", "dan", "evzen"]):
    print(velke)

    