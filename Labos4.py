# Labos4

from kolegij import unos_kolegija
from ispiti import unos_ispita
from student import unos_studenta, ispis_studenta

kolegiji = []
broj_kolegija = int(input("Unesite broj kolegija: "))
for i in range(broj_kolegija):
    kolegiji.append(unos_kolegija(i + 1))

# Zadatak 1 --> ispis
# print(f"Popis svih kolegija:")
# for i in range(broj_kolegija):
#    ispis_kolegija(kolegiji[i + 1])

ispiti = []
broj_ispita = int(input("Unesite broj ispita: "))
for i in range(broj_ispita):
    ispiti.append(unos_ispita(kolegiji.copy(), i + 1))

# Zadatak 2 --> ispis
# print("Popis svih ispita:")
# for i in range(broj_ispita):
#    ispis_ispita(ispiti[i + 1])

studenti = []
broj_studenata = int(input("Unesite broj studenata: "))
for i in range(broj_studenata):
    studenti.append(unos_studenta(ispiti.copy(), i + 1))

for student in studenti:
    ispis_studenta(student)
