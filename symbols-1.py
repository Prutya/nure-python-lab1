import string

class BukvoVivoditel(object):
    def __init__(self):
        self.alfavit = string.ascii_lowercase

    def schitat_iz_konsoli(self):
        vvod = input("Vvedite bukvu: ").lower()
        try:
            self.index = self.alfavit.index(vvod)
        except ValueError:
            pass

    def vivesti_sleduyushie_tri_bukvi(self):
        rezultat = ""
        for i in range(1, 4):
            novyi_index = (self.index + i) % len(self.alfavit)
            rezultat += self.alfavit[novyi_index]
        print(rezultat)


printer = BukvoVivoditel()
printer.schitat_iz_konsoli()
printer.vivesti_sleduyushie_tri_bukvi()
