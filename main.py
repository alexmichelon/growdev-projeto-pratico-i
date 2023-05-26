import model.load.load_data as load

list_keys_compras = {'name': str, 'last_name': str, 'age': int, 'sex': str, 'purchase': float, 'year': int, 'payment': str}
file_path_compras = 'model/data/compras_new.txt'
header, data = load.open_file('model/data/compras_10.csv', 'r')

list_keys_alunos = {'nome': str, 'ano': int, 'escola': str, 'nota_semestre_1': float, 'nota_semestre_2': float, 'faltas': int, 'nota_exame': float, 'monitoria': bool}
file_path_alunos = 'model/data/alunos_new.txt'
header, data = load.open_file('model/data/alunos_10.csv', 'r')

file_mode = 'w'

data = load.load_data_to_list_of_dicts(data, list_keys_alunos, ',')

#print(people)

file = load.load_list_of_dicts_to_data(header, data, file_path_alunos, file_mode, ',')
print('Acabou!')

