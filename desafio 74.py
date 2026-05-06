# Desafio 74:
""""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

from random import randint

numeros = tuple(randint(1,10) for _ in range(5))

print (f'Os números sorteados foram: {numeros}')
print (f'O maior número sorteado foi {max(numeros)}')
print (f'O menor número sorteado foi {min(numeros)}')