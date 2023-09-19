
saldo = 500
rentesats = 0.01
rente = 0
sisteEndringer = []

def innskudd(nySaldoP):
    global saldo
    global rentesats
    global sisteEndringer
    saldo += nySaldoP
    sisteEndringer.append(f"+{nySaldoP}")
    if saldo > 1000000:
        rentesats = 0.02
        print("Gratulerer, du får bonusrente!")
    print(f'saldoen er {saldo}')

def uttak(antall):
    global saldo
    global rentesats
    global sisteEndringer
    sisteEndringer.append(f"-{antall}")
    if antall <= saldo:
        saldo -= antall
        if saldo < 1000000:
            rentesats = 0.01
            print("Du har nå ordinær rente.")
        print(f'saldoen er {saldo}')
        return saldo
    else:
        return "Du har ikke nok penger på kontoen."

def beregn_rente():
    global saldo 
    global rentesats
    global rente
    rente = saldo * rentesats
    print(f'Renten er {rente}')
    return rente

def renteoppgjor():
    global saldo
    global rente
    global sisteEndringer
    sisteEndringer.append(f"+{rente}")
    saldo += rente
    print(f'Saldoen er {saldo}')
    return saldo

def endringer():
    global saldo
    global rente
    global sisteEndringer
    if len(sisteEndringer) > 3:
        for n in range(len(sisteEndringer) - 3):
            sisteEndringer.pop(0)
    for linje in sisteEndringer:
        print(linje)

while True:
    print("\nVelg en funksjon:")
    print("1. innskudd")
    print("2. uttak")
    print("3. beregn_rente")
    print("4. renteoppgjor")
    print("5. 3 siste endringer")
    print("0. Avslutt")

    valg = input("Skriv inn tallet til den ønskede funksjonen eller 0 for å avslutte: ")

    if valg == "1":
        innskudd(int(input("skriv hvor mye du vil legge inn: ")))
    elif valg == "2":
        uttak(int(input("skriv hvor mye du vil trekke fra: ")))
    elif valg == "3":
        beregn_rente()
    elif valg == "4":
        renteoppgjor()
    elif valg == "5":
        endringer()
    elif valg == "0":
        print("Programmet avsluttes.")
        break
    else:
        print("Ugyldig valg. Prøv igjen.")