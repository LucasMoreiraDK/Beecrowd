ini , fim = map(int , input().split())


horas = 0
if ini == fim:
    print("O JOGO DUROU 24 HORA(S)")
elif ini > fim:
    horas = (24-ini)+fim
    print(f"O JOGO DUROU {horas} HORA(S)")
else:
    horas = (fim-ini)
    print(f"O JOGO DUROU {horas} HORA(S)")

