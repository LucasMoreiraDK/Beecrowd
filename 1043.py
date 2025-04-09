a,b,c = map(float , input().split())
per = a+b+c


if a+b > c and a+c>b and b+c > a:
    print(f"Perimetro = {per}")

    
else:

    area = ((a+b)*c)/2
    print(f"Area = {area}")
    
