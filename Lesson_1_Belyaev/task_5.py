"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

ping_website = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for website_nou in ping_website:
    ping = subprocess.Popen(website_nou, stdout=subprocess.PIPE)
    i = 0
    for line in ping.stdout:
        if i < 10:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            print(line.decode('utf-8'))
            i += 1
