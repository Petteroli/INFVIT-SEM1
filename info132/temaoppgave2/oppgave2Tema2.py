#temaoppgave 2
#gjette hvor mange bokstaver som er i en setning

setning = input("skriv en setning: ")
gjetting = int(input("gjett hvor mange bokstaver som er i setningen: "))

if gjetting == len(setning):
    print("true")
else:
    print("false")
