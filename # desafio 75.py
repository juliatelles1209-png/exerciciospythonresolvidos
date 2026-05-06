# desafio 75
"""Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

num = tuple(int(input('Digite um valor:')) for _ in range (4))

# a) Quantas vezes apareceu o valor 9:
num9 = num.count(9)
print (f'O número 9 apareceu {num9} vezes')

# b) Em que posição foi digitado o primeiro valor 3:
if 3 in num:
    print (f'O valor 3 foi digitado primeiro na posição {num.index(3)+1}')
else:
    print ('O valor 3 não foi digitado')

# C) Quais foram os números pares:
pares = []
for n in num:
    if n % 2 == 0:
        pares.append(n)
print (f'Os números pares digitados foram: "{pares}"')