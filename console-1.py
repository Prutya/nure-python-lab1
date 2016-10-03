class KonsolniyPisatel(object):
    def __init__(self, provershik):
        self.validator = provershik

    def vivesti(self, nadpis):
        if (self.validator.proverit(nadpis)):
            print(nadpis)
        else:
            print("Chto-to poshlo ne tak... Prostite.")


class KonsolniyProvershik(object):
    def proverit(self, nadpis):
        return nadpis == "Silence is golden."


# Vnedrenie zavisimosti shablon
provershik = KonsolniyProvershik()
pisatel = KonsolniyPisatel(provershik)
pisatel.vivesti("Silence is golden.")
pisatel.vivesti("Drugaya stroka.")
