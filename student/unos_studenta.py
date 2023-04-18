from ispiti import get_ispit
from utilities import unos_intervala
from .student import Student


def unos_studenta(ispiti, index):
    """
    Funkcija za unos studenta po indeksu.

    :param ispiti:
    :param index:
    :return:
    """

    ime = input(f"Unesite ime {index}. studenta: ")
    prezime = input(f"Unesite prezime {index}. studenta: ")
    print("Odaberite ispit:")
    for i, ispit in enumerate(ispiti, start=1):
        get_ispit(ispit, i)

    odabir_ispita = unos_intervala(1, len(ispiti))
    ispit = ispiti[odabir_ispita - 1]

    student = Student(ime, prezime, ispit)

    return student
