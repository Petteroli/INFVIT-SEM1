def fakultetFor(n):
    if n == 0:
        print("fakultet 1")

    elif n < 0:
        print(f"fakultet {n} er ikke gyldig")
        
    else:
        sum = 1
        for j in range(1,n+1):
            sum *= j
            print(sum)

fakultetFor(5)
