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
print(je_prvocislo(1))    # False
print(je_prvocislo(2))    # True
print(je_prvocislo(3))    # True
print(je_prvocisla(100))   # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
