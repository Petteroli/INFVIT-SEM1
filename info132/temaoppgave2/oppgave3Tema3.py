#temaoppgave 3
# Lag et program som først leser inn et tall fra tastaturet, deretter legger til et tilfeldig siffer bakerst i tallet og til slutt deler det nye tallet på det gamle.

import random 

tall1 = int(input("skriv et tall: "))
randomTall = random.randint(0, 9)
kombinering = str(tall1) + str(randomTall)
utregning = int(kombinering) / tall1 

print(f'{kombinering} / {tall1} = {utregning}')