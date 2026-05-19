# desafio 79
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = [] 
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado.')
    else:
        print('Valor duplicado... Não irei adicioná-lo')
    resp = (input('Quer continuar(S/N)?: ')).strip().lower()[0]
    if resp in 'Nn':
        print('Programa encerrado!')
        break
valores.sort()
print(f'Os valores adicionados foram {valores}')