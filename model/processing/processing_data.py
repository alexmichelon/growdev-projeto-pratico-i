#retorna registro conforme lista de índices repassado
def locate_data(data=list, index=list):  
    try:
        if len(index) == 0:
            print('error in function locate_data: parameter "index" must be informed')
            return []
        elif len(index) == 1:  
            return data[index[0]]
        elif len(index) == 2:
            return data[index[0]:index[1]]
        else:
            return data[index[0]:index[1]:index[2]]
    except IndexError as error:
        print(f'index not found: {error}')
        return []

#compara dois valores com um operador lógico
def compare_values(value1, logical_operator, value2):
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

#filtra dados considerando um campo, um valor e um operador lógico
def filter_data_old(data, key=list, logical_operator=list, value=list):
    found_data = []
    for line in data:
        if compare_values(line[key], logical_operator, value):
            found_data.append(line)
    return  found_data 

#filtra dados considerando uma lista de dicionários contendo em dicionários dados de filtragem filter_fata = [{'key': key, 'logical_operator': logical_operator, 'value': value, 'type_value': type}]
def filter_data(data, comparisions=list):
    found_data = []
    for line in data:
        for index, comparision in enumerate(comparisions):
            if(comparision['type_value'] == bool):
                if(str(comparision['value'])[0].upper() in ('T', 'V', '1')):
                    comparision['value'] = True
                else:
                    comparision['value'] = False
            if compare_values(line[comparision['key']], comparision['logical_operator'], comparision['type_value'](comparision['value'])) == False:
                break
            if index == (len(comparisions)-1):
                found_data.append(line)
    return  found_data 