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

fakultetWhile(5)