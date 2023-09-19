#Hovedinnlevering oppgave 3

saldo = 500
rentesats = 0.01
rente = 0

def innskudd(nySaldoP):
    global saldo
    global rentesats
    saldo += nySaldoP
    if saldo > 1000000:
        rentesats = 0.02
        print("Gratulerer, du får bonusrente!")
    beregn_rente()
    print(f'saldoen er {saldo}')

def uttak(antall):
    global saldo
    global rentesats
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
    saldo += rente
    print(f'Saldoen er {saldo}')
    return saldo

innskudd(1000000)
uttak(5000)
innskudd(5000)
beregn_rente()
renteoppgjor()

