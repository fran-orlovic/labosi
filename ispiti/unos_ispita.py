from datetime import date
from kolegij import get_kolegij
from utilities import unos_intervala


def unos_ispita(kolegiji, index):
    """
    Funkcija za unos ispita po indeksu.

    :param index:
    :param kolegiji:
    :return ispit:
    """
    ispit = {}
    print("Popis kolegija:")
    for i, kolegij in enumerate(kolegiji, start=1):
        get_kolegij(kolegij, i)
    odabir_kolegija = unos_intervala(1, i)
    ispit['kolegij'] = kolegiji[odabir_kolegija - 1]
    dan = int(input(f"Unesite dan {index}. ispita: "))
    mjesec = int(input(f"Unesite mjesec {index}. ispita: "))
    godina = int(input(f"Unesite godinu {index}. ispita: "))
    ispit['datum'] = date(godina, mjesec, dan)

    return ispit
