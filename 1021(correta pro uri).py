money = float(input())
money = int(round(money * 100))  # Converte para centavos (inteiro)

# NOTAS
cem = money // 10000
money %= 10000

cinquenta = money // 5000
money %= 5000

vinte = money // 2000
money %= 2000

dez = money // 1000
money %= 1000

cinco = money // 500
money %= 500

dois = money // 200
money %= 200

# MOEDAS
moedaum = money // 100
money %= 100

moedacinquenta = money // 50
money %= 50

moedavintecinco = money // 25
money %= 25

moedadez = money // 10
money %= 10

moedacinco = money // 5
money %= 5

moedaumcen = money // 1

print("NOTAS:")
print(f"{cem} nota(s) de R$ 100.00")
print(f"{cinquenta} nota(s) de R$ 50.00")
print(f"{vinte} nota(s) de R$ 20.00")
print(f"{dez} nota(s) de R$ 10.00")
print(f"{cinco} nota(s) de R$ 5.00")
print(f"{dois} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{moedaum} moeda(s) de R$ 1.00")
print(f"{moedacinquenta} moeda(s) de R$ 0.50")
print(f"{moedavintecinco} moeda(s) de R$ 0.25")
print(f"{moedadez} moeda(s) de R$ 0.10")
print(f"{moedacinco} moeda(s) de R$ 0.05")
print(f"{moedaumcen} moeda(s) de R$ 0.01")
