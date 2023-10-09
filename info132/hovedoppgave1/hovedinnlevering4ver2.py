#Oppgave 4
import random

def treTilfeldigeSifre():
    
    sifre = [random.randint(1, 9) for _ in range(3)]
    sifre.sort()
    resultat = int("".join(map(str, sifre)))

    return resultat

# Test funksjonen
print(treTilfeldigeSifre())

