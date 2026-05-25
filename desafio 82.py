#desafio 82
"""Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas."""

num = []
numpar = []
numimpar = []

while True:
    n = int(input('Digite um número: '))
    num.append(n)

    if n % 2 == 0:
        numpar.append(n)
    else:
        numimpar.append(n)

    resp = str(input('Quer continuar (S/N): ')).strip().lower()[0]

    while resp not in ('s', 'n'):
        resp = str(input('Resposta inválida! Quer continuar (S/N): ')).strip().lower()[0]

    if resp in 'n':
        print('Finalizando...')
        break

print(f'A lista completa é {num}')
print(f'A lista de números pares é {numpar}')
print(f'A lista de números ímpares é {numimpar}')

