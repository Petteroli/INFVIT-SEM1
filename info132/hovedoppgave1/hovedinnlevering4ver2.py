import random

def tre_tilfeldige_sifre():
    # Generer 3 tilfeldige sifre mellom 1 og 9
    siffer1 = random.randint(1, 9)
    siffer2 = random.randint(1, 9)
    siffer3 = random.randint(1, 9)

    # Finn største og minste siffer ved hjelp av min() og max()
    min_siffer = min(siffer1, siffer2, siffer3)
    max_siffer = max(siffer1, siffer2, siffer3)

    # Lag tallet i stigende rekkefølge
    mellomste_siffer = siffer1 + siffer2 + siffer3 - min_siffer - max_siffer

    # Konkatenere sifrene i stigende rekkefølge
    resultat = int(str(min_siffer) + str(mellomste_siffer) + str(max_siffer))

    return resultat

# Test funksjonen
print(tre_tilfeldige_sifre())
