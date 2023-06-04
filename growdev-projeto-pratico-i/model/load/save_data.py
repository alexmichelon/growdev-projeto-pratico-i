
#converte uma lista de dicionários em um arquivo e o salva 
#parâmetros: 
# -header: cabeçalho do arquivo de dados
# -list_dicts: lista de dicionários contendo do dados do arquivo de dados
# -file_path: caminho do arquivo a ser aberto (formato diretório: pasta/pasta_1/arquivo.csv)
# -data_separator: separador de cada dado (campo) em cada registro do arquivo de dados
def save_list_of_dicts_to_datafile(header: list[str], list_dicts: list[dict], file_path: str, data_separator: str):
    '''
    Convert list of dicts in a datafile and save in informed path\n\n
    header\n list of str contents the name of colums of datafile\n
    list_dicts\n list of dicts where each dict is a record of datafile\n
    file_patch \n path of the datafile in format ('folder/folder_1/file.csv').\n
    data_separator\n caracter to separate each data in a record of datafile in format (',', ' ', '|', etc.)\n
    '''
    file = open(file_path, 'w') #cria o arquivo no caminho informado no formato escrita ('w')
    file.write(str(header).strip('[]').replace("'", '').replace(' ', '') + '\n') #insere o cabeçalho na primeira linha do arquivo: converte a lista cabeçalho em uma str, retira colchetes do início e final da str e substitui aspas simpels por espaço em branco
    for list_index, dict in enumerate(list_dicts): #lê cada dicionário da lista de dicionários buscando índice e os dados do dicionário lido
        line = '' #inicializa a linha que vai receber dados do dicionário lido da lista de dicionários
        for dict_index, dict_value in enumerate(dict.values()): #lê cada valor do dicionário lido da lista de dicionários buscando índice e dados do dicionário lido
            if dict_index != (len(dict)-1): #verifica se o índice do valor lido é o último do dicionário lido
                line += str(dict_value) + data_separator #adiciona o valor da posição do dicionário lido na linha com o separador
            elif list_index != (len(list_dicts)-1): #veririca se o dicionário lido é o último da lista de dicionários
                line += str(dict_value) + '\n' #último campo do dicionário: adiciona o valor do campo do dicionário lido somado a um caracter quebra de linha
            else: #última linha lida da lista de dicionários
                line += str(dict_value) #adiciona o valor do dicionário lido (último valor do último dicionário lido da lista de dicionários)
        file.write(line) #insere a linha lida no arquivo de dados
    file.close() #fecha a escrita no arquivo de dados