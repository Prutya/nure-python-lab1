class ZapolnitelMassiva(object):
    @staticmethod
    def zapolnit(massiv):
        for i in range(len(massiv)):
            massiv[i] = 0

        massiv[0] = 1
        massiv[-1] = 1
        return massiv

rezultat = ZapolnitelMassiva.zapolnit([0] * 10)
print(rezultat)
