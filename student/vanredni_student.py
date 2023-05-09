from .student import Student
from .izracun_skolarine import IzracunSkolarine


class VanredniStudent(Student, IzracunSkolarine):

    def __init__(self, ime, prezime, ispit):
        Student.__init__(self, ime, prezime, ispit)

    def izracun_skolarine(self):
        return self.ispit.kolegij.ects * 50

    def ispis(self):
        print(f"Vanredni student {self.ime} {self.prezime} je prijavio:")
        self.ispit.ispis()
        print(f"\tPotrebno je platiti {self.izracun_skolarine()} eura.")
