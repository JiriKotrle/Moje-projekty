import os
from pole import rada_1, rada_2, rada_3, oddelovac

os.system('cls')

rady = [rada_1, rada_2, rada_3]

for x in rady:
    rozpad = list(x) # rozloží radu do jednotlivých znaků a ty uloží v listu
    x = '|' + '|'.join(rozpad) + '|' # mezi každý znak a na začátek a konec vloží | a vytvoří zpět string
    print(x, oddelovac, sep='\n')

tahy = []

while True:
    hrac_x = input('Číslem 1 až 9 vyber pole, kam umístíš X:')
    if hrac_x.isdigit() == False or int(hrac_x) < 1 or int(hrac_x) > 9:
        print('Špatně zadané číslo! Zkus to znovu!')
        continue
    
    if int(hrac_x) in tahy:
        print('Tento tah už je obsazený! Zkus to znovu!')
        continue

    hrac_x = int(hrac_x)  # Převedení na celé číslo
    tahy.append(hrac_x)

    if hrac_x > 0 and hrac_x <= 3:
        rada_1 = list(rada_1)
        rada_1[hrac_x - 1] = 'X'
        rada_1 = ''.join(rada_1)
    elif hrac_x > 3 and hrac_x <= 6:
        rada_2 = list(rada_2)
        rada_2[hrac_x - 4] = 'X'
        rada_2 = ''.join(rada_2)
    else:
        rada_3 = list(rada_3)
        rada_3[hrac_x - 7] = 'X'
        rada_3 = ''.join(rada_3)

    rady = [rada_1, rada_2, rada_3]
    for x in rady:
        rozpad = list(x) # rozloží radu do jednotlivých znaků a ty uloží v listu
        x = '|' + '|'.join(rozpad) + '|' # mezi každý znak a na začátek a konec vloží | a vytvoří zpět string
        print(x, oddelovac, sep='\n')

    if (sum(1 for x in rada_1 if x == 'X') == 3 or # kontrola výhry horizontálně
        sum(1 for x in rada_2 if x == 'X') == 3 or 
        sum(1 for x in rada_3 if x == 'X') == 3):
        print('Vyhrál jsi!')
        break
    
    c = False # kontrola výhry vertikálně
    for i in range(len(rada_1)): 
        if sum(1 for x in rada_1[i] if x == 'X') == 1 and sum(1 for x in rada_2[i] if x == 'X') == 1 and sum(1 for x in rada_3[i] if x == 'X') == 1:
            print('Vyhrál jsi!')
            c = True
            break
    if c == True:
        break
      
    i = 0 # předělat dle kódu výše
    if sum(1 for x in rada_1[i] if x == 'X') == 1 and sum(1 for x in rada_2[i+1] if x == 'X') == 1 and sum(1 for x in rada_3[i+2] if x == 'X') == 1:
        i += 1
        print('Vyhrál jsi!')
        break

    i = 0 # kontrola výhry diagonálně
    if sum(1 for x in rada_1[i+2] if x == 'X') == 1 and sum(1 for x in rada_2[i+1] if x == 'X') == 1 and sum(1 for x in rada_3[i] if x == 'X') == 1:
        i += 1
        print('Vyhrál jsi!')
        break

    set_tahy = set(tahy) # pokud je zahráto 9 tahů bez vítěze, tak je remíza
    if len(set_tahy) == 9:
        print('Remíza!')
        break

    while True: # musím dát další smyčku while ukončenou break, abych při špatném tahu donutil hrac_o, aby hrál znovu (bez while se to při špatném tahu hrac_o vracelo zpět k hrac_x)
        hrac_o = input('Číslem 1 až 9 vyber pole, kam umístíš O:')
        if hrac_o.isdigit() == False or int(hrac_o) < 1 or int(hrac_o) > 9:
            print('Špatně zadané číslo! Zkus to znovu!')
            continue
    
        if int(hrac_o) in tahy:
            print('Tento tah už je obsazený! Zkus to znovu!')
            continue

        hrac_o = int(hrac_o)  # Převedení na celé číslo

        if hrac_o > 0 and hrac_o <= 3:
            rada_1 = list(rada_1)
            rada_1[hrac_o - 1] = 'O'
            rada_1 = ''.join(rada_1)
        elif hrac_o > 3 and hrac_o <= 6:
            rada_2 = list(rada_2)
            rada_2[hrac_o - 4] = 'O'
            rada_2 = ''.join(rada_2)
        else:
            rada_3 = list(rada_3)
            rada_3[hrac_o - 7] = 'O'
            rada_3 = ''.join(rada_3)

        rady = [rada_1, rada_2, rada_3]
        for x in rady:
            rozpad = list(x) # rozloží každou řadu do jednotlivých znaků a ty uloží v listu
            x = '|' + '|'.join(rozpad) + '|' # mezi každý znak a na začátek a konec vloží | a vytvoří zpět string
            print(x, oddelovac, sep='\n')

        tahy.append(hrac_o)
        break

    print(tahy)
    #break
    # dodělat vyhodnocení výhry + remízy