# Initialisering av saldo og rentesats
saldo = 500
rentesats = 0.01

# Funksjon for innskudd
def gjor_innskudd(antall):
    global saldo
    saldo += antall
    return saldo

# Funksjon for uttak
def gjor_uttak(antall):
    global saldo
    if antall <= saldo:
        saldo -= antall
        return saldo
    else:
        return "Du har ikke nok penger på kontoen."

# Funksjon for å beregne renten for gjeldende saldo
def beregn_rente():
    global saldo, rentesats
    if saldo > 1000000:
        rentesats = 0.02
    rente = saldo * rentesats
    return rente

# Funksjon for det årlige renteoppgjøret
def arlig_renteoppgjor():
    global saldo
    rente = beregn_rente()
    saldo += rente
    return saldo

# Eksempel på bruk:
print("Saldo etter innskudd:", gjor_innskudd(100000))
print("Saldo etter uttak:", gjor_uttak(5000))
print("Rente for gjeldende saldo:", beregn_rente())
print("Saldo etter årlig renteoppgjør:", arlig_renteoppgjor())
