d1 = int(input().split()[1])
h1,m1,s1 = map(int,input().split(":"))

d2 = int(input().split()[1])
h2,m2,s2 = map(int,input().split(":"))


segD1 = (s1)+(m1*60)+(h1*60*60)+(d1*24*60*60)
segD2 = (s2)+(m2*60)+(h2*60*60)+(d2*24*60*60)

dif = segD2-segD1 

d = dif//(24*60*60)
dif = dif%(24*60*60)

h = dif//(60*60)
dif = dif%(60*60)

m = dif//60
dif = dif%60

s = dif

print(f"{d} dia(s)")
print(f"{h} hora(s)")
print(f"{m} minutos(s)")
print(f"{s} segundo(s)")
