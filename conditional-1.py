import math

class VichislitelKornya(object):
    x = 1
    y = 1

    def poluchit_koren(self):
        if (not self.proverit_if_koren_exists(self.y)):
            raise Exception()

        pod_kornem = self.x - math.sqrt(self.y)

        if (not self.proverit_if_koren_exists(pod_kornem)):
            raise Exception()

        return math.sqrt(pod_kornem)

    def proverit_if_koren_exists(self, chislo):
        return chislo > 0

    def poluchit_s_konsoli_x_y(self):
        self.x = int(input('Pozhaluista vvedite x'))
        self.y = int(input('Pozhaluista vvedite y'))


vichislitel = VichislitelKornya()
vichislitel.poluchit_s_konsoli_x_y()

print(vichislitel.poluchit_koren())
