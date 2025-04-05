cem = cinquenta = vinte = dez = cinco = dois = um = 0
money = int(input())
print(money)


cem = money//100
money = money%100

cinquenta = money//50
money = money%50

vinte = money//20
money = money%20

dez = money//10
money = money%10

cinco = money//5
money = money%5

dois = money//2
money = money%2

um = money//1
money = money%1



print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")
