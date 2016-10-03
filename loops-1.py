class KonsolnyiVivoditel(object):
    def vivesti_na_ekran(self, tekst):
        print(tekst)

    def vivesti_neskolko_raz(self, tekst, kolichestvo_raz):
        for i in range(kolichestvo_raz):
            self.vivesti_na_ekran(tekst)

printer = KonsolnyiVivoditel()
printer.vivesti_neskolko_raz("You are welcome!", 10)
