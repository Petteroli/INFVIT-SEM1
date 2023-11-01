#oppgave4
from collections import Counter
#Fant counter på Geeksforgeeks.org og modifiserte den til å bli en egen kode
#https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/

def finn_mest_brukte_ord(setning):
    liste = setning.split()
    mestBruktOrd = Counter(liste).most_common()
    print(mestBruktOrd)

finn_mest_brukte_ord('Dette er dette en test som er enkel og grei')
    