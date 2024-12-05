def nejvetsi(seznam_cisel):
    serazeno = []
    while len(seznam_cisel):
        serazeno.append(max(seznam_cisel))
        seznam_cisel.pop(seznam_cisel.index(max(seznam_cisel)))
    return serazeno


def test_nejvetsi():
    assert nejvetsi([1,5,8]) == [8,5,1]
    assert nejvetsi([8,5,9,7,5,2]) == [9,8,7,5,5,2]
    assert nejvetsi([1000,5,444,5]) == [1000,444,5,5]
    assert nejvetsi([112,152,2000,1508]) == [2000,1508,152,112]