
import random

arquivo = open('alunos.csv', 'a')
mat_alu = 1
lista = ['S', 'N']

# Gerar matricula, data, curso , cotista - Nome veio por fora
def escrever(arquivo, mat_alu):
    for i in range (1, 10001):
        dia = random.randint(1, 31)
        curso = random.randint(1, 6)
        cota = random.sample(lista, 1)
        arquivo.write(f'{mat_alu},{dia}/01/2019,{curso},{cota},\n')
        mat_alu += 1

escrever(arquivo, mat_alu)