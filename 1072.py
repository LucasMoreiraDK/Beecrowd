n = int(input())

tabIn = 0
tabOut = 0

for i in range(n):
    b = int(input())
    
    if b >= 10 and b <= 20:
        tabIn += 1
    else:
        tabOut += 1
print(f"{tabIn} in") 
print(f"{tabOut} out")
