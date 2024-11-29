def bin_to_dec(binarni_cislo):
    num = str(binarni_cislo)
    soucet = 0

    for index, number in enumerate(num):
        exponent = len(num) - index - 1
        if number == "1":
            print(exponent)
            soucet += 2 ** exponent 


    return soucet

def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128