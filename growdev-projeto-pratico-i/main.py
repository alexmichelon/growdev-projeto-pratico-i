import model.load.load_data as load
import model.processing.processing_data as processing
import model.load.save_data as save
import model.assistant.adjust_data as ad

list_keys_compras = [str, str, int, str, float, int, str]
file_path_compras = 'model/data/compras.csv'

list_keys_alunos = [str, int, str, float, float, int, float, bool]
file_path_alunos = 'model/data/alunos.csv'

list_keys_cars = [str, str, float, str, int, str, bool, str, float]
file_path_cars = 'growdev-projeto-pratico-i/growdev-projeto-pratico-i/model/data/carros.txt'
file_path_cars_save = 'model/data/carros_new.csv'

data_separator = ','

######Testes#######

#salvar dados d arquivo na lista de dicionários
header, data = load.load_datafile_to_list_of_dicts(file_path_cars, list_keys_cars, data_separator)
#print(data)

'''#salvar lista de dicionários em um arquivo
save.save_list_of_dicts_to_datafile(header, data, file_path_cars_save, data_separator)'''

'''#Acesso por índice
indexes = [1,2]
range = indexes[2:]
#range = [[0],0,[0,1],[0,2,1]]
range = [[1495,1500,None],0,None,63,[50,60,3]]
#range = [0,[0],[1,3],[0,20,2],2,3,[12,52,3]]
type_of_test = 'Acesso por item índice'
indexes, located_data = processing.locate_data_for_list_of_index(data, range)
print(f'{type_of_test}: \n {indexes}')
#print(f'{type_of_test}: \n {indexes}\n\n {located_data}')'''


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

'''#Atualização por índice:
type_of_test = 'Atualização por Índice'
indexes = [0,3,[0,3,2]]
update_list=[{'ano': 'XXXXXXXXX'}, {'sobrenome': 'ZZZZZZZZZZZZ'}]
data, indexes, list_data_updated, count_records_updated = processing.update_data_by_indexes(data, indexes, update_list)
print(f'{type_of_test}:\n'
      f'Registros atualizados: {count_records_updated}\n'
      f'Índices atualizados:\n {indexes}\n' 
      f'Resgistros atualizados:\n {list_data_updated}')'''


'''#Atualização por regra:
type_of_test = 'Atualização por Regra'
#{'key': key, 'logical_operator': logical_operator, 'value': value}
rules = [{'key': 'valor', 'logical_operator': '<=', 'value': 50000}]
rules = None
result, data_updated, count = processing.update_data_by_rule(data, rules, update_list)
print(f'{type_of_test}: \n Records updated: {count} \n\n\n {data_updated} \n')'''

'''#Agrupamento:
type_of_test = 'Agrupamento'
keys = 'cidade'
result = processing.group_data_by_count(data, keys)
print(f'{type_of_test}: \n {result}')'''


'''type_of_test = 'Moda'
result = ad.calculate_mode(data, 'pago')
print(f'{type_of_test}: \n {result}')

type_of_test = 'Média'
result = ad.calculate_mean(data, 'dp')
print(f'{type_of_test}: \n {result}')

type_of_test = 'Mediana'
result = ad.calculate_median(data, 'dp')
print(f'{type_of_test}: \n {result}')

type_of_test = 'Variancia'
result = ad.calculate_standard_variance(data, 'dp')
print(f'{type_of_test}: \n {result}')
'''

'''type_of_test = 'Desvio Padrão'
result = ad.calculate_standard_deviation(data, 'dp')
print(f'{type_of_test}: \n {result}')'''

data = ad.remove_null_values(data, 'dp', 'standard_deviation')
print(data)