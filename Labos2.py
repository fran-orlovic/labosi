#Labos2
from datetime import date

kolegij = {}
ispit = {}
student = {}

kolegij['naziv'] = input("Unesite ime kolegija: ")
kolegij['ECTS'] = input("Unesite broj ECTSa: ")

dan = int(input("Unesite dan ispita: "))
mjesec = int(input("Unesite mjesec ispita: " ))
godina = int(input("Unesite godinu ispita: "))

#print("Kolegij",kolegij['naziv'].upper(),"nosi",kolegij['ECTS'],"ECTS bodova") # --> Zadatak 1

ispit['datum'] = date(godina, mjesec, dan)
#print("Datum ispita je:",ispit['datum']) --> Zadatak 2

student['ime'] = input("Unesite ime studenta: ")
student['prezime'] = input("Unesite prezime studenta:")
student['ispit'] = ispit
student['kolegij'] = kolegij
# --> Zadatak 3
print("\nStudent", student['ime'].capitalize(), student['prezime'].capitalize())
print("je prijavio ispit iz kolegija", student['kolegij']['naziv'].upper())
print("koji će se održati:", student['ispit']['datum'])