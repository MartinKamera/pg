def sudy_lichy(cislo):
    num = int(cislo)
    sud_lich =""
    
    if num % 2 == 0:
        sud_lich = "sudý"
    else:
        sud_lich = "lichý"
    return sud_lich

def test_sudy_lichy():
    assert sudy_lichy(8) == "sudý"
    assert sudy_lichy(7) == "lichý"