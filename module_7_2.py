import io
from pprint import pprint
print('Записать и запомнить')
print('--------------------')

def custom_write(file_name, strings):
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')

    for i, string in enumerate(strings, 1):
        byte_position = file.tell()
        file.write(string + '\n')
        strings_positions[(i, byte_position)] = string

    file.close()

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

