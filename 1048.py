salario = float(input())
reajuste = 0.0

if salario <= 400:
    reajuste = salario*(0.15)
    print(f"Novo salario: {salario+reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 15 %")
elif salario >400 and salario <=800:
    reajuste = salario*(0.12)
    print(f"Novo salario: {salario+reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 12 %")
elif salario >800 and salario <=1200:
    reajuste = salario*(0.10)
    print(f"Novo salario: {salario+reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 10 %")
elif salario >1200 and salario <=2000:
    reajuste = salario*(0.07)
    print(f"Novo salario: {salario+reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 7 %")
elif salario >2000:
    reajuste = salario*(0.04)
    print(f"Novo salario: {salario+reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 4 %")
n    
