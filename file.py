with open('referat.txt', 'r', encoding='utf-8') as file_:
    content = file_.read()
    print(f'Длина считанного: {len(content)} символ\символов')
    x = content.split()
    x = len(x)
    print(f'Количество слов: {x}')
    content = content.replace('.', '!')
with open('referat2.txt', 'w', encoding='utf-8') as file_:
    file_.write(content)



