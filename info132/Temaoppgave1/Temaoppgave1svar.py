#oppgave 1
print("Petter")
print("Aatland")
print("Oliversen")

a="Petter"
b="Aatland"
c="Oliversen"

for i in range(1):
    print(a)
    print(b)
    print(c)

#oppgave 2a
dollar = float(11.62)
euro = float(10.2)
kroner = float(input("skriv et tall:" ))
konverteringD = kroner / dollar
konverteringE = kroner / euro

print(f' {kroner} norske kroner tilsvarer {konverteringE:.3f} og {konverteringD:.3f}')

#oppgave 2b
dollar = float(11.62)
euro = float(10.2)
kroner = float(input("skriv et tall:" ))
konverteringD = kroner / dollar
konverteringE = kroner / euro

print(f' {kroner} norske kroner tilsvarer {konverteringE:.3f}\N{euro sign} og {konverteringD:.3f}\N{dollar sign}')