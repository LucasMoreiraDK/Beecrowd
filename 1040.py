a,b,c,d = map(float , input().split())

med = ((2*a)+(3*b)+(4*c)+(1*d))/10

print(f"Media: {med:.1f}")
if med > 7:
    print("Aluno aprovado.")
elif med >=5 and med <=6.9:
    print("Aluno em exame.")
    examenota = float(input())
    print(f"Nota do exame: {examenota:.1f}")
    total = (examenota+med)/2
    if total >=5:
        print("Aluno aprovado.")
        print(f"Media final: {total}")
    elif total <=4.9:
        print("Aluno reprovado.")
        print(f"Media final: {total}")
elif med < 5 :
    print("Aluno reprovado.")
    
