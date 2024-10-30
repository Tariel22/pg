def cislo_text(cislo):
    cisla = {
        0: "nula",
        1: "jedna",
        2: "dvě",
        3: "tři",
        4: "čtyři",
        5: "pět",
        6: "šest",
        7: "sedm",
        8: "osm",
        9: "devět",
        10: "deset",
        11: "jedenáct",
        12: "dvanáct",
        13: "třináct",
        14: "čtrnáct",
        15: "patnáct",
        16: "šestnáct",
        17: "sedmnáct",
        18: "osmnáct",
        19: "devatenáct",
        20: "dvacet",
        30: "třicet",
        40: "čtyřicet",
        50: "padesát",
        60: "šedesát",
        70: "sedmdesát",
        80: "osmdesát",
        90: "devadesát",
        100: "sto"
    }

    if cislo in cisla:
        return cisla[cislo]
    elif 21 <= cislo <= 99:
        desitky = (cislo // 10) * 10
        jednotky = cislo % 10
        if jednotky == 0:
            return cisla[desitky]
        else:
            return f"{cisla[desitky]} {cisla[jednotky]}"
    else:
        return "Číslo mimo rozsah"

# Testování funkce
print(cislo_text(0))      # "nula"
print(cislo_text(1))      # "jedna"
print(cislo_text(15))     # "patnáct"
print(cislo_text(25))     # "dvacet pět"
print(cislo_text(100))    # "sto"
python second.py
