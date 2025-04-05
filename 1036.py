import math
 

a,b,c = map(float, input().split())

raiz = (b**2)-4*a*c

if a == 0:
    print("Impossivel calcular")
elif raiz < 0:
    print("Impossivel calcular")
else:
    raizz = math.sqrt(raiz)
    r1 = (-b+raizz)/(2*a)
    r2 = (-b-raizz)/(2*a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")

