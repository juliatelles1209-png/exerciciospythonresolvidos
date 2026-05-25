#Desafio 81
"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

num = []

while True:
    n = (int(input('Digite um valor:')))
    num.append(n)

    resp = str(input('Quer continuar (S/N): ')).lower().strip()[0]
    while resp not in ('s', 'n'):
        resp = str(input('Quer continuar (S/N): ')).lower().strip()[0]
    if resp in 'n':
        print('Finalizando...')
        break

total = len(num)
num.sort(reverse = True)

print(f'O total de elementos foi {total}')
print(f'Os números digitados foram {num}')

if 5 in num:
    print('O valor 5 foi encontrado na lista')
else:
    print('O valor 5 não foi encontrado na lista')