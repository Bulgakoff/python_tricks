# функция для создания файла

import os


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.writelines(text)


def create_fol(name):
    os.mkdir(name)


def get_list(fol_only=False):
    result = os.listdir()
    if fol_only:
        result = [f for f in result if os.path.isfile(f)]  # если иттератор f это файл (папка - .isdir(f))
    return result


if __name__ == '__main__':
    create_file('test.txt', 'dddddddddddddd')
    try:
        create_fol('fol_3')
    except FileExistsError as a:
        print(a)
    print(get_list())
