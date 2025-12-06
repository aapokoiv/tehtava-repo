class Operaatio:
    def __init__(self, sovellus, lue_syote):
        self._sovellus = sovellus
        self._lue_syote = lue_syote
        self._edellinen = None

    def suorita(self):
        pass

    def kumoa(self):
        if self._edellinen is not None:
            self._sovellus.aseta_arvo(self._edellinen)


class Summa(Operaatio):
    def suorita(self):
        self._edellinen = self._sovellus.arvo()
        self._sovellus.plus(self._lue_syote())


class Erotus(Operaatio):
    def suorita(self):
        self._edellinen = self._sovellus.arvo()
        self._sovellus.miinus(self._lue_syote())


class Nollaus(Operaatio):
    def suorita(self):
        self._edellinen = self._sovellus.arvo()
        self._sovellus.nollaa()


class Kumoa(Operaatio):
    def __init__(self, sovellus, lue_syote, hae_edellinen_komento):
        super().__init__(sovellus, lue_syote)
        self._hae_edellinen = hae_edellinen_komento

    def suorita(self):
        komento = self._hae_edellinen()
        if komento:
            komento.kumoa()