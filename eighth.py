def bin_to_dec(binární_číslo):
    # Převést vstup na řetězec
    binární_číslo = str(binární_číslo)
    # Převést řetězec z binární soustavy do desítkové
    return int(binární_číslo, 2)

def testovací_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

# Testování funkce
testovací_funkce()

# Výsledek pro zadané číslo
print(bin_to_dec("10011101"))  # Mělo by vypsat 157
