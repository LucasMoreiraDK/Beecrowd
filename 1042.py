listaIn = []
listaOrd = []
v1,v2,v3 = map(int ,input().split())

listaIn.extend([v1, v2, v3])

listaOrd = sorted(listaIn)

for i in listaOrd:
    print(i)
print("")
for i in listaIn:
    print(i)
