from Extracao import filiais_values, fornecedores_values, mercadorias_values

#Transformação Filiais
filiais_values_t = []

for linha in filiais_values:

    if (1 > int(linha[1]) > 99):
        print("Código de Filial inválido. Precisa estar entre 1 e 99.")
        break

    if (len(linha[2]) > 50):
        print("Nome da Filial inválida. Precisa ter no máximo 50 caracteres.")
        break    

    filiais_values_t.append(linha)


#Transformação Fornecedores
fornecedores_values_t = []

for linha in fornecedores_values:
    
    if (1 > int(linha[1]) > 999):
        print("Código de Fornecedor inválido. Precisa estar entre 1 e 999.")
        break
     
    if (len(linha[3]) != 2):
        print("Sigla do Estado inválida. Precisa ter 2 caracateres.")
        break    

    fornecedores_values_t.append(linha)    


#Transformação Mercadorias
mercadorias_values_t = []

for linha in mercadorias_values:
    
    if (1 > int(linha[1]) > 999):
        print("Código da Mercadoria inválido. Precisa estar entre 1 e 999.")
        break
     
    if (len(linha[2]) > 50):
        print("Nome da Mercadoria inválida. Precisa ter no máximo 50 caracteres.")
        break    

    mercadorias_values_t.append(linha)      