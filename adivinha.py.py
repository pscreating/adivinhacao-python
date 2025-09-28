from random import randint

pc = randint (1,10)

print('\nTopa um desafio?\nEu vou pensar em um número de 1 a 10!\nTente adivinhar qual é!!\n')

acertou =  False

palpite = 0

while not acertou:

    jogador = int(input('\nQual o seu palpite?'))

    palpite += 1

    if jogador < pc:
        print('\nQuase lá... Um pouco mais!')

    if jogador > pc:
        print('\nQue chute alto, haha! Tente mais uma vez! ')

    if jogador == pc:
        acertou = True

        print('\nVoce acertou! Pensamos no mesmo número: {}! E você deu {} palpites até aqui!'.format(jogador, palpite))
