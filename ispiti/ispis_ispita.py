
def get_ispit(ispit, index):
    """
    Funkcija koja vraća indeks i naziv kolegija.
    :param index:
    :param ispit:
    :return:
    """
    print(f"\t{index}. Ispit iz kolegija {ispit.kolegij.naziv}")


def ispis_svih_ispita(ispiti):
    for ispit in ispiti:
        ispit.ispis()
