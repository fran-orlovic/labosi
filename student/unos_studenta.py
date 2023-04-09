from ispiti import get_ispit


def unos_studenta(ispiti, index):
    """
    Funkcija za unos studenta po indeksu.

    :param ispiti:
    :param index:
    :return:
    """
    student = {}

    student['ime'] = input(f"Unesite ime {index}. studenta: ")
    student['prezime'] = input(f"Unesite prezime {index}. studenta: ")

    for i, ispit in enumerate(ispiti, start=1):
        get_ispit(ispit, i)

    odabir_ispita = int(input("Unesite ispit: "))
    student['ispit'] = ispiti[odabir_ispita - 1]

    return student
