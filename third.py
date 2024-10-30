def je_prvocislo(cislo):
    if cislo < 2:
        return False
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            return False
    return True
def vrat_prvocisla(maximum):
    seznam_prvocisel = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            seznam_prvocisel.append(i)
    return seznam_prvocisel
