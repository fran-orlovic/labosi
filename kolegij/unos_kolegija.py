from .kolegij import Kolegij


def unos_kolegija(index):
    """
    Funkcija za unos kolegija po indeksu.

    :param index:
    :return kolegij:
    """

    naziv = input(f"Unesite naziv {index}. kolegija: ")
    ects = int(input(f"Unesite ECTS bodove za {index}.kolegij: "))

    kolegij = Kolegij(naziv, ects)

    return kolegij
