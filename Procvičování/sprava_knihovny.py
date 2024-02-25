# Zadání: Správa knihovny

# Vytvořte program v Pythonu, který umožní správu knihovny. Každá kniha bude mít následující informace: název knihy, autor, rok vydání a počet dostupných kopií. Program by měl umožnit následující operace:

# Přidání nové knihy do knihovny. Max. kapacita knihovny je ale 10 knih.
# Výpis všech knih v knihovně se všemi informacemi.
# Vyhledání knihy podle názvu a vypsání jejích detailů (autor, rok vydání, dostupné kopie).
# Aktualizace počtu dostupných kopií knihy.
# Odstranění knihy z knihovny.
# Při implementaci použijte slovníky pro ukládání informací o knihách a využijte cykly k interaktivnímu ovládání programu uživatelem

knihovna = {}

def pridani():
    """
    Prida knihu do knihovny.
    """
    pridavat = True
    while pridavat:
        nazev = input('Zadej nazev knihy:')
        
        if nazev in knihovna != 0:
            print(f'{nazev} jiz v knihovne registrujeme!')
        else:
            autor = input('Zadej autora knihy:')
            rok = input('Zadej rok vydani knihy:')
            while True:
                kopie = input('Zadej pocet kopii knihy:')
                if kopie.isdigit() != True:
                    print('Pocet kopii musi byt cele cislo! Zadej znovu!')
                    continue
                else:
                    break

            info = {'autor': autor, 'rok': rok, 'pocet_kopii': kopie}
            knihovna[nazev] = info
        
        pokracovat = str(input('Chces pokracovat v pridavani? (ANO/ NE):').upper())
        if pokracovat == 'NE':
            pridavat = False

    print(knihovna)
    
    
def kopie_do_txt():
    """
    prekopiruje data ze slovniku knihovny do txt
    """
    klice = knihovna.keys()
    for x in klice:
        with open('knihovna_txt.txt', mode='a', encoding='utf-8') as txt:
            txt.write(f'název: {x}, ')
            txt.write(f'autor: {knihovna[x]["autor"]}, ')
            txt.write(f'rok: {knihovna[x]["rok"]}, ')
            txt.write(f'kopie: {knihovna[x]["pocet_kopii"]}\n')


def vymazani_txt():
    vymazat = input('Chcete vymazat všechna data z knihovny? (ANO/ NE):')
    if vymazat.upper() == 'ANO':
        with open('knihovna_txt.txt', mode='w', encoding='utf-8') as txt:
            txt.write('')


def vypis():
    with open('knihovna_txt.txt', mode='r', encoding='utf-8') as txt:
        print(txt.read())

def vyhledani():
    """
    vyhleda knihu dle nazvu a vrati jeji detaily
    """
    nazev = input('Zadej nazev knihy:')
   
    with open('knihovna_txt.txt', mode='r', encoding='utf-8') as txt:
        knihy = txt.readlines()

    for i in range(len(knihy)):
        if f'název: {nazev}' in knihy[i]:
            print('Nalezeno...')
            autor = knihy[i].split(',')[1]
            rok = knihy[i].split(',')[2]
            kopie = knihy[i].split(',')[3]
            print(autor + rok + kopie)
            break
        
    if f'název: {nazev}' not in knihy[i]:
        print(f'Kniha s názvem "{nazev}" nebyla nalezena.')


def vymazani_knihy():
    nazev = input('zadej nazev knihy, kterou chces vymazat:')
    
    with open('knihovna_txt.txt', mode='r', encoding='utf-8') as txt:
        knihy = txt.readlines()
    smazano = False
    for i in range(len(knihy)):
        if f'název: {nazev}' in knihy[i]:
            print(f'Mazu knihu {nazev}!')
            knihy.pop(i) # metoda .pop() odstraní z listu záznam
            smazano = True
            break
        if smazano == False:
            print(f'Kniha s názvem "{nazev}" nebyla nalezena.')

    with open('knihovna_txt.txt', mode='w', encoding='utf-8') as txt:
            txt.write('')

    with open('knihovna_txt.txt', mode='a', encoding='utf-8') as txt:
        txt.writelines(knihy)


def aktualizace_kopii():
    with open('knihovna_txt.txt', mode='r', encoding='utf-8') as txt:
        knihy = txt.readlines()
    nazev = input('zadej nazev knihy, kde chces aktualizovat:')
    
    while True:
        novy_pocet = input('zadej novy pocet kopii:')
        if novy_pocet.isdigit() != True:
            print('Pocet kopii musi byt cele cislo! Zadej znovu!')
            continue
        else:
            break

    nalezeno = False

    print(knihy)
    for i in range(len(knihy)):    
        if f'název: {nazev}' in knihy[i]:
            nalezeno = True
            # Rozděl řádek podle ': ' a aktualizuj čtvrtý prvek (počet kopií)
            rozdeleny_radek = knihy[i].split(', ')
            print(rozdeleny_radek)
            rozdeleny_radek[3] = f'kopie: {novy_pocet}\n'
            knihy[i] = ', '.join(rozdeleny_radek)
            print(f'Aktualizováno: {knihy[i]}')
            print(knihy)
            break
    if nalezeno == False:
        print('Kniha nenalezena!')
    
    with open('knihovna_txt.txt', mode='w', encoding='utf-8') as txt:
            txt.write('')
    with open('knihovna_txt.txt', mode='a', encoding='utf-8') as txt:
        txt.writelines(knihy)


#pridani()
#kopie_do_txt()
#vymazani_txt()
# vypis()
#vyhledani()
#vymazani_knihy()
aktualizace_kopii()