import requests
from bs4 import BeautifulSoup

def scrape_website():
    # Získejte URL od uživatele
    url = input("Zadejte URL webu, který chcete prohledat: ")
    
    # Pošlete GET požadavek na zadanou URL
    response = requests.get(url)
    
    # Vytvořte objekt BeautifulSoup pro parsování HTML obsahu
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Najděte a extrahujte požadovaná data z parsovaného HTML
    # Upravte následující kód podle struktury webu, který chcete prohledávat
    
    # Příklad: Vytáhněte všechny názvy a odkazy na novinky
    articles = soup.find_all('article')
    
    for article in articles:
        title = article.find('h2').text.strip()
        link = article.find('a')['href']
        print(f"Název: {title}")
        print(f"Odkaz: {link}\n")

# Příklad použití: Prohledejte novinky na webové stránce
scrape_website()
