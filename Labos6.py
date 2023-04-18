# Labos6

from utilities import unos_intervala
from kolegij import unos_kolegija, ispis_svih_kolegija
from ispiti import unos_ispita, ispis_svih_ispita
from student import unos_studenta, ispis_svih_studenata

running = True

kolegiji = []
ispiti = []
studenti = []

while running:
    print("---------------------")
    print("1.Unos novog kolegija")
    print("2.Unos novog ispita")
    print("3.Unos novog studenta")
    print("4.Ispis kolegija")
    print("5.Ispis ispita")
    print("6.Ispis studenta")
    print("7.Zaustavi program")
    print("---------------------")
    akcija = unos_intervala(1, 7)
    if akcija == 1:
        kolegiji.append(unos_kolegija(len(kolegiji) + 1))
    if akcija == 2:
        ispiti.append(unos_ispita(kolegiji.copy(), len(ispiti) + 1))
    if akcija == 3:
        studenti.append(unos_studenta(ispiti.copy(), len(studenti) + 1))
    if akcija == 4:
        print("Popis svih kolegija:")
        ispis_svih_kolegija(kolegiji.copy())
    if akcija == 5:
        print("Popis svih ispita:")
        ispis_svih_ispita(ispiti.copy())
    if akcija == 6:
        print("Popis svih studenata:")
        ispis_svih_studenata(studenti.copy())
    if akcija == 7:
        running = False
