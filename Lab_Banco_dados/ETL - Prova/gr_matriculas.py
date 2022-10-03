import random

arquivo = open('matriculas.txt', 'a')
lista = ['A', 'R']
mat_alu = 1

def escrever(arquivo, mat_alu):
    for i in range (1, 10001):
        semestre = random.randint(1, 2)
        #mat_alu
        cod_disc = random.randint(1, 24)
        nota = random.randint(0, 10)
        faltas = random.randint(0, 20)
        arquivo.write(f'{semestre},{mat_alu},{cod_disc},{nota},{faltas},\n')
        mat_alu += 1

escrever(arquivo, mat_alu)