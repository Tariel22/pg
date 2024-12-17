import sys  # Pro práci s argumenty příkazového řádku
import requests  # Pro stahování obsahu z internetu
from bs4 import BeautifulSoup  # Pro analýzu HTML obsahu

def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne obsah stránky z dané URL, zkontroluje stavový kód odpovědi,
    a najde všechny odkazy <a href="..."> v HTML kódu stránky.
    """
    try:
        # 1. Odeslání požadavku na zadanou URL
        response = requests.get(url)
        
        # 2. Kontrola stavového kódu odpovědi (200 znamená úspěch)
        if response.status_code != 200:
            raise Exception(f"Chyba: Stavový kód {response.status_code}")
        
        # 3. Analýza HTML obsahu stránky
        soup = BeautifulSoup(response.content, "html.parser")
        
        # 4. Vyhledání všech <a> tagů s atributem href a získání jejich hodnot
        hrefs = [a.get("href") for a in soup.find_all("a", href=True)]
        
        # 5. Vrácení seznamu odkazů
        return hrefs
    except Exception as e:
        # Pokud dojde k chybě, vypíše se chybová zpráva
        print(f"Chyba při zpracování URL: {e}")
        return []

if __name__ == "__main__":
    try:
        # 6. Načtení URL z příkazového řádku
        url = sys.argv[1]
        
        # 7. Zavolání funkce pro získání odkazů
        odkazy = download_url_and_get_all_hrefs(url)
        
        # 8. Vypsání odkazů jeden po druhém
        for odkaz in odkazy:
            print(odkaz)
    except Exception as e:
        # Pokud program skončí chybou, vypíše se chybová zpráva
        print(f"Program skončil chybou: {e}")
