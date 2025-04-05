#aparentemente essa minha solução não é adequada pois o python as vezes arredonda incorretamente alguns valores pequenos#

money = float(input())

cem  = money//100
money = money-(cem*100)

cinquenta = money//50
money = money-(cinquenta*50)

vinte = money//20
money = money-(vinte*20)

dez = money //10
money = money-(dez*10)

cinco = money//5
money=money-(cinco*5)

dois = money//2
money=money-(dois*2)

#moedas#

moedaum = money //1
money=money-(moedaum*1)

moedacinquenta = money//0.5
money=money-(moedacinquenta*0.5)

moedavintecinco = money//0.25
money=money-(moedavintecinco*0.25)

moedadez = money//0.1
money=money-(moedadez*0.1)

moedacinco = money//0.05
money=money-(moedacinco*0.05)

moedaumcen = money//0.01
money=money-(moedaumcen*0.01)

print("NOTAS:")
print(f"{int(cem)} nota(s) de R$ 100.00")
print(f"{int(cinquenta)} nota(s) de R$ 50.00")
print(f"{int(vinte)} nota(s) de R$ 20.00")
print(f"{int(dez)} nota(s) de R$ 10.00")
print(f"{int(cinco)} nota(s) de R$ 5.00")
print(f"{int(dois)} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{int(moedaum)} moeda(s) de R$ 1.00")
print(f"{int(moedacinquenta)} moeda(s) de R$ 0.50")
print(f"{int(moedavintecinco)} moeda(s) de R$ 0.25")
print(f"{int(moedadez)} moeda(s) de R$ 0.10")
print(f"{int(moedacinco)} moeda(s) de R$ 0.05")
print(f"{int(moedaumcen)} moeda(s) de R$ 0.01")





