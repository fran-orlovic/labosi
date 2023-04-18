
class Kolegij:
    def __init__(self, naziv, ects):
        self.__naziv = naziv
        self.__ects = ects

    @property
    def ects(self):
        return self.__ects

    @ects.setter
    def ects(self, ects):
        if ects < 0:
            raise Exception("ECTS bodovi moraju biti pozitivan broj!")
        else:
            self.__ects = ects

    @property
    def naziv(self):
        return self.__naziv

    @naziv.setter
    def naziv(self, naziv):
        self.__naziv = naziv

    def ispis(self):
        print(f"Kolegij {self.naziv} nosi {self.ects} ECTS bodova")
