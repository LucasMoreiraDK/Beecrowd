x,y = map(float ,input().split())


if x == y == 0:
    print("Origem")
elif y == 0 and x !=0:
    print("Eixo X")
elif x == 0 and y !=0:
    print("Eixo Y")
else:
    if x > 0 and y<0:
        print("Q4")
    if x > 0 and y>0:
        print("Q1")
    if x < 0 and y<0:
        print("Q3")
    if x < 0 and y>0:
        print("Q2")
