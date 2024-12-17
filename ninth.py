def dec_to_bin(cislo):
    # Převést číslo na int (pokud je zadané jako řetězec)
    cislo = int(cislo)
    # Převést na binární číslo a odstranit prefix '0b'
    return bin(cislo)[2:]

def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"

if __name__ == "__main__":
    import pytest
    pytest.main()
