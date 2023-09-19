# Definer funksjonene du vil inkludere i valgmenyen
def funksjon1():
    print("Dette er funksjon 1")

def funksjon2():
    print("Dette er funksjon 2")

def funksjon3():
    print("Dette er funksjon 3")

# Lag en valgmeny
while True:
    print("\nVelg en funksjon:")
    print("1. Funksjon 1")
    print("2. Funksjon 2")
    print("3. Funksjon 3")
    print("0. Avslutt")

    valg = input("Skriv inn tallet til den ønskede funksjonen eller 0 for å avslutte: ")

    if valg == "1":
        funksjon1()
    elif valg == "2":
        funksjon2()
    elif valg == "3":
        funksjon3()
    elif valg == "0":
        print("Programmet avsluttes.")
        break
    else:
        print("Ugyldig valg. Prøv igjen.")
