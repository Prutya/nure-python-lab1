import math

class PryamougolnyiTreugolnik(object):
    def __init__(self, katet_a, katet_b):
        self.a = math.fabs(katet_a)
        self.b = math.fabs(katet_b)

    def vichislit_ploshad(self):
        return self.a * self.b * 0.5

    def gipotenuza(self):
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def perimetr(self):
        return self.a + self.b + self.gipotenuza()

abc = PryamougolnyiTreugolnik(-3, 4)
print('Ploshad: ' + str(abc.vichislit_ploshad()))
print('Gipotenuza C: ' + str(abc.gipotenuza()))
print('Perimetr: ' + str(abc.perimetr()))
