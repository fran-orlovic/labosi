from abc import ABC, abstractmethod


class Student(ABC):
    def __init__(self, ime, prezime, ispit):
        self._ime = ime
        self._prezime = prezime
        self._ispit = ispit

    @property
    def ime(self):
        return self._ime

    @ime.setter
    def ime(self, ime):
        self._ime = ime

    @property
    def prezime(self):
        return self._prezime

    @prezime.setter
    def prezime(self, prezime):
        self._prezime = prezime

    @property
    def ispit(self):
        return self._ispit

    @ispit.setter
    def ispit(self, ispit):
        self._ispit = ispit

    @abstractmethod
    def ispis(self):
        pass
