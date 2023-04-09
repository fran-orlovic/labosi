
def unos_kolegija(index):
    """
    Funkcija za unos kolegija po indeksu.

    :param index:
    :return kolegij:
    """
    kolegij = {}

    kolegij['naziv'] = input(f"Unesite naziv {index}. kolegija: ")
    kolegij['ects'] = int(input(f"Unesite ECTS bodove za {index}.kolegij: "))

    return kolegij
