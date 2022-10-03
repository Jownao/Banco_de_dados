import csv

#Extração para os dados da Filial

#Abrindo o arquivo CSV
with open('CVS/dm_filial.csv', encoding='utf-8') as csv_filial:

    #indicando qual o delimitador do arquivo CSV
    csvfilial = csv.reader(csv_filial, delimiter = ',')

    #Pulando a linha de cabeçalho. Primeira linha do CSV
    next(csvfilial)

    #Lista para armazenar os valores a serem inseridos no Banco de Dados
    filiais_values = []

    #Percorrendo o arquivo CSV para inserir as linhas na nossa lista
    for row in csvfilial:
        value = (row[0], row[1], row[2])
        filiais_values.append(value)
    print(filiais_values)

#Extração para os dados do Fornecedor

#Abrindo o arquivo CSV
with open('CVS/dm_fornecedor.csv', encoding='utf-8') as csv_fornecedor:

    #indicando qual o delimitador do arquivo CSV
    csvfornecedor = csv.reader(csv_fornecedor, delimiter = ',')

    #Pulando a linha de cabeçalho. Primeira linha do CSV
    next(csvfornecedor)

    #Lista para armazenar os valores a serem inseridos no Banco de Dados
    fornecedores_values = []

    #Percorrendo o arquivo CSV para inserir as linhas na nossa lista
    for row in csvfornecedor:
        value = (row[0], row[1], row[2], row[3], row[4])
        fornecedores_values.append(value)


#Extração para os dados do Mercadoria

#Abrindo o arquivo CSV
with open('CVS/dm_mercadoria.csv', encoding='utf-8') as csv_mercadoria:

    #indicando qual o delimitador do arquivo CSV
    csvmercadoria = csv.reader(csv_mercadoria, delimiter = ',')

    #Pulando a linha de cabeçalho. Primeira linha do CSV
    next(csvmercadoria)

    #Lista para armazenar os valores a serem inseridos no Banco de Dados
    mercadorias_values = []

    #Percorrendo o arquivo CSV para inserir as linhas na nossa lista
    for row in csvmercadoria:
        value = (row[0], row[1], row[2])
        mercadorias_values.append(value)
