# Banco_de_dados
## Conteúdo voltado para banco de dados, com algumas atividades resolvidas e alguns tutoriais quem sabe de utilização de cada linguagem SQL.
---------------------------
# Funções de Agregação
|Função| Exemplo| Descrição|
|--------|---------|-------|
|Avg|`Avg(Sales)`|Calcula a média de um conjunto numérico de valores.
|Bin|`Bin(UnitPrice BY ProductName)`|Seleciona qualquer atributo numérico de uma dimensão, tabela de factos ou medida contendo valores de dados e coloca-os num número discreto de depósitos. Esta função é tratada como um novo atributo de dimensão para fins de agregação, filtragem e definição de níveis de detalhe.
|Count|`Count(Products)`|Determina o número de itens com um valor não nulo.
|Primeiro|`First(Sales)`|Seleciona o primeiro valor não nulo devolvido do argumento da expressão. A função  `First`  opera ao nível mais detalhado especificado na dimensão definida explicitamente.
|Último|`Last(Sales)`|Seleciona o último valor não nulo devolvido da expressão.
|Max|`Max(Revenue)`|Calcula o valor máximo (valor numérico mais alto) das linhas que satisfazem o argumento da expressão numérica.
|Median|`Median(Sales)`|Calcula o valor mediano (intermédio) das linhas que satisfazem o argumento da expressão numérica. Quando existe um número par de linhas, o mediano é a média das duas linhas do meio. Esta função devolve sempre um duplo.
|Min|`Min(Revenue)`|Calcula o valor mínimo (valor numérico mais baixo) das linhas que satisfazem o argumento da expressão numérica.
|StdDev|`StdDev(Sales) StdDev(DISTINCT Sales)`|Devolve o desvio padrão de um conjunto de valores. O tipo devolvido é sempre um duplo.
|StdDev_Pop|`StdDev_Pop(Sales) StdDev_Pop(DISTINCT Sales)`|Devolve o desvio padrão de um conjunto de valores através da utilização da fórmula computacional para variância completa e desvio padrão.
|Sum|`Sum(Revenue)`|Calcula a soma obtida através da adição de todos os valores que satisfazem o argumento da expressão numérica.

