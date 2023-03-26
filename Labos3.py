#Labos3
from datetime import date
# Zadatak 1
kolegiji = []
broj_kolegija = int(input("Unesite broj kolegija:"))
for i in range(broj_kolegija):
    kolegij = {}
    j = i+1
    kolegij['ime'] = input("Unesite ime kolegija:")
    kolegij['ects'] = int(input(f"Unesite ECTS bodove za {j}.kolegij:"))
    kolegiji.append(kolegij)
# Zadatak 1 --> ispis
#print("Popis svih kolegija:")
#for kolegij in kolegiji:
#    print(f"\tKolegij {kolegij['ime']} nosi {kolegij['ects']} ECTS bodova")

#Zadatak 2
ispiti = []
broj_ispita = int(input("Unesite broj ispita:"))
for i in range(broj_ispita):
    ispit = {}
    print("Popis kolegija:")
    for index, kolegij in enumerate(kolegiji, start=1):
        print(f"\t{index}.{kolegij['ime']}")
    num = int(input("Unesite kolegij:"))
    dan = int(input("Unesite dan ispita: "))
    mjesec = int(input("Unesite mjesec ispita: "))
    godina = int(input("Unesite godinu ispita: "))
    ispit['datum'] = date(godina, mjesec, dan)
    ispit['kolegij'] = kolegiji[num-1]
    ispiti.append(ispit)
# Zadatak 2 --> ispis
#print("Popis svih ispita:")
#for ispit in ispiti:
#    print(f"\tIspit iz kolegija {ispit['kolegij']['ime']}," +
#          f"koji nosi {ispit['kolegij']['ects']} ECTS bodova,"+
#          f"održat će se {ispit['datum']}")

studenti = []
broj_studenata = int(input("Unesite broj studenata:"))
for i in range(broj_studenata):
    student = {}
    student['ime'] = input("Unesite ime studenta:")
    student['prezime'] = input("Unesite prezime studenta:")
    for index, ispit in enumerate(ispiti, start=1):
        print(f"\t{index}. Ispit iz kolegija {ispit['kolegij']['ime']}")
    num = int(input("Unesite kolegij:"))
    student['ispit'] = ispiti[num-1]
    studenti.append(student)
# Zadatak 3 --> ispis
print("Popis svih studenata:")
for student in studenti:
    print(f"\tStudent {student['ime']} {student['prezime']} je prijavio:" +
          f"\n\tIspit iz kolegija {student['ispit']['kolegij']['ime']} "+
          f"koji će se održati {student['ispit']['datum']}")