
def ispis_ispita(ispit):
    """
    Funkcija koja ispisuje informacije o ispitu.
    :param ispit:
    :return:
    """
    print(f"\t\tIspit iz kolegija {ispit['kolegij']['naziv']}, " +
          f"koji nosi {ispit['kolegij']['ects']} ECTS bodova, " +
          f"koji će se održati {ispit['datum']}")


def get_ispit(ispit, index):
    """
    Funkcija koja vraća indeks i naziv kolegija.
    :param index:
    :param ispit:
    :return:
    """
    print(f"\t{index}. Ispit iz kolegija {ispit['kolegij']['naziv']}")
