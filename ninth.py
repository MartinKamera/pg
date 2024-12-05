def dec_to_bin(cislo):
    num = int(cislo)
    binar = []
    mocnina = 0
    if num == 0:
        binar = ["0"]
    else:
        while 2 ** mocnina < num:
            mocnina += 1 
        i = mocnina
        for mocnina in range(mocnina, -1, -1):
            if num >= 2 ** mocnina :
                binar.append("1")
                num -= 2 ** mocnina
            elif num < 2 ** mocnina and mocnina != i:
                binar.append("0")
    return "".join(binar)


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"