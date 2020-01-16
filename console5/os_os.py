
import os
try:
    os.remove('t1.txt')
except FileNotFoundError as a:
    print(a)
try:
    os.rename('t2.txt', 't3.txt')
except FileNotFoundError as a:
    print(a)
print('////////////////os.listdir()/////////////')
print(os.listdir('..'))# список Аналогично можно получить
# содержимое каталога, расположенного на один уровень выше относительно текущего:
print('////////////////os.path//////os.path.basename()////Возвращает название файла пути///')
print(os.path.basename(r'C:\Users\user\PycharmProjects\PythonFir\src\py_tricks\giti\console5\seek_tell.py'))
print('////////////////os.path.dirname()//Возвращает часть каталога пути./')
print(os.path.dirname(r'C:\Users\user\PycharmProjects\PythonFir\src\py_tricks\giti\console5\seek_tell.py'))

print('////////////////os.path.exists()///Проверяет, существует ли указанный файл.////')
print(os.path.exists(r'C:\Users\user\PycharmProjects\PythonFir\src\py_tricks\giti\lesson_conManager\corer.py'))

print('////////////////os.path.isdir(), os.path.isfile()///Проверяет, является ли объект папкой или файлом.////')

print(os.path.isdir(r'C:\Users\user\PycharmProjects\PythonFir\src\py_tricks\giti\console5\seek_tell.py'))
print(os.path.isdir(r'C:\Users\user\PycharmProjects\PythonFir\src\py_tricks\giti\console5'))

print('////////////////os.path.join()///Позволяет объединить несколько путей.////')
print(os.path.join(r'C:\Users\user\PycharmProjects\PythonFir\src\py_tricks\giti\console5','seek_tell.py'))

print('////////////////os.path.split()///Разделяет путь на кортеж, содержащий и путь до каталога, и имя файла////')

print(os.path.split(r'C:\Users\user\PycharmProjects\PythonFir\src\py_tricks\giti\lesson_conManager\corer.py'))
