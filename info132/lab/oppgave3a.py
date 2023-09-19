fahrenheit = float(input("skriv en temp i fahrenheit: "))
konverteringF = (fahrenheit - 32) * 5/9
celcius = float(input("skriv en temp i celcius: "))
konverteringC = (celcius * 9/5) + 32
print(f'{fahrenheit}\N{degree fahrenheit} = {konverteringF:.2f}\N{degree celsius}')
print(f'{celcius}\N{degree celsius} = {konverteringC:.2f}\N{degree fahrenheit}')