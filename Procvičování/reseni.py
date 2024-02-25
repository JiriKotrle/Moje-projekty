# Inicializace prázdné knihovny
knihovna = {}

def pridej_knihu():
    nazev = input("Zadejte název knihy: ")
    autor = input("Zadejte jméno autora: ")
    rok_vydani = input("Zadejte rok vydání: ")
    dostupne_kopie = int(input("Zadejte počet dostupných kopií: "))

    knihovna[nazev] = {'autor': autor, 'rok_vydani': rok_vydani, 'dostupne_kopie': dostupne_kopie}
    print(f"Kniha '{nazev}' byla přidána do knihovny.\n")

def vypis_knihy():
    print("Seznam všech knih v knihovně:")
    for nazev, info in knihovna.items():
        print(f"Název: {nazev}")
        print(f"Autor: {info['autor']}")
        print(f"Rok vydání: {info['rok_vydani']}")
        print(f"Dostupné kopie: {info['dostupne_kopie']}")
        print("-----------------------")

def vyhledej_knihu():
    hledany_nazev = input("Zadejte název knihy k vyhledání: ")
    if hledany_nazev in knihovna:
        info = knihovna[hledany_nazev]
        print(f"Detaily knihy '{hledany_nazev}':")
        print(f"Autor: {info['autor']}")
        print(f"Rok vydání: {info['rok_vydani']}")
        print(f"Dostupné kopie: {info['dostupne_kopie']}")
    else:
        print(f"Kniha '{hledany_nazev}' nebyla nalezena v knihovně.")

def aktualizuj_kopie():
    nazev_knihy = input("Zadejte název knihy, u které chcete aktualizovat počet dostupných kopií: ")
    if nazev_knihy in knihovna:
        nove_kopie = int(input("Zadejte nový počet dostupných kopií: "))
        knihovna[nazev_knihy]['dostupne_kopie'] = nove_kopie
        print(f"Počet dostupných kopií knihy '{nazev_knihy}' byl aktualizován.\n")
    else:
        print(f"Kniha '{nazev_knihy}' nebyla nalezena v knihovně.")

def odstran_knihu():
    nazev_knihy = input("Zadejte název knihy, kterou chcete odstranit z knihovny: ")
    if nazev_knihy in knihovna:
        del knihovna[nazev_knihy]
        print(f"Kniha '{nazev_knihy}' byla odstraněna z knihovny.\n")
    else:
        print(f"Kniha '{nazev_knihy}' nebyla nalezena v knihovně.")

# Hlavní smyčka programu
while True:
    print("Vyberte operaci:")
    print("1. Přidat knihu")
    print("2. Vypsat knihy")
    print("3. Vyhledat knihu")
    print("4. Aktualizovat počet dostupných kopií")
    print("5. Odstranit knihu")
    print("6. Konec programu")

    volba = input("Zadejte číslo operace: ")

    if volba == '1':
        pridej_knihu()
    elif volba == '2':
        vypis_knihy()
    elif volba == '3':
        vyhledej_knihu()
    elif volba == '4':
        aktualizuj_kopie()
    elif volba == '5':
        odstran_knihu()
    elif volba == '6':
        print("Program končí. Děkujeme za použití.")
        break
    else:
        print("Neplatná volba. Zadejte prosím platné číslo operace.\n")
