#oppgave3b
def formater_navnB(fornavn,etternavn,mellomnavn = None):
    if mellomnavn != None:
       kombinering = str(fornavn) + " " + str(mellomnavn)
       print(f'{etternavn}, {kombinering}')
    else:
        print(f'{etternavn},{fornavn}')

formater_navnB('Petter', 'Oliversen', 'Aatland')
formater_navnB('Petter', 'Oliversen')