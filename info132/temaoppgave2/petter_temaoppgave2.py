#temaoppgave 1
#regne ut radius av en sirkel

import math

radius = float(input("skriv en radius: "))
sirkel = math.pi * (radius**2)

print(f'Arealet til en sirkel med radius {radius:.3f} er {sirkel:.3f}')


#temaoppgave 2
#gjette hvor mange bokstaver som er i en setning

setning = input("skriv en setning: ")
gjetting = int(input("gjett hvor mange bokstaver som er i setningen: "))

if gjetting == len(setning) - setning.count(' '):
    print("true")
else:
    print("false")


#temaoppgave 3
# Lag et program som først leser inn et tall fra tastaturet, deretter legger til et tilfeldig siffer bakerst i tallet og til slutt deler det nye tallet på det gamle.

import random 

tall1 = int(input("skriv et tall: "))
randomTall = random.randint(0, 9)
kombinering = str(tall1) + str(randomTall)
utregning = int(kombinering) / tall1 

print(f'{kombinering} / {tall1} = {utregning}')