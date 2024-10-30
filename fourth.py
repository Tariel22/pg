def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Implementace pravidel pohybu pro různé figury zde.
    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
def je_tah_mozny(figura, start_pozice, cilova_pozice, obsazena_pole):
    x_start, y_start = start_pozice
    x_cilova, y_cilova = cilova_pozice

    # 1. Проверка, что целевая позиция не вне доски
    if not (1 <= x_cilova <= 8 and 1 <= y_cilova <= 8):
        return False

    # 2. Проверка, что целевая позиция свободна
    if cilova_pozice in obsazena_pole:
        return False

    # 3. Проверка движений в зависимости от фигуры
    if figura == 'pěšec':
        if x_start == x_cilova and (y_cilova == y_start + 1 or (y_start == 2 and y_cilova == y_start + 2)):
            return True
    elif figura == 'jezdec':
        if (abs(x_cilova - x_start) == 2 and abs(y_cilova - y_start) == 1) or (abs(x_cilova - x_start) == 1 and abs(y_cilova - y_start) == 2):
            return True
    elif figura == 'věž':
        if x_start == x_cilova or y_start == y_cilova:
            if not je_pole_obsazeno(start_pozice, cilova_pozice, obsazena_pole):
                return True
    elif figura == 'střelec':
        if abs(x_cilova - x_start) == abs(y_cilova - y_start):
            if not je_pole_obsazeno(start_pozice, cilova_pozice, obsazena_pole):
                return True
    elif figura == 'dáma':
        if (x_start == x_cilova or y_start == y_cilova or abs(x_cilova - x_start) == abs(y_cilova - y_start)):
            if not je_pole_obsazeno(start_pozice, cilova_pozice, obsazena_pole):
                return True
    elif figura == 'král':
        if abs(x_cilova - x_start) <= 1 and abs(y_cilova - y_start) <= 1:
            return True

    return False

def je_pole_obsazeno(start_pozice, cilova_pozice, obsazena_pole):
    x_start, y_start = start_pozice
    x_cilova, y_cilova = cilova_pozice

    # Вектор движения
    krok_x = 1 if x_cilova > x_start else -1 if x_cilova < x_start else 0
    krok_y = 1 if y_cilova > y_start else -1 if y_cilova < y_start else 0

    # Проходим по полям между начальной и целевой позициями
    x, y = x_start + krok_x, y_start + krok_y
    while (x, y) != (x_cilova, y_cilova):
        if (x, y) in obsazena_pole:
            return True
        x += krok_x
        y += krok_y

    return False
