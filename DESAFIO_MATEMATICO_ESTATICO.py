totalerros = 0
acertos = 0
tentativas = 0
print("Acerte todas as equações matemáticas para vencer o desafio:")
while acertos < 4:
    acertos = 0
    erros = 0
    tentativas += 1
    i = int(input("Soma: 456 + 38 = "))
    if i == 494:
        acertos += 1
    else:
        erros +=1
    ii = int(input("Subtração: 763 - 57 = "))
    if ii == 706:
        acertos += 1
    else:
        erros +=1
    iii = int(input("Multiplicação: 12 x 36 = "))
    if iii == 432:
        acertos += 1
    else:
        erros +=1
    iv = int(input("Divisâo: 150 ÷ 25 = "))
    if iv == 6:
        acertos += 1
    else:
        erros +=1
    if erros >= 1:
        print("Tente de novo, você errou:", erros, "equações")
    totalerros += erros
print("Parabéns você resolveu o desafio em", tentativas, "tentativas.\nCom o total de", totalerros, "erros.")