a,b,c = map(float , input().split())
pi = 3.14159

areaTriangulo = ((a*c)/2)
areaCirculo = pi*(c**2)
areaTrapezio = (((a+b)*c)/2)
areaQuadrado = b*b
areaRetangulo = b*a

print("TRIANGULO: {:.3f}".format(areaTriangulo))
print("CIRCULO: {:.3f}".format(areaCirculo))
print("TRAPEZIO: {:.3f}".format(areaTrapezio))
print("QUADRADO: {:.3f}".format(areaQuadrado))
print("RETANGULO: {:.3f}".format(areaRetangulo))


