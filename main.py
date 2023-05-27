import model.load.load_data as load
import model.processing.processing_data as processing

list_keys_compras = {'name': str, 'last_name': str, 'age': int, 'sex': str, 'purchase': float, 'year': int, 'payment': str}
file_path_compras = 'model/data/compras_new.txt'
header, data = load.open_file('model/data/compras_10.csv', 'r', ',')

list_keys_alunos = {'nome': str, 'ano': int, 'escola': str, 'nota_semestre_1': float, 'nota_semestre_2': float, 'faltas': int, 'nota_exame': float, 'monitoria': bool}
file_path_alunos = 'model/data/alunos_new.txt'
header, data = load.open_file('model/data/alunos.csv', 'r', ',')

list_keys_cars = {'nome': str, 'carro': str, 'valor': float, 'cor': str, 'ano': int, 'pago': bool}
file_path_cars = 'model/data/carros_new.txt'
header, data = load.open_file('model/data/carros.txt', 'r', ',')

file_mode = 'w'

data = load.load_data_to_list_of_dicts(data, list_keys_cars, ',')

#file = load.load_list_of_dicts_to_data(header, data, file_path_alunos, file_mode, ',')
#print('Acabou!')

range = [2]
#dados = [0,1,2,3,4,5,6,7,8,9,10]
data_located = processing.locate_data(data, range)
#print(f'Dados localizados:\n {data_located}')
#print(f'Dados localizado:\n {data[100]}')

#{'key': key, 'logical_operator': logical_operator, 'value': value, 'type_value': type}
filters = [{'key': 'cor', 'logical_operator': '==', 'value': 'prata', 'type_value': str},
           {'key': 'ano', 'logical_operator': '>', 'value': '2000', 'type_value': int},
           {'key': 'pago', 'logical_operator': '==', 'value': 't', 'type_value': bool}]

found_data = processing.filter_data(data, filters)

print(f'Carros filtrados: \n {found_data}')
print(header)