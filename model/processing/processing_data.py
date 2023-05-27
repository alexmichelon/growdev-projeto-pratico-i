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
    