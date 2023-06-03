import model.load.load_data as load
import model.processing.processing_data as processing

list_keys_compras = {'name': str, 'last_name': str, 'age': int, 'sex': str, 'purchase': float, 'year': int, 'payment': str}
file_path_compras = 'model/data/compras_new.txt'

list_keys_alunos = {'nome': str, 'ano': int, 'escola': str, 'nota_semestre_1': float, 'nota_semestre_2': float, 'faltas': int, 'nota_exame': float, 'monitoria': bool}
file_path_alunos = 'model/data/alunos_new.txt'

#list_keys_cars = {'nome': str, 'carro': str, 'valor': float, 'cor': str, 'ano': int, 'cidade': str, 'pago': bool, 'tempo': str}
list_keys_cars = [str, str, float, str, int, str, bool, str]
file_path_cars = 'model/data/carros.txt'
file_path_cars_save = 'model/data/carros_new.csv'

data_separator = ','

######Testes#######

#salvar dados d arquivo na lista de dicionários
header, data = load.load_datafile_to_list_of_dicts(file_path_cars, list_keys_cars, data_separator)
#print(data)

'''#salvar lista de dicionários em um arquivo
load.save_list_of_dicts_to_datafile(header, data, file_path_cars_save, data_separator)'''

'''#Acesso por índice
indexes = [1,2]
range = indexes[2:]
range = [0,[0,1],[0,2,1]]
range = [[None,None,None]]
print(range)
type_of_test = 'Acesso por item índice'
result = processing.locate_data_for_list_of_index(data, range)
print(f'{type_of_test}: \n {result}')
'''

'''#Seleção/Filtragem:
#{'key': key, 'logical_operator': logical_operator, 'value': value}
rules = [{'key': 'cor', 'logical_operator': '==', 'value': 'prata'},
           {'key': 'ano', 'logical_operator': '>=', 'value': 50000},
           {'key': 'pago', 'logical_operator': '==', 'value': True},
           {'key': 'carro', 'logical_operator': '==', 'value': 'Strada'}]
#rules = None
type_of_test = 'Seleção/Filtragem'
result = processing.filter_data(data, rules)
print(f'{type_of_test}: \n {result}')'''


'''#Projeção:
type_of_test = 'Projeção'
keys = ['nome', 'carro', 'valor']
result = processing.projection_data(data, keys)
print(f'{type_of_test}: \n {result}')'''


'''#Atualização:
type_of_test = 'Atualização'
#{'key': key, 'logical_operator': logical_operator, 'value': value}
rules = [{'key': 'valor', 'logical_operator': '<=', 'value': 50000}]
#rules = None
update_list=[{'tempo': 'Neveeeee'}, {'pago': False}]
result, data_updated, count = processing.update_data_by_rule(data, rules, update_list)
print(f'{type_of_test}: \n Records updated: {count} \n\n\n {data_updated} \n')'''

'''#Agrupamento:
type_of_test = 'Agrupamento'
keys = 'cidade'
result = processing.group_data_by_count(data, keys)
print(f'{type_of_test}: \n {result}')'''
