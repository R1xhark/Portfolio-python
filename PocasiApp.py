import requests

def ziskej_pocasi(mesto):
    # Připojení k API pro získání dat o počasí
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={mesto}&appid=TVOJE_API_KLÍČ"
    response = requests.get(api_url)
    data = response.json()
    
    # Zpracování dat a výpis informací o počasí
    teplota = data["main"]["temp"] - 273.15  # Převod teploty na stupně Celsius
    vlhkost = data["main"]["humidity"]
    popis = data["weather"][0]["description"]
    
    print(f"Počasí pro {mesto}:")
    print(f"Teplota: {teplota:.1f}°C")
    print(f"Vlhkost: {vlhkost}%")
    print(f"Popis: {popis}")

# Získání uživatelem zadaného města
mesto = input("Zadejte město: ")

# Získání a výpis informací o počasí
ziskej_pocasi(mesto)
