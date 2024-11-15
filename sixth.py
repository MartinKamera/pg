import sys
import requests


def download_url_and_get_all_hrefs(url):
    req = requests.get(url)
    
    if req.status_code != 200:
        print("Neplatné URL") 
    
    req_unicode = req.text
    hrefs = []

    i = 0
    
    while i+5 <= len(req_unicode):
        if (req_unicode[i:i+5] == "href="):
            z = i + 6
            href =[]
            while req_unicode[z] !='"':
                href.append(req_unicode[z])
                z += 1

            hrefs.append("".join(href))
            i = z
        else:
            i += 1  
    
    print(hrefs)
    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        download_url_and_get_all_hrefs(url)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")