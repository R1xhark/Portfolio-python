# Importujeme modul datetime pro práci s časem
import datetime

# Vytvoření třídy pro položku úkolu
class PolozkaUkolu:
    def __init__(self, nazev, datum):
        self.nazev = nazev
        self.datum = datum

# Vytvoření třídy pro seznam úkolů
class SeznamUkolu:
    def __init__(self):
        self.ukoly = []

    def pridej_ukol(self, ukol):
        self.ukoly.append(ukol)

    def vypis_ukoly(self):
        if len(self.ukoly) == 0:
            print("Seznam úkolů je prázdný.")
        else:
            print("Seznam úkolů:")
            for ukol in self.ukoly:
                print(f"Název: {ukol.nazev}")
                print(f"Datum: {ukol.datum.strftime('%d.%m.%Y')}")
                print("---")

# Vytvoření instance seznamu úkolů
seznam = SeznamUkolu()

# Přidání úkolů do seznamu
ukol1 = PolozkaUkolu("Nakoupit potraviny", datetime.datetime(2023, 6, 30))
ukol2 = PolozkaUkolu("Dokončit projekt", datetime.datetime(2023, 7, 15))
seznam.pridej_ukol(ukol1)
seznam.pridej_ukol(ukol2)

# Výpis seznamu úkolů
seznam.vypis_ukoly()
