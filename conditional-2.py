class ProvershikChisla(object):
    chislo = 0

    def __init__(self, chislo):
        self.chislo = chislo

    def proverit(self):
        if (self.chislo < 7):
            return "Yes"
        elif (self.chislo > 10):
            return "No"
        elif (self.chislo == 9):
            return "Error"
        else:
            return "Nepravilnoe chislo!!!"

chisla = [1, 7, 9, 10, 11]

for i in chisla:
    checker = ProvershikChisla(i)
    print(checker.proverit())
