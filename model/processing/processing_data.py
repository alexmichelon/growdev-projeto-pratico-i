#retorna registro conforme lista de índices repassado:
# -data: lista de dicionário de dados
# -list_index: lista de índices para localização dos dados.Permite busca por slicing no formato: [n,[n],[n,n],[n,n,n],[n]]. Para slice sem valor, considerar [a:] = [a,None]; [a::] = [a, None, None]; [::] = [None, None, None]
def locate_data_for_list_of_index(data: list[dict], list_index: list[list]):  
    """
    Locate data in datafile whit informed index, considering slice format.\n\n
    data\n list of data(dict): each data line of the file. \n
    index -> list of indexes of position to locate data. Ps.: format [a,[a,b],[a,b,c]]. 
    that return the format for each position of the list [a:b:c]. 
    Arguments b e c can be empty. To using slice mode in format: [a:] = [a,None]; [a::] = [a, None, None]; ; [::] = [None, None, None].\n
    return a list of dicts that contains filtred data.
    """
    try:
        located_data = [] #cria (vazia) lista de dados localizados
        for i in range (len(list_index)): #lê o tamanho da lista de índices fornecido e cria um contador
            index = [] #cria uma lista de índices para verificação
            index.append(list_index[i]) #atribui para a lista de índices o índice lido da lista de índices informados
            if (type(index[0]) == list): #verifica se o tamanho do índice lido é do tipo lista. Ex.: caso seja informado [[n]] ao invés de [n] onde n é um número inteiro
                if (len(index[0]) > 1): #verifica se existe mais de um ítem no índice lido (slicing)
                    if len(index[0]) == 2: #caso o índice lido (lista) tenha duas posições
                        located_data.append(data[index[0][0]:index[0][1]]) #adiciona a lista de dados localizados em formade slicing dados no formato: [n:n] onde n é um número inteiro 
                    elif len(index[0]) == 3: #caso o índice lido (lista) tenha três posições
                        located_data.append(data[index[0][0]:index[0][1]:index[0][2]])#adiciona a lista de dados localizados em formade slicing dados no formato: [n:n:n] onde n é um número inteiro 
                    else: #caso o índice lido (lista) tenha mais de três posições
                        print(f'too many parameters provided: expected 3, informed {len(index[0])}') #retorna erro de número de parâmetros
                        located_data.clear() #limpa a lista de dados localizados
                        break #para de procurar dados
                else: #em caso de haver apenas um ítem no índice lido (lista de índices)
                    located_data.append(data[index[0][0]]) #adiciona  a lista de dados localizados dados no formato: [n] onde n é um número inteiro. Obs.: para o caso de ser informado uma lista do tipo [n,[n]] ao invés de [n,n]. 
            else: #caso o índice lido não seja uma lista. Obs.: esteja no formato [n] onde n é um número inteiro
                located_data.append(data[index[0]]) #adiciona  a lista de dados localizados dados no formato: [n] onde n é um número inteiro
        return located_data #retorna a lista de dados localizados
    except IndexError as error: #tratamento de exceção para o caso de ser informado índice que não exista na lista
        print(f'index not found: {error}') #retorna erro de 'índice não encontrado'
        return [] #retorna vazio pois não há dados para o índice informado



#compara dois valores com um operador lógico (feita em aula)
def compare_values(value1: str, logical_operator: str, value2: any):
    """
    Compare two values from logical operator informed.\n\n
    value1 \n key(columm) of datafile. \n
    logical_operator \n value do logical operator to compare.\n
    value2 \n value of key(columm) desired.\n
    return the operation whit value1 and value2 from the logical operator.
    """
    if logical_operator == '==':
        return value1 == value2   
    elif logical_operator == '>':
        return value1 > value2   
    elif logical_operator == '<':
        return value1 < value2   
    elif logical_operator == '!=':
        return value1 != value2   
    elif logical_operator == '>=':
        return value1 >= value2   
    elif logical_operator == '<=':
        return value1 <= value2
    return False


