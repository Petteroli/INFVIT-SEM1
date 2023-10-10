def multiplikasjonstabell(n=int):
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
         

multiplikasjonstabell(3)