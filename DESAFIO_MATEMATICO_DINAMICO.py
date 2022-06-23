import random

erros = 0
totalerros = 0
acertos = 0
tentativas = 0

print("Resolva as equações corretamente para vencer o desafio")

while acertos < 4:

    acertos = 0
    erros = 0
    tentativas += 1

    soma1 = random.randint(0, 1000)
    soma2 = random.randint(0, 1000)
    sub1 = random.randint(0, 1000)
    sub2 = random.randint(0, 1000)
    mult1 = random.randint(0, 100)
    mult2 = random.randint(0, 100)
    n = random.randint(0, 100)
    div1 = random.randint(0, 100)
    div2 = n * div1

    print("Resolva", soma1, "+", soma2, ":")
    pergunta1 = float(input())
    print("Resolva", sub1, "-", sub2, ":")
    pergunta2 = float(input())
    print("Resolva", mult1, "*", mult2, ":")
    pergunta3 = float(input())
    print("Resolva", div2, "÷", div1, ":")
    pergunta4 = float(input())

    if pergunta1 == soma1 + soma2:
        acertos += 1
    else:
        erros += 1

    if pergunta2 == sub1 - sub2:
        acertos += 1
    else:
        erros += 1

    if pergunta3 == mult1 * mult2:
        acertos += 1
    else:
        erros += 1

    if pergunta4 == div2 / div1:
        acertos += 1
    else:
        erros += 1

    if acertos < 4:
        print("Faça de novo até acertar todas. Você cometeu", erros, "erros.")

    totalerros += erros

print("Parabéns, você completou o desafio em", tentativas, "tentativas e teve um total de", totalerros, "respostas erradas.")