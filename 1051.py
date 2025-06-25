salario = float(input())

if salario <= 2000:
    print("Isento")
elif salario >= 2000.01 and salario <= 3000:
    salCorigido8 = salario-2000
    print(f"R$ {salCorigido8*0.08:.2f}")
    
elif salario >=3000.01 and salario <= 4500:
    salCorigido18 = salario-3000
    print(f"R$ {(salCorigido18*0.18)+(1000*0.08):.2f}")
    
elif salario > 4500:
    salCorigido28 = salario-4500
    print(f"R$ {(salCorigido28*0.28)+(1500*0.18)+(1000*0.08):.2f}")