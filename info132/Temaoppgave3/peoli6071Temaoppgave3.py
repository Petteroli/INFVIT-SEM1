#oppgave 1a
def multiplikasjonstabell(n=int):
    for i in range(1, n+1):
        rad = [i * j for j in range(1, n+1)]
        print(" ".join(map(str, rad)))
         
multiplikasjonstabell(3)

#oppgave 1b
def multiplikasjonstabellB(n=int):
    print("* | ",end="")
    delt = "--+"
    for k in range(1,n+1):
        print(f'{k}',end=" ")
        if (n > 3):
            delt += "---"
        else: 
            delt += "--"
    print(f'\n{delt}' )
    for i in range(1, n+1):
        rad = [i * j for j in range(1, n+1)]
        print(f"{i} |",(" ".join(map(str, rad))))
         
multiplikasjonstabellB(3)

#oppgave 2a
def fakultetFor(n):
    if n == 0:
        print("fakultet 1")

    elif n < 0:
        print(f"fakultet {n} er ikke gyldig")
        return None
        
    else:
        sum = 1
        for j in range(1,n+1):
            sum *= j
        print(sum)

fakultetFor(-5)


#oppgave2b
def fakultetWhile(n):
    if n == 0:
        print("fakultet 1")
            
    elif n < 0:
        print(f"fakultet {n} er ikke gyldig")
             
    else:
        sum = 1
        øktTall = 1
        while øktTall <= n:
            sum *= øktTall
            øktTall += 1
        print(sum)  

fakultetWhile(0)