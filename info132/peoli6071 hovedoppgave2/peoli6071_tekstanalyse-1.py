import os

#funksjon jeg lærte på videregående Den henter tekstfilen, bruker den i linje 82
def pathRelToFolder(filePath):
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    absFilePath = os.path.join(scriptDir, filePath)
    return absFilePath

class Tekstanalyse:
    tekst = 'ekempeltekst.txt'  # teksten som analyseres
    avsnittliste = []  # liste over normaliserte avsnitt i teksten
    ordlister = []  # liste av lister over ord som forekommer i hvert avsnitt
    ordtellinger = []  # liste av lister med ordtellinger for hvert avsnitt

    def __init__(self, tekst):
        self.tekst = tekst

    def normaliser_tekst(self, spesialtegn='.,:;!?–'):
        "Fjerner spesialtegn fra self.tekst og konverterer til små bokstaver." 
        self.tekst = self.tekst.lower()
        for spesial in spesialtegn:
            if spesial in spesialtegn:
                self.tekst = self.tekst.replace(spesial, "")
   

    def til_avsnitt(self, avsnittskille='\n\n'):
        "Deler self.tekst opp i en liste av avsnitt som lagres i self.avsnitt ."
        self.avsnittliste = self.tekst.split(avsnittskille)

       
    def lag_ordliste(self, avsnittekst):
        "Lager en liste av ord som forekommer i avsnittet."
        avsnittliste = []
        for ord in avsnittekst.split():
            if ord not in avsnittliste:
                avsnittliste.append(ord)
        return avsnittliste
  

    def tell_ordforekomster(self, ordliste, avsnittekst):
        "Lager en liste over antall forekomster av ordene i ordliste i avsnittet."
        antallOrd = []
        for ord in ordliste:
            antall = avsnittekst.split().count(ord)
            antallOrd.append(antall)
        return antallOrd
               
    def analyser_tekst(self):
        "Lager en ordliste og teller ordforekomster for hvert avsnitt i teksten."
        ordlister = []
        ordtellinger = []
        for avsnittekst in self.avsnittliste:
            ordliste = self.lag_ordliste(avsnittekst)
            ordtelling = self.tell_ordforekomster(ordliste, avsnittekst)
            ordlister.append(ordliste)
            ordtellinger.append(ordtelling)
        self.ordlister = ordlister
        self.ordtellinger = ordtellinger


    def skriv_ut(self):
        "Skriver ut analyseresultatene for hvert avsnitt på skjermen."
        counter = 0
        for i in self.avsnittliste:
            print(f'{self.avsnittliste[counter]} \n {self.ordlister[counter]} \n {self.ordtellinger[counter]}')
            print("\n")
            counter += 1

    def lagre_til_fil(self, filnavn):
        "Lagrer analyseresultatene for hvert avsnitt i en fil."
        counter = 0
        with open(filnavn, "w") as fil:
            for linje in self.avsnittliste:
                fil.write(f'Avsnitt: {counter +1} \n')
                fil.write("\t" + str(self.avsnittliste[counter]) + "\n") 
                fil.write("\t" + str(self.ordlister[counter]) + "\n")
                fil.write("\t" + str(self.ordtellinger[counter]) + "\n\n")
                counter += 1

# testkjøring
filnavn = pathRelToFolder('eksempeltekst.txt')
eksempeltekst = open(filnavn).read()
tekstanalyse = Tekstanalyse(eksempeltekst)
tekstanalyse.normaliser_tekst()
tekstanalyse.til_avsnitt()
tekstanalyse.analyser_tekst()
tekstanalyse.skriv_ut()
tekstanalyse.lag_ordliste(filnavn)
tekstanalyse.lagre_til_fil("analyse.txt")