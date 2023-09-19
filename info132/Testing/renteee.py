def innskudd(saldo, nySaldoP):
    saldo += nySaldoP
    return saldo

def uttak(saldo, antall):
    if antall <= saldo:
        saldo -= antall
        return saldo
    else:
        return "Du har ikke nok penger på kontoen."

def beregn_rente(saldo, rentesats):
    if saldo > 1000000:
        rentesats = 0.02
    rente = saldo * rentesats
    return rente

def renteoppgjor(saldo, rentesats):
    rente = beregn_rente(saldo, rentesats)
    saldo += rente
    return saldo

saldo = 500
rentesats = 0.01

saldo = innskudd(saldo, 1000000)
saldo = uttak(saldo, 5000)
print(f"renten er {beregn_rente(saldo, rentesats)}")
saldo = renteoppgjor(saldo, rentesats)
print(saldo)
