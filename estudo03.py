# Curso Python Aula de Estudo 3 - Operadores Aritméticos
# https://algoritmosempython.com.br/cursos/programacao-python/operadores/

# + Adição
# - Subtração 
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão Inteira
# % Resto da divisão

# Ordem de Precedência
# 1 {}
# 2 **
# 3 *, /, //, %,
# 4 +, -

# OBS: Para fazer na quebra de linha no cmd print usa o (\n) e para juntar usa o (end)

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potência é {}'.format(di, e))

nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome)) # Coloca o resultado da string em 20 caracteres a direita

nome1 = input('Qual seu nome? ')
print('Prazer em te conhecer {:<20}!'.format(nome1)) # Coloca o resultado da string em 20 caracteres a esquerda

nome2 = input('Qual seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome2)) # Coloca o resultado da string em 20 de = em volta 
