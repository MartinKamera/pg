# Příklad 3: Práce s externími daty a výpočty
# Zadání:
# Napište funkci `convert_to_czk`, která:
# 1. Přijme částku (`amount`) jako desetinné číslo a kód měny (`currency`) jako řetězec (např. "USD", "EUR").
# 2. Stáhne aktuální kurzovní lístek z URL:
#    http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
# 3. Načte příslušný kurz podle zadaného kódu měny a provede převod zadané částky na české koruny (CZK).
# 4. Funkce vrátí výslednou částku v CZK zaokrouhlenou na dvě desetinná místa.
# Pokud zadaná měna v kurzovním lístku neexistuje, vyhoďte výjimku `ValueError`.

import requests
def convert_to_czk(amount, currency):
    # Stáhneme aktuální kurzovní lístek
    url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    response = requests.get(url)
    prevod = 0


    if response.status_code != 200:
        raise ValueError("Nepodařilo se stáhnout kurzovní lístek.")
    
    data = response.text.splitlines()

    for idx, line in enumerate(data):
        if idx >= 3:
            casti = line.split("|")
            mnozstvi = float(casti[2].strip()) 
            code = (casti[3].strip())
            kurz = (casti[4].strip())
            kurz1 = kurz.replace(",",".")
            kurz_conv = float(kurz1) 
            if code == currency:
                prevod = mnozstvi * amount * kurz_conv

    return prevod
