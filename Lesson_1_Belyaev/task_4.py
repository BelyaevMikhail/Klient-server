"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
my_list = ['разработка', 'администрирование', 'protocol', 'standard']

for word in my_list:
    word = word.encode('utf-8')
    print(word)
    word = word.decode('utf-8')
    print(word)
