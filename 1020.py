dias = int(input())

anos = dias//365
dias = dias-(365*anos)

meses = dias//30
dias = dias-(30*meses)

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
