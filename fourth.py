def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ_figurky = figurka["typ"]
    pocatecni_pozice = figurka["pozice"]
    vektor = (cilova_pozice[0]-pocatecni_pozice[0], cilova_pozice[1]-pocatecni_pozice[1])
    je_vektor_legit = vektor[0] == 0 or vektor[1] == 0 or abs(vektor[0])==abs(vektor[1]) or typ_figurky == "jezdec"
    je_mozny = cilova_pozice[0]<=8 and cilova_pozice[1]<=8 and cilova_pozice[1]>=0 and cilova_pozice[0]>=0 and je_vektor_legit 
    radek_krok= (cilova_pozice[0] - pocatecni_pozice[0]) // max(abs(cilova_pozice[0] - pocatecni_pozice[0]), 1)
    sloupec_krok= (cilova_pozice[1] - pocatecni_pozice[1]) // max(abs(cilova_pozice[1] - pocatecni_pozice[1]), 1)


    
    # if (je_mozny and typ_figurky != "jezdec"):
    #     aktualni_pozice = (pocatecni_pozice[0] + radek_krok, pocatecni_pozice[1] + sloupec_krok)
    #     while aktualni_pozice != cilova_pozice:
        
    #         if aktualni_pozice in obsazene_pozice:
    #             je_mozny = False
    #             break
    #         aktualni_pozice = (aktualni_pozice[0] + radek_krok, aktualni_pozice[1] + sloupec_krok)
    
        



            
  



    return je_mozny 


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

print(je_tah_mozny(pesec, (2, 2), obsazene_pozice))  # True
print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True

"""
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
"""