import os
import sys

print(os.name)  # имя операционной системы
print(os.getcwd())  # теккущее место
# path_curr = os.path.join(os.getcwd(), 'fol_1')# определили путь у текущего модуля от куда вызвали, именовали папку
# os.mkdir(path_curr)
# print(sys.argv[0])
for arg in sys.argv:
    print(arg, end=' ')
    print(type(arg))
