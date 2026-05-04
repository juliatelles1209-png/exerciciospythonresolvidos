"""desafio 73:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense."""

times = 'Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo', 'Athletico-PR', 'Bahia', 'Bragantino', 'Coritiba', 'Vitoria', 'Botafogo', 'Atletico', 'Internacional', 'Vasco', 'Grêmio', 'Cruzeiro', 'Santos', 'Corinthians', 'Mirassol', 'Remo', 'Chapecoense'

#cabeçalho
print ('-='*40)
print ('-='*15, 'BRASILEIRÃO 2026', '-='*16)
print ('-='*40)

# a) Os 5 primeiros times
print (f'Os 5 primeiros colocados são {times[0:5]}')
print ('-='*40)

# b) Os últimos 4 colocados.
print (f'Os 4 últimos colocados são {times[16:20]}')
print ('-='*40)

# c) Times em ordem alfabética.
times_ord = tuple(sorted(times))
print (f'Times em ordem alfabética {times_ord}')
print ('-='*40)

# d) Em que posição está o time da Chapecoense
print (f'O time da Chapecoense está em {times.index("Chapecoense")+1}° posição')
print ('-='*40)

# Funcionalidade adicional: Pesquisar qual a posição do seu time 
while True:
    resp = str(input('Quer descobrir a posição do seu time? (S/N)')).strip().lower()[0]

    if resp not in ('sim', 's'):
        print ('Programa finalizado')
        break

    else:
        time_usuário = str(input('Qual o seu time?')).strip().title()
        if time_usuário not in times:
            print ('Seu time não faz parte da série A do Brasileirão')
            break
        
        else: 
            print (f'Seu time está na {times.index(time_usuário)+1}° posição')