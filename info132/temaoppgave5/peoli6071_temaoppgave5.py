#oppgave 1a
def telle_bokstaver(ord, bokstav):
        telle =  ord.count(bokstav)
        print(telle)
        
telle_bokstaver('hallo hallo', 'l')

#oppgave 1b
def telle_ord(setning):
    liste = setning.split()
    print(len(liste))
    
telle_ord('Python er gøy')

#oppgave2
def erstatte_bokstav(setning,finnBokstav,erstattBokstav):
    erstatt = setning.replace(finnBokstav,erstattBokstav)
    print(erstatt)

erstatte_bokstav('banan','a','o')

#oppgave3a
def formater_navnA(fornavn,etternavn):
    print(f'{etternavn},{fornavn}')

formater_navnA('Petter', 'Oliversen')

#oppgave3b
def formater_navnB(fornavn,etternavn,mellomnavn = None):
    if mellomnavn != None:
       kombinering = str(fornavn) + " " + str(mellomnavn)
       print(f'{etternavn}, {kombinering}')
    else:
        print(f'{etternavn},{fornavn}')

formater_navnB('Petter', 'Oliversen', 'Aatland')
formater_navnB('Petter', 'Oliversen')

#oppgave4
from collections import Counter
#Fant counter på Geeksforgeeks.org
#https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/

def finn_mest_brukte_ord(setning):
    liste = setning.split()
    mestBruktOrd = Counter(liste).most_common(1)
    print(mestBruktOrd)

finn_mest_brukte_ord('Dette er dette en test som er enkel og grei')