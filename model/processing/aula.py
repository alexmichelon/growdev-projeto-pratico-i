def localiza(dados, linha):
    quantidade_registros = len(dados)
    if linha < quantidade_registros:
        return dados[linha]
    else:
        print('Indice superior a quantidade de registros.')
        return {}

def testar(v1, operacao, v2):
    if operacao == '==':
        return v1 == v2   
    elif operacao == '>':
        return v1 > v2   
    elif operacao == '<':
        return v1 < v2   
    elif operacao == '!=':
        return v1 != v2   
    elif operacao == '>=':
        return v1 >= v2   
    elif operacao == '<=':
        return v1 <= v2
    return False

def filtrar(dados, campo, valor, operacao):
    dados_filtrados = []
    for linha in dados:

        if testar(linha[campo], operacao, valor):
            dados_filtrados.append(linha)
    return  dados_filtrados

def projetar(dados, colunas):
    dados_projetados = []
    for linha in dados:
        linha_projetada = {}
        for campo, valor in linha.items():
            if campo in colunas:
                linha[campo] = valor
        dados_projetados.append(linha_projetada)
    return dados_projetados