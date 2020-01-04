import random
import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf -8') as f:
        f.write(text)  # только один аргумент для записи в файл


def create_folder(name):
    try:
        os.mkdir(name)  #
    except FileExistsError as a:
        print(a)


def filter_folders(only_folders=False):  # когда нужно прояснить муки выбора,
    # отфильтровать результат (возможна тернальная ситуация)
    result = os.listdir()  # а это список папок и файлов
    if only_folders:  # когда only_folders True!!! по папкам
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_fol_files(name):
    if os.path.isfile(name):
        os.remove(name)
    else:
        try:
            os.rmdir(name)
        except FileNotFoundError as s:
            print(s)


def copy_file_fol(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)  # копирование папок copytree
        except FileExistsError as a:
            print(a)
    else:
        shutil.copyfile(name, new_name)  # копирование файлов copyfile


def save_info(message):
    current_time = datetime.datetime.now()
    res = f'---> {current_time} --->{message}'
    with open('log.txt', 'a', encoding='utf -8') as f:
        f.write(res+'\n')



def guess(puzzle):
    min_num = 1
    max_num = 100

    count = 0
    # что бы не было такого   while result != '=':
    # NameError: name 'result' is not defined
    result = None
    while result != '=':
        count += 1
        number = random.randint(min_num, max_num)
        print(number)
        result = input('Сказать какой результат < = или >: ')
        if result == '<':
            print(f'Число {number} меньше чем {puzzle} ')
            min_num = number + 1
            print(f'min_num = {min_num}')

        elif result == '>':
            print(f'Число {number} ,больше чем {puzzle} ')
            max_num = number - 1
        else:
            print('введен ошибочный символ повторите ввод ')

    print(f'Ура победа Число {number} равно  {puzzle} ')
    print(f'Ответ получен за {count} попыток ')
    print('END')


if __name__ == '__main__':
    create_file('texx.txt', 'Some text')
    create_folder('f1')
    filter_folders()
    delete_fol_files('texx3.txt')

    copy_file_fol('folder_4', 'f_5')
    guess(40)
    copy_file_fol('texx.txt', 'texx2.txt')
    save_info('qwe')
