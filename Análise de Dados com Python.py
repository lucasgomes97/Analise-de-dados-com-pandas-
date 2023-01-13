# Análise de Dados com Python
# 1 -Importar a base de dados
import pandas as pd
tabela_dados = pd.read_csv(r'C:\Users\vidal\Downloads\telecom_users.csv')

# 2 -Visualizar a base de dados
# (entender as informações disponiveis e descobrir possíveis erros: informções que não te ajuda, só te atrapalha  )
# axis -> 0 = linha ; axis -> 1 = coluna
tabela_dados = tabela_dados.drop('Unnamed: 0', axis=1)# retirar dados da tabela que não contribuem em nada
print(tabela_dados)

# 3 -Tratamento de Dados
print(tabela_dados.info())# Apresenta todos os dados da tabela
# 3.1 -Resolver os valores que estão sendo reconhecidos de forma errada
tabela_dados["TotalGasto"] = pd.to_numeric(tabela_dados["TotalGasto"], errors= "coerce")
print(tabela_dados.info())
# 3.2 -Resolver valores vazio (colunas e linhas que todos ou alguns valores são vazios, estes serão excluidas)
tabela_dados = tabela_dados.dropna(how="all", axis=1)# Exlui colunas e/ou linhas que são completamentes vazias
tabela_dados = tabela_dados.dropna(how="any", axis=0)# Se tiver um codigo vazio, a linha e/ou coluna sera excluida
print(tabela_dados.info())

# 4 - Análise Inicial 
print(tabela_dados['Churn'].value_counts()) # informa os resultados da tabela da linha digita nos [].
print(tabela_dados['Churn'].value_counts(normalize=True).map("{:.1%}".format))# apresenta em porcentagem os resultados

# 5 - Análise detalhada 
# 5.1 Comparar cada coluna da base de dados com a coluna Churn
import plotly.express as px
# 5.1.1 Criando o gráfico
# Criando um gráfico para cada coluna da tabela 
for coluna in tabela_dados.columns:  
    grafico = px.histogram(tabela_dados, x=coluna, color="Churn", text_auto=True)
    # 5.1.2 Exibindo gráfico
    grafico.show()
# Conclusão
''' Clientes que tem famílias maiores tendem a cancelar menos 
    * Planos familias 
        - Promoções diferenciadas para mais pessoas da mesma família 
        
    Os clientes nos primeiros meses tem a tendência  Muito maior a cancelar
        - Pode ser algum markting muito agressivo
        - Pode ser que a experiência nos primeiros meses seja ruim
        - Pode fazer uma promoção de no primeiro ano a mensalidade seja menor 
    Tem algum problema no serviço Fibra
    Quanto mais serviços o cliente tem, menos ele cancela
        - Podemos oferecer mais serviços de graça ou por um preço muito menor
    Quase todos os cancelamentos estão no contrato mensal
        - Oferece desconto no anual, no de 2 anos 
    No boleto eletrônico  o cancelamento é muito maior, oferece desconto no cartão ou em dcc
    '''
