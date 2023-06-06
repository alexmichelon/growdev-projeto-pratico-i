#abre o arquivo de dados e o divide em cabeçalho e dados
#parâmetros:
# -file_path: caminho do arquivo a ser aberto (em formato diretório: pasta/pasta_1/arquivo.csv)
# -data_separator: separador de cada dado (campo) em cada registro do arquivo de dados
def open_file(file_path: str, data_separator: str):
    '''
    Open a datafile and splits data in header and data.\n\n
    file_patch \n path of the datafile in format ('folder/folder_1/file.csv').\n
    data_separator\n caracter to separate each data in a record of datafile in format (',', ' ', '|', etc.)\n
    return tuple content header (list) and data_list (list) both separated whit data_separator.
    '''
    file = open(file_path, 'r') #abre o arquivo do caminho informado no modo leitura ('r')
    content = file.readlines() #lê as linhas do arquivo de dados e transforma em uma lista
    header = content[0].replace('\n', '').split(data_separator) #atribui o primeiro registro da lista como cabeçalho
    data_list = content[1:] #atribui os demais registros da lista como dados
    return header, data_list #retorna uma tupla com duas listas: cabeçalho e dados

#converte dados em uma lista de dicionários, 
#parâmetros:
# -file_path: caminho do arquivo a ser aberto (formato diretório: pasta/pasta_1/arquivo.csv)
# -list_type_keys: lista de str contendo o tipo de dado de cada coluna do arquivo
# -data_separator: separador de cada dado (campo) em cada registro do arquivo de dados (formato: ',', ' ', '|', etc.)
def load_datafile_to_list_of_dicts(file_path: str, list_type_keys: list[str], data_separator: str):
    '''
    Load datafile to list of dicts. Convert dynamically the datafile records by informed list of data type values\n\n
    file_patch \n path of the datafile in format ('folder/folder_1/file.csv').\n
    list_type_keys \n list contents type value of datafile columns\n
    data_separator\n caracter to separate each data in a record of datafile in format (',', ' ', '|', etc.)\n
    return a tuple content header (list of str) e data (list of dicts).
    '''
    header, data_list = open_file(file_path, data_separator) #abre o aquivo e atribui a primeira linha ao cabeçalho e as demais linhas para data
    data = [] #cria e inicializa (vazia) a lista de dicionários
    for d in data_list: #lê cada linha da lista que contêm os dados (linha lida)
        record = d.split(data_separator)#retira cada separador de dados dos dados e atribui a linha lida no momento a uma lista (record)
        line = {} #cria e inicializa (vazia) o dicionário que vai receber a linha lida
        for index in range (len(list_type_keys)): #cria contador com base no tamanho da lista de tipos de dados (list_type_keys)
            try:
                if(list_type_keys[index] == bool): #verifica se o tipo de dado da posição lida na lista de tipos de valores das colunas é lógico (bool)
                    if(record[index][0].upper() in ('T', 'V', '1') ): #verifica se o dado inicia por T (True), V (Verdadeiro) ou 1 (Verdadeiro): valores normalmente atribuidos a valores lógicos
                        line.setdefault(header[index], True) #insere na linha lida chave (valor do cabeçalho) e valor verdadeiro (True)
                    elif(record[index][0].upper() in ('F', '0') ): #verifica se o dado inicia por T , F (Falso) ou 1 (Falso): valores normalmente atribuidos a valores lógicos
                        line.setdefault(header[index], False) #insere na linha lida chave (valor do cabeçalho) e valor falso (False)
                    else: #senão for nem True ou False
                        line.setdefault(header[index], None)  #insere nulo
                else: #se o valor da chave da lista não for lógico (bool)  
                    line.setdefault(header[index], list_type_keys[index](record[index].replace('\n',''))) #insere na linha lida chave (valor do cabeçalho) e valor ao dicionário: caso tipo de dado for str, retira a quebra de linha
            except ValueError:
                line.setdefault(header[index], None)            
        data.append(line) #adiciona o dicionário line (posições da linha lida) dentro da lista de dicionários
    return header, data #retorna cabeçalho e a lista de dados (cada linha dos dados é um dicionário na lista)