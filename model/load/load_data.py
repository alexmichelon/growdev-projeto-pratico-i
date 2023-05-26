#abre o arquivo de dados
#parâmetros:
# - caminho do arquivo a ser aberto (file_path)
# -modo de uso do arquivo (file_mode). Obs.: informações sobre parâmetros no arquivo INFORMATION.md
def open_file(file_path, file_mode):
    file = open(file_path, file_mode) #abre o arquivo no caminho informado e da forma de uso informada
    content = file.readlines() #transforma os dados do arquivo em uma lista
    header = content[0] #atribui a primeira linha da lista como cabeçalho
    data = content[1:] #atribui as demais linhas da lista como dados a serem trabalhados
    return header, data #retorna duas listas: cabeçalho e dados

#converte dados em uma lista de dicionários, 
#parâmetros:
# -dados do arquivo (data)
# -chaves e valores da lista de campos do arquivo (dict_keys)
# -separador de dados existente no arquivo (data_separador)
def load_data_to_list_of_dicts(data, dict_keys, data_separator):
    list = [] #inicializa a lista de dicionários
    for d in data: #percorre cada linha da lista de dados     
        record = d.split(data_separator) #retira cada separador de dados e atribui a linha do arquivo a uma lista (record)
        line = {} #inicializa o dicionário que vai receber a linha lida
        position = 0 #iterador da posição do valor a ser lido na lista (record)
        for key, value in dict_keys.items(): #busca cada chave e valor existente na lista de campos (dict_keys)
            if(value == str): #se for texto (String)
                line.setdefault(key, value(record[position]).replace('\n','')) #retira a quebra de linha
            elif(value == bool): #se for lógico (booleano)
                if(record[position][0].upper() in ('T', 'V', '1') ): #verifica se o dado inicia por T (True), V (Verdadeiro) ou 1 (Verdadeiro)
                    line.setdefault(key, True) # atribui verdadeiro
                else: #se não encontrar este tipo de caracter
                    line.setdefault(key, False) #atribui falso
            else: #se o valor da chave da lista não for texto (String) ou lógico (booleano)  
                line.setdefault(key, value(record[position])) #atribui chave e valor ao dicionário
            position += 1 #iterar a posição do valor a ser lido na lista (record)
        list.append(line) #após atribuir todos os valores de chave e valor da linha, salva a linha na lista de dados  
    return list # retorna a lista de dados: cada linha dos dados é um dicionário na lista


#converte uma lista de dicionários em um arquivo e o salva 
#parâmetros: 
# -cabeçalho da lista de dicionários (header)
# -lista de dicionários (list_dicts)
# -caminho do arquivo (file_path)
# -modo de uso do arquivo (file_mode). Obs.: informações sobre parâmetros no arquivo INFORMATION.md
# -separador de dados (data_separator)
def load_list_of_dicts_to_data(header, list_dicts, file_path, file_mode, data_separator):
    file = open(file_path, file_mode) #cria o arquivo no caminho informado e seta o tipo de uso do arquivo
    file.write(header) #insere o cabeçalho no início do arquivo
    for dict in list_dicts: #verifica cada dicionário da lista de dicionário
        line = '' #incializa a linha que vai receber dados do dicionário da lista de dicionários
        for value in dict.values(): #verifica cada campo e valor do dicionário da lista de dicionários
            line += str(value) + data_separator #adiciona o valor do dicionário somado ao separador no conteúdo existente da lista
        line = line.rstrip(line[line.rfind(data_separator)]) + '\n' #retira o último separador de dados da linha e adiciona uma quebra de linha ao final da linha
        file.writelines(line) #insere a linha no arquivo
    return file # retorna o arquivo













#agrupa valores de uma lista de dicionários em um dicionário utilizando duas chaves 
def list_dict_group_by_values_two_keys(dictionary_grouped, dictionary, key_group, key_sum):
    dictionary_grouped[dictionary[key_group]] =  dictionary_grouped.get(dictionary[key_group], 0) + dictionary[key_sum]
    return dictionary_grouped

#conta número de ocorrências de valores de uma chave em uma lista de dicionários
def list_dict_count_values_key(dictionary_grouped, dictionary, key_group):
    dictionary_grouped[dictionary[key_group]] =  dictionary_grouped.get(dictionary[key_group], 0) + 1
    return dictionary_grouped

def sum_column_values_whitout_conditions(list_dict, key):
    column_values = 0
    for dict in list_dict:
        column_values += dict[key]
    return column_values

#converte valor float em moeda (Brasil)
def convert_to_currency(value):
    x = "{:,.2f}".format(float(value))
    y = x.replace(',','x')
    z = y.replace('.',',')
    return z.replace('x','.')