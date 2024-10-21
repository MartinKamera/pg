def je_prvocislo(cislo):
    
    #Tady si převedu předanou hodnotu cislo na integer
    nmbr = int(cislo)
    
    #deklaruji proměnnou boolean, která si pamatuje zda je zadaná hodnota prvočíslo
    #jako výchozí hodnotu této proměné jsem inicioval na True, ale nedělal bych to, pokud by python povolil deklaraci bez inicializace
    trfls = True
    
    #tahle podmínka zkoumá, zda je zadanej parametr cislo rovný jedné, pokud je podmínka splněna a parametr cislo se opravdu rovná jedné, 
    #nastaví se hodnota trfls na False, program přeskočí následující blok Else a provede rovnou instrukce return trfls, 
    #která vrátí hodnotu False v tomhle případě. 
    if nmbr == 1:
        trfls = False
    
    #pokud první podmínka není splněna, vkročí program do tohoto bloku, ve kterém se postupnou inkrementací čísla i v intervalu 1 až parametr (cislo -1) snaží zjistit,
    #zda se v se onom intervalu nenachází číslo, které není jedna a zároveň dělí parametr cislo bez zbytku (viz. podmínka: if (nmbr % i == 0 and i!=1)). Pokud je tato podmínka splněna,
    #nastaví se trfls na False, provede se instrukce break, která zastaví cyklus for před dalšími iteracemi a program skočí přímo k instrukci return trfls, který opět vrátí False
    else:
        for i in range(1, nmbr):
            if (nmbr % i == 0 and i!=1):
                trfls = False
                break
            else:
                i =+ 1 
    
    #pokud v předchozím cyklu žádné číslo v intervalu od jedné nesplnilo podmínku a zároveň se parametr číslo nerovná jedné, hodnota trls zůstává True, což znamená, že instrukce return trlfs vrátí hodnotu True. 
    return trfls

def vrat_prvocisla(maximum):
    retezec = []
    for i in range(1, int(maximum ) + 1):
        if je_prvocislo(i):
            retezec.append(i)     
    return retezec

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
  