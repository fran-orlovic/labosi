
def ispis_kolegija(kolegij):
    """
    Funkcija koja ispisuje informacije o kolegiju.
    :param kolegij:
    :return:
    """
    print(f"\tKolegij {kolegij['naziv']} " +
          f"nosi {kolegij['ects']} ECTS bodova")


def get_kolegij(kolegij, index):
    """
    Funkcija koja vraća indeks i naziv kolegija.
    :param index:
    :param kolegij:
    :return:
    """
    print(f"\t{index}. {kolegij['naziv']}")
