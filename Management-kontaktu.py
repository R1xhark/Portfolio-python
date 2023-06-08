def seradit_kontakty(kontakty):
    serazene_kontakty = sorted(kontakty, key=lambda x: x['jmeno'])
    return serazene_kontakty

def pridat_kontakt(kontakty):
    jmeno = input("Zadejte jméno kontaktu: ")
    email = input("Zadejte email kontaktu: ")
    kontakt = {'jmeno': jmeno, 'email': email}
    kontakty.append(kontakt)
    print("Kontakt byl úspěšně přidán.")

def zobrazit_kontakty(kontakty):
    if not kontakty:
        print("Nebyly nalezeny žádné kontakty.")
        return
    print("Seznam kontaktů:")
    for kontakt in kontakty:
        print(kontakt['jmeno'], kontakt['email'])

def serazene_kontakty(kontakty):
    serazene_kontakty = sorted(kontakty, key=lambda x: x['jmeno'])
    return serazene_kontakty

def odstranit_kontakt(kontakty):
    jmeno = input("Zadejte jméno kontaktu, který chcete odstranit: ")
    nalezeno = False
    for kontakt in kontakty:
        if kontakt['jmeno'] == jmeno:
            kontakty.remove(kontakt)
            nalezeno = True
            break
    if nalezeno:
        print("Kontakt byl úspěšně odstraněn.")
    else:
        print("Kontakt s tímto jménem nebyl nalezen.")

def sprava_kontaktu():
    kontakty = []
    while True:
        print("\n--- Správa kontaktů ---")
        print("1. Přidat kontakt")
        print("2. Zobrazit kontakty")
        print("3. Seřadit kontakty podle jména")
        print("4. Odstranit kontakt")
        print("5. Konec")
        volba = input("Zadejte vaši volbu (1-5): ")
        
        if volba == '1':
            pridat_kontakt(kontakty)
        elif volba == '2':
            zobrazit_kontakty(kontakty)
        elif volba == '3':
            serazene_kontakty = seradit_kontakty(kontakty)
            zobrazit_kontakty(serazene_kontakty)
        elif volba == '4':
            odstranit_kontakt(kontakty)
        elif volba == '5':
            print("Ukončuji program...")
            break
        else:
            print("Neplatná volba. Zkuste to prosím znovu.")

# Spusťte program správy kontaktů
sprava_kontaktu()
