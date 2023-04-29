from ispiti import get_ispit
from utilities import unos_intervala
from .redovni_student import RedovniStudent
from .vanredni_student import VanredniStudent


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

    print("Odaberite tip studenta: ")
    print("\t1.Redovni")
    print("\t2.Vanredni")
    odabir_tipa = unos_intervala(1, 2)
    if odabir_tipa == 1:
        broj_prijava = int(input("Unesite broj prijava na ispit: "))
        student = RedovniStudent(ime, prezime, ispit, broj_prijava)
    else:
        student = VanredniStudent(ime, prezime, ispit)

    return student
