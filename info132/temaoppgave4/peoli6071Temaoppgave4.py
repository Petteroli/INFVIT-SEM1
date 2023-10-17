class Bil:
    def __init__(self, merke, modell, år):
        self.merke = merke
        self.modell = modell
        self.år = år 
        self.eier = None

    def skriv_ut_info(self):
        print(f'Merke: {self.merke}, Modell: {self.modell}, år: {self.år}', end=", ")
        if self.eier:
            eier.skriv_ut_info()
    
    def alder(self, nåværende_år = 2023):
        utregning = nåværende_år - self.år
        print(utregning)

class Eier:
    def __init__(self, navn, adresse):
        self.navn = navn
        self.adresse = adresse

    def skriv_ut_info(self):
        print(f'Navn: {self.navn}, Adresse: {self.adresse}')

bil1 = Bil('Renault', 'Twizy', 2012)
bil2 = Bil('Porche','Cayenne', 2023)
eier = Eier('Olof', 'Palmeveien 12')
bil1.eier = eier


bilpark = [bil1,bil2]

def bilpark_info(bilpark):
    for bil in bilpark:
        bil.skriv_ut_info()
       
bilpark_info(bilpark)