#oppgave 2 hovedinnlevering

def temperaturKonvertering(grader,skala='C'):
    if skala == "C":

        fahrenheit = (grader * 9/5) + 32
        return fahrenheit
    
    elif skala == "F":

        celcius = (grader - 32) * 5/9
        return celcius
    
    else:

        fahrenheit = (grader * 9/5) + 32
        return fahrenheit

print(temperaturKonvertering(34,"C"))
print(temperaturKonvertering(93.2,"F"))    
print(temperaturKonvertering(34))