def cislo_text(cislo):
    # Převeď číslo na řetězec
    cislo = str(cislo)

    # Složky pro textové reprezentace čísel
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desítky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    speciální_desítky = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    
    # Pokud je číslo nula
    if cislo == "0":
        return jednotky[0]

    # Převod na text
    if len(cislo) == 1:  # Jednociferná čísla
        return jednotky[int(cislo)]
    
    elif len(cislo) == 2:  # Dvouciferná čísla
        if 10 <= int(cislo) < 20:  # Speciální desítky
            return speciální_desítky[int(cislo) - 10]
        else:
            desítka = desítky[int(cislo[0])]
            jednotka = jednotky[int(cislo[1])] if cislo[1] != '0' else ""
            return desítka + (" " + jednotka if jednotka else "")
    
    elif len(cislo) == 3:  # Třeciferná čísla
        stovka = "sto" if cislo[0] == '1' else jednotky[int(cislo[0])] + " sta"
        dvouciferné = cislo[1:]
        return stovka + (" " + cislo_text(dvouciferné) if int(dvouciferné) > 0 else "")
    
    return "Číslo mimo rozsah"

# Příklad použití funkce
if __name__ == "__main__":
    for i in range(101):
        print(f"{i} -> {cislo_text(i)}")
