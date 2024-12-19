def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    :return: True, pokud je tah možný, jinak False.
    """
    typ = figurka['typ']
    start_pozice = figurka['pozice']
    x_start, y_start = start_pozice
    x_cil, y_cil = cilova_pozice

    # Kontrola, zda cílová pozice je na šachovnici
    if not (1 <= x_cil <= 8 and 1 <= y_cil <= 8):
        return False

    # Kontrola, zda cílová pozice není obsazena
    if cilova_pozice in obsazene_pozice:
        return False

    # Logika pohybu pro různé figury
    if typ == 'pěšec':
        if x_start == x_cil and (y_cil == y_start + 1 or (y_start == 2 and y_cil == y_start + 2)):
            return True
        if abs(x_cil - x_start) == 1 and y_cil == y_start + 1 and cilova_pozice in obsazene_pozice:
            return True
    elif typ == 'jezdec':
        if (abs(x_cil - x_start), abs(y_cil - y_start)) in [(2, 1), (1, 2)]:
            return True
    elif typ == 'věž':
        if x_start == x_cil or y_start == y_cil:
            if not je_pole_obsazeno(start_pozice, cilova_pozice, obsazene_pozice):
                return True
    elif typ == 'střelec':
        if abs(x_cil - x_start) == abs(y_cil - y_start):
            if not je_pole_obsazeno(start_pozice, cilova_pozice, obsazene_pozice):
                return True
    elif typ == 'dáma':
        if (x_start == x_cil or y_start == y_cil or abs(x_cil - x_start) == abs(y_cil - y_start)):
            if not je_pole_obsazeno(start_pozice, cilova_pozice, obsazene_pozice):
                return True
    elif typ == 'král':
        if abs(x_cil - x_start) <= 1 and abs(y_cil - y_start) <= 1:
            return True

    return False


def je_pole_obsazeno(start_pozice, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda jsou všechna pole mezi startovní a cílovou pozicí volná.
    """
    x_start, y_start = start_pozice
    x_cil, y_cil = cilova_pozice

    krok_x = (x_cil - x_start) // max(1, abs(x_cil - x_start))
    krok_y = (y_cil - y_start) // max(1, abs(y_cil - y_start))

    x, y = x_start + krok_x, y_start + krok_y
    while (x, y) != (x_cil, y_cil):
        if (x, y) in obsazene_pozice:
            return True
        x += krok_x
        y += krok_y

    return False
