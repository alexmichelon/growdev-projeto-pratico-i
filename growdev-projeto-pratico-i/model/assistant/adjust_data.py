import model.processing.processing_data as processing

#calcula a moda dos valores de uma chave (coluna) da base de dados
def calculate_mode(data: list[dict], key: str):
    grouped_by_key_values = processing.group_data_by_count(data, key, None)
    mode = max(grouped_by_key_values, key=grouped_by_key_values.get)
    return mode

#calcula a média dos valores de uma chave (coluna) da base de dados
def calculate_mean(data: list[dict], key: str):
    sum = 0
    count = 0
    for d in data:
        if(d[key] != None):
            sum += d[key]
            count += 1
            print(sum, count)
    mean = sum / count    
    return mean

#calcula a mediana dos valores de uma chave (coluna) da base de dados
def calculate_median(data: list[dict], key: str):
    key_values = []
    for d in data:
        if(d[key] != None):
            key_values.append(d[key]) 
    key_values = sorted(key_values)
    print(key_values)
    median = 0
    if(len(key_values) % 2) == 0:
        median = int(len(key_values) / 2)
        median = (key_values[median-1] + (key_values[median])) / 2
        
    else:
        median = int((len(key_values) - 1) / 2)
        median = key_values[median]
    return median

#calcula a variuância dos valores de uma chave (coluna) da base de dados
def calculate_standard_variance(data: list[dict], key: str):
    variance = 0  
    mean = calculate_mean(data, key)
    for d in data:
        if(d[key] != None):
            variance += ((d[key] - mean) ** 2)
    variance = variance / len(data)
    return variance

#calcula o desvio padrão dos valores de uma chave (coluna) da base de dados
def calculate_standard_deviation(data: list[dict], key: str):
    sd = calculate_standard_variance(data, key)
    sd = sd ** (1/2)
    return sd

#ajusta os valores nulos de uma base de dados com base em uma chave (coluna) e modo de substituição (function)
def remove_null_values(data: list[dict], key: str, function: str):
    if (function == 'mode'):
        value = calculate_mode(data, key)
    elif (function == 'mean'):
        value = calculate_mean(data, key)
    elif (function == 'median'):
        value = calculate_median(data, key)
    elif (function == 'variance'):
        value = calculate_standard_variance(data, key)
    elif (function == 'standard_deviation'):
        value = calculate_standard_deviation(data, key)
    for d in data:
        if(d[key] == None):
            d[key] = value    
    return data