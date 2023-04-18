
def get_kolegij(kolegij, index):
    """
    Funkcija koja vraća indeks i naziv kolegija.
    :param index:
    :param kolegij:
    :return:
    """
    print(f"\t{index}. {kolegij.naziv}")


def ispis_svih_kolegija(kolegiji):
    for kolegij in kolegiji:
        kolegij.ispis()
