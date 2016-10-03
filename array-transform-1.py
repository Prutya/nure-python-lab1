class PreobrazovatelMassiva(object):
    @staticmethod
    def preobrazovat_massiv(massiv, chislo):
        srednee_arifmeticheskoye = sum(massiv) / len(massiv)
        for i in range(len(massiv)):
            if massiv[i] > chislo:
                massiv[i] = srednee_arifmeticheskoye
        return massiv

massiv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
PreobrazovatelMassiva.preobrazovat_massiv(massiv, 7)
print(massiv) # => [1, 2, 3, 4, 5, 6, 7, 5.5, 5.5, 5.5]
