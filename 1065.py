v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
v5 = int(input())

pares = 0
valores = [v1,v2,v3,v4,v5]

for i in valores:
    if (i%2)==0:
        pares+=1
print(f"{pares} valores pares")
