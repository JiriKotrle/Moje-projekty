import random
moznosti = ['kamen', 'nuzky', 'papir']
hrac = 'kamen'
pocitac = random.choice(moznosti)
print(pocitac)

while True:
    if pocitac == 'kamen':
        print('Nerozhodne')
    if pocitac  == 'papir':
        print('Prohral jsi')
        break
    if pocitac  == 'nuzky':
        print('Vyhral jsi')
        break