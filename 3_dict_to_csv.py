"""
Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    import csv

    dict_1 = [
        {'name':'Igor', 'age': '30', 'job': 'engineer'},
        {'name':'Anna', 'age': '25', 'job': 'wife_of_engineer'},
        {'name':'Tom', 'age': '5', 'job': 'son_of_engineer'},
        {'name':'Mini', 'age': '1', 'job': 'dauther_of_engineer'}
    ]
    dict_2 = [
        {'name':'Alina', 'age': '29', 'job': 'sellor'},
        {'name':'Mark', 'age': '30', 'job': 'hasbund_of_sellor'},
        {'name':'Nil', 'age': '1', 'job': 'dauther_of_sellor'}
    ]

    with open ('user.csv', 'w', encoding= 'utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter = ';')
        writer.writeheader()

        for user in dict_1:
            writer.writerow(user)

    with open ('user.csv', 'a', encoding='utf-8') as f:

        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter = ';')
        
        for user in dict_2:
            writer.writerow(user)         

if __name__ == "__main__":
    main()
