a,b,c = map(float , input().split())
listaOrd = [a,b,c]
listaOrd.sort(reverse=True)

a = listaOrd[0]
b = listaOrd[1]
c = listaOrd[2]




if a >=b+c:
    print("NAO FORMA TRIANGULO")
else:
    if a >=b+c:
        print("NAO FORMA TRIANGULO")
    if (a**2)==((b**2)+(c**2)):
        print("TRIANGULO RETANGULO")
    if (a**2)>((b**2)+(c**2)):
        print("TRIANGULO OBTUSANGULO")
    if (a**2)<((b**2)+(c**2)):
        print("TRIANGULO ACUTANGULO")
        
    if (a==b==c):
        print("TRIANGULO EQUILATERO")
    elif a==b or b==c or a==c:
        print("TRIANGULO ISOSCELES")
