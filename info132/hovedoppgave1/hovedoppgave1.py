#hovedinnlevering oppgave 1
import math

def pi(d=None):
    if d is None:
        return round(math.pi,2)
    
    if d > 16:
        print("For mange desimaler!")
        return round(math.pi,d)
    
    return round(math.pi,d)

print(pi(3))
print(pi(17))
print(pi())