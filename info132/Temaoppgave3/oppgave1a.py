

def multiplikasjonstabell(n=int):
    for i in range(1, n+1):
        rad = [i * j for j in range(1, n+1)]
        print(" ".join(map(str, rad)))
         

multiplikasjonstabell(3)

multiplikasjonstabell(5)