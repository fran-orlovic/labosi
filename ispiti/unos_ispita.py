from datetime import date
from kolegij import get_kolegij
from utilities import unos_intervala
from .ispit import Ispit


def unos_ispita(kolegiji, index):
    """
    Funkcija za unos ispita po indeksu.

    :param index:
    :param kolegiji:
    :return ispit:
    """

    print("Popis kolegija:")
    for i, kolegij in enumerate(kolegiji, start=1):
        get_kolegij(kolegij, i)

    odabir_kolegija = unos_intervala(1, len(kolegiji))
    kolegij = kolegiji[odabir_kolegija - 1]

    dan = int(input(f"Unesite dan {index}. ispita: "))
    mjesec = int(input(f"Unesite mjesec {index}. ispita: "))
    godina = int(input(f"Unesite godinu {index}. ispita: "))

    datum = date(godina, mjesec, dan)

    ispit = Ispit(kolegij, datum)

    return ispit
