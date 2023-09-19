dollar = float(11.62)
euro = float(10.2)
kroner = float(input("skriv et tall:" ))
konverteringD = kroner / dollar
konverteringE = kroner / euro

print(f' {kroner} norske kroner tilsvarer {konverteringE:.3f}\N{euro sign} og {konverteringD:.3f}\N{dollar sign}')