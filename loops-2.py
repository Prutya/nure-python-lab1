class Kvadrat(object):
    def __init__(self, dlina_storoni, vivoditel):
        self.dlina_storoni = dlina_storoni
        self.vivoditel = vivoditel

    def vivesti_na_ekran(self):
        self.vivoditel.vivesti(self.dlina_storoni)

class VivoditelKvadrata(object):
    def vivesti(self, dlina_storoni):
        stroka = "* " * dlina_storoni
        for i in range(dlina_storoni):
            print(stroka)

printer = VivoditelKvadrata()
kvadrat = Kvadrat(5, printer)
kvadrat.vivesti_na_ekran()
