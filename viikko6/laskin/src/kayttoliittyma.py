from enum import Enum
from tkinter import StringVar, constants, ttk

from operaatiot import Erotus, Kumoa, Nollaus, Summa


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._edellinen_komento = None

        self._komennot = {
            Komento.SUMMA: lambda: Summa(self._sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: lambda: Erotus(self._sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: lambda: Nollaus(self._sovelluslogiikka, self._lue_syote),
            Komento.KUMOA: lambda: Kumoa(
                self._sovelluslogiikka,
                self._lue_syote,
                lambda: self._edellinen_komento
            )
}

    def _lue_syote(self):
        try:
            return int(self._syote_kentta.get())
        except:
            return 0

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)


        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)


    def _suorita(self, komento_nimi):
        komento = self._komennot[komento_nimi]()

        komento.suorita()

        if komento_nimi != Komento.KUMOA:
            self._edellinen_komento = komento
            self._kumoa_painike["state"] = constants.NORMAL
        else:
            self._kumoa_painike["state"] = constants.DISABLED

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta.delete(0, constants.END)
