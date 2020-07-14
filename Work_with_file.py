cook_book = {}
with open('Чтение данных.txt', encoding = 'utf-8') as f:
    for line in f:
        if line != '\n':
            print(line.rstrip())
        else:
            continue