#filtra dados considerando uma lista de dicionários contendo em dicionários dados de filtragem 
# -data: lista de dicionário de dados
# -rules: lista de regras para filtrar. Formato "rule" = {'key': str, 'logical_operator': str, 'value': any}
def filter_data(data: list[dict], rules: list[dict]):
    """
    Filter the data from rules informed. \n\n
    data \n list of data(dict): each data line of the file. \n
    rules \n list of rules(dict): informed rules to filter the data. 
    Rule is a logical comparision in format {'key': str, 'logical_operator': str, 'value': any}. \n
    return list of dicts whit founded data.
    """
    found_data = [] #cria e inicializa (vazia) a lista de dicionários onde serão inseridos os dados encontrados
    for line in data: #lê cada linha (dicionário) de data (lista de dicionários)
        if(rules == None): #se a lista de regras for None
            return [] #para a busca e retorna uma lista vazia
        for index, rule in enumerate(rules): #lê cada regra da lista de regras criando um contador
            if compare_values(line[rule['key']], rule['logical_operator'], (rule['value'])) == False: #verifica se a regra lida é valida
                break #senão for uma regra válida, para a execução
            if index == (len(rules)-1): #verifica se ainda existe regras a serem validadas: até a última regra da lista de regras
                found_data.append(line) #o registro se encaixa nas regras da lista de regras e é inserido na lista de dicionários de dados encontrados
    return  found_data #retorna lista de dicionários contendo dados encontrados a partir das regras


#efetua a seleção dos dados através de lista de chaves (feita em aula)
# -data: lista de dicionário de dados
# -keys: lista de str onde cada posição é um campo (coluna) da base de dados
def projection_data(data: list[dict], keys: list[str]):
    """
    Show datafile filtred for list of keys informed.\n\n
    data \n list of data(dict): each data line of the file. \n
    keys \n list[str] of keys: key is a field in the datafile.\n
    return list of dicts that contains data ahit keys informed.
    """
    project_data = [] #cria e inicializa (vazia) a lista de dicionários contendo dados projetados
    for line in data: #lê cada linha (dicionário) de data (lista de dicionários)
        project_line = {} #cria e inicializa (vazio) a o dicionário que irá receber os dados projetados
        for key, value in line.items(): #lê cada chave e valor da linha lida ds lista de dicionários
            if key in keys: #lê cada chave da lista de chaves (chave é um campo do arquivo de dados)
                project_line[key] = value #atribui o valor da chave na posição chave da linha projetada
        project_data.append(project_line) #adiciona a linha projetada (dicionário) na lista de dicionários de dados projetados
    return project_data #retorna a lista de dicionários de dados projetados


#filters = [{'key': 'cidade', 'logical_operator': '==', 'value': '', 'type_value': any}]

#Atualiza dados do dicionário de dados 
# -data: lista de dicionário de dados
# -rules: lista de regras para filtrar. Formato "rule" = {'key': str, 'logical_operator': str, 'value': any}
# -update_list: lista de dicionários contendo chaves e valores para atualizar: chave (campo) e value (valor)
def update_data_by_rule(data: list[dict], rules: list[dict], update_list: list[dict]):
    """
    Update the value of data in the list of dicts from rule(s) informed \n\n
    data \n list of data(dict): each data line of the file. \n
    rules \n list of rules(dict): informed rules to filter the data. Obs.: can be None, then update all records. 
    Rule(dict) is a logical comparision in format {'key': str, 'logical_operator': str, 'value': any}. \n
    update_list \n list{dict) of keys and values to update the datafile in format: {'key': str, 'value': any}. \n
    return all data that contains updated records.
    """
    modified_records = 0 #número de registros atualizados
    list_data_updated = [] #lista de dicionário de dados atualizados
    for line in data: #lê cada linha (dicionário) de data (lista de dicionários)
        if rules == None: #verifica se as regras são nulas: atualiza todos os registros da lista de dicionários
            for dict in update_list: #lê cada dicionário (chave e valor) da lista de dicionários de dados para atualização
                        for key, value in dict.items(): #lê chave e valor do dicionário lido
                            line[key] = value #atualiza com o valor informdo a linha na posição da chave informada
            list_data_updated.append(line) #adiciona linha atualizada na lista de dicionário de dados atualizados
            modified_records += 1 #itera o contador de registros atualizados
        else: #caso existam regras informadas
            for index, rule in enumerate(rules): #lê a regra da lista de dcionários de regras com um contador
                if compare_values(line[rule['key']], rule['logical_operator'], (rule['value'])) == False: #verifica se a regra lida é valida
                    break #senão for uma regra válida, para a execução
                if index == (len(rules)-1): #verifica se ainda existe regras a serem validadas: até a última regra da lista de regras
                    for dict in update_list: #lê cada dicionário (chave e valor) da lista de dicionários de dados para atualização
                        for key, value in dict.items(): #lê chave e valor do dicionário lido
                            line[key] = value #atualiza com o valor informdo a linha na posição da chave informada
                    list_data_updated.append(line) #adiciona linha atualizada na lista de dicionário de dados atualizados
                    modified_records += 1 #itera o contador de registros atualizados
    return data, list_data_updated, modified_records #retorna a lista de dicionário de dados contendo os registros atualizados, a lista de dicionário contendo apenas os dados atualizados e o número de registros atualizados

