from ispiti import ispis_ispita


def ispis_studenta(student):
    """
    Funkcija koja ispisuje informacije o studentu.
    :param student:
    :return:
    """
    print(f"\tStudent {student['ime']} {student['prezime']} je prijavio:")
    ispis_ispita(student['ispit'])
