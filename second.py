#prevede nmbstr v intervalu 0 az 100 na jeho textovou podobu
def cislo_text(cislo):
    nmbstr = str(cislo)
    cislo_cislem = int(cislo)
    if cislo_cislem > 100:
        return "Číslo je větší než sto"
    if cislo_cislem < 0:
        return "Číslo je menší než nula"    
    else:

        if cislo_cislem == 100:
            cislo_slovy = "sto"
        if cislo_cislem < 100:
            
            if (cislo_cislem >= 10 and cislo_cislem < 20):
                nactky = ["deset","jedenáct","dvanáct","třináct","čtrnáct","patnáct","šestnáct","sedmnáct","osmnáct","devatenáct"]
                cislo_slovy = nactky[int(nmbstr[1])]
            else:
                jednotky = ["nula","jedna","dva","tři","čtyři","pět","šest","sedm","osm","devět"]
                desitky = ["dvacet","třicet","čtyřicet","padesát","šedesát","sedmdesát","osmdesát","devadesát"]
                if cislo_cislem < 10:
                    cislo_slovy = jednotky[int(nmbstr[0])]
                else:
                    if (cislo_cislem%10)!=0:
                        cislo_slovy = desitky[int(nmbstr[0])-2] +" "+jednotky[int(nmbstr[1])]
                    else:
                        cislo_slovy = desitky[int(nmbstr[0])-2]
        
        return cislo_slovy
            
        
        
    

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)