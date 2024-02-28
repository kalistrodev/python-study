# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o 
# usuário venceu ou perdeu!

#Exemplo 1 com um número definido!
pense =  int(input('Pense em um número 1 a 10: '))
print('A sua resposta foi ', pense)
if pense == 7:
    print('Você acertou! PARABÉNS')
else:
    print('Você ERROU! O computador venceu!')

# Exemplo 2 com um número escolhido aleatóriamente!
from random import randint
computador = randint(0, 5) # Faz o computador gerar um número aleatório de 0 a 5
print('-=-' * 5)
print('Vou pensar em um número entre 0 e 5. Tente advinhar! ')
print('-=-' * 5)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('Você acertou!')
else: 
    print('Você errou! Eu pensei no número {} e não no {}!'.format(computador, jogador))
    