#Agrupa valores de um campo: conta registros deste campo ou soma valores de outro campo
# -data: lista de dicionário de dados
# -key: campo (coluna) para agrupar dados (chave agrupadora)
# -key_sum: campo que terá seus valores somados (chave a somar) e agrupados por key. Caso seja None, soma registros de key
def group_data_by_count(data:list[dict], key:str, key_sum:str | None):
    '''
    Group values by a filed \n\n
    data \n list of data(dict): each data line of the file. \n
    key\n field of the datafile (column) to group values (grouping key).\n
    key_sum\n field os the datafile (column) that will its values summed and group by the key. 
    Should be a numerical value. Can be None, then sum all the records that contain the key.\n
    return a dict that contains key (key value) and value (group value).
    '''
    grouped_by_key_values = {} #cria a inicializa (vazio) um dicionário para receber os dados agrupados
    if key_sum == None: #verifica se a chave para somar é None
        for line in data: #lê cada linha (dicionário) de data (lista de dicionários)
            grouped_by_key_values[line[key]] = grouped_by_key_values.get(line[key], 0) + 1 #verifica se o valor da chave a agrupar existe no dicionário. Senão existir, cria, se existir soma o valor existente com o registro lido (contador): conta ocorrências da chave agrupadora
    else: #se há uma chave a somar informada
        for line in data: #lê cada linha (dicionário) de data (lista de dicionários)
            grouped_by_key_values[line[key]] = grouped_by_key_values.get(line[key], 0) + line[key_sum] #verifica se o valor da chave a agrupar existe no dicionário. Senão existir, cria, se existir soma o valor existente com o registro lido: soma valores de uma chave a somar para agrupar pela chave agrupadora
    return grouped_by_key_values #retorna o dicionário contendo chave (valor da chave agrupadora) e valor (valor agrupado pela chave a somar ou contador de ocorrências da chave agrupadora)


#função de agrupamento por uma chave desenvolvida em aula
#def group_data_by_list(data=list[dict], key=str):
#    data_grouped_by_key_values = {}
#    for line in data:
#        key_value = line[key]
#        if data_grouped_by_key_values.get(key_value) == None:                              
#            data_grouped_by_key_values[key_value] = []
#        data_grouped_by_key_values[key_value].append(line)
#    return data_grouped_by_key_values


#Agrupa valores de um campo: agrupa registros pelo valor de um campo informado
# -data: lista de dicionário de dados
# -key: campo (coluna) para agrupar dados (chave agrupadora)
def group_data_by_list(data:list[dict], key:str):
    '''
    Group records by a filed \n\n
    data \n list of data(dict): each data line of the file. \n
    key\n field of the datafile (column) to group values (grouping key).\n
    return a list of dicts that contains key (key value) and value (records).
    '''
    key_values = [] #cria e inicializa (vazia) uma lista de chaves que contêm valores da chave agrupadora
    list_records = [] #cria e inicializa (vazia) uma lista de registros agrupado pelo valor da chave agrupadora
    for line in data: #lê cada linha (dicionário) de data (lista de dicionários)
        if(line[key] not in key_values): #verifica se o valor da chave agrupadora na linha lida existe dentro da lista de valores da chave agrupadora
            key_values.append(line[key]) #adiciona da lista de valores da chave agrupadora o valor da chave agrupadora
    for i in range(len(key_values)): #verifica o tamanho da lista de valores da chave agrupadora e cria um contador para receber posições desta lista
        records = [] #cria e inicializa (vazia) uma lista para adição dos registros agrupados para cada valor da chave agrupadora
        for line in data: #lê cada linha (dicionário) de data (lista de dicionários)
            if(line[key] == key_values[i]): #verifica se o valor da chave agrupadora da linha lida é igual ao da lista de valores da chave agrupadora na posição do iterador
                records.append(line) #se for, adiciona a linha na lista de registros do valor da chave agrupadora
        list_records.append(records) #após acabar de ver o arquivo para o valor da chave agrupadora, adiciona estes registros na lista de registros agrupados por valores da chave agrupadora
    
    grouped_by_key_values = {} #cria e inicializa (vazio) um dicionário contendo chave (valor da chave agrupadora) e valor (lista de registros contendo o valor da chave agrupadora)
    for i in range (len(key_values)):  #verifica o tamanho da lista de valores da chave agrupadora e cria um contador para receber posições desta lista
        grouped_by_key_values[key_values[i]] = list_records[i] #no dicionário de agrupamento de valores, adiciona os registros do valor da chave agrupadora (value) para o valor da chave agrupadora (chave)
    return grouped_by_key_values # retorna o dicionário contendo chave (valor da chave agrupadora) e valor (registros do valor da chave agrupadora)