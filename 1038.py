cod,quan = map(int , input().split())
total = 0.0

cachorroquente = 4.00 #1
xsalada = 4.50#2
xbeaco = 5.00#3
torradasimples = 2.00#4
refri = 1.5#5

if cod ==1:
    total = cachorroquente*quan
    print(f"Total: R$ {total:.2f}")
elif cod ==2:
        total = xsalada*quan
        print(f"Total: R$ {total:.2f}")
elif cod ==3:
        total = xbeaco*quan
        print(f"Total: R$ {total:.2f}")
elif cod ==4:
        total = torradasimples*quan
        print(f"Total: R$ {total:.2f}")
elif cod ==5:
        total = refri*quan
        print(f"Total: R$ {total:.2f}")


