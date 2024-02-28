# Escreva um programa que leia a velocidade de um carro.
# Se ela ultrapassar de 80Km/h, mostre uma mensagem
# dizendo que f multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é 80Km/h ')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com cuidado!')
