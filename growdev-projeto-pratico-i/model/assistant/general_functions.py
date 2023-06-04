#compara se o valor informado é None parta parâmetros na função for in range
# -data: lista de dicionário de dados
# -parameter: tipo do parâmetro verificado
# -value: valor verificado
def compare_none_value_for_in_range(data: list[dict], parameter: str, value: any):
    '''
    Compare if informed value is None and assign a value that permited slicing in data.\n\n
    data\n list of data(dict): each data line of the file.\n
    parameter\n a str that informed parameter of for in range function.\n
    value\n value to compare: if None, change value to valid slicing value.
    '''
    if value == None: #verifica se o valor informado é igual a None
        if parameter == 'start': #verifica se o parâmetro informado é 'start'
            value = 0 #se valor é None e parâmetro for 'start', atribui valor zero
        elif parameter == 'stop': #verifica se o parâmetro informado é 'stop'
            value = len(data) #se valor é None e parâmetro for 'stop', atribui valor posição final da lista de dicionário de dados (slicing formato [start:])
        elif parameter == 'step': #verifica se o parâmetro informado é 'step'
            value = 1 #se valor é None e parâmetro for 'step', atribui valor 1 (slicing) (slicing formato [start:stop:] ou [start::])
    return int(value)  #retorna valor para o parâmetro diferente de None


#compara dois valores com um operador lógico (feita em aula)
def compare_values_whit_logical_operator(value1: str, logical_operator: str, value2: any):
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