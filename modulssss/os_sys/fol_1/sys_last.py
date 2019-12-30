
import os
import sys


# name = sys.platform
#
# for i in range(1, 6):
#     path_new = os.path.join(os.getcwd(), f'{name}_{i}')
#     os.mkdir(path_new)
def ping(zz):
    print(zz)


def hello(name, surn):
    print(f'hello {name} {surn}')


def get_info():
    print(os.listdir())  # что бы получить список текущей дирректориии


comm = sys.argv[1]
if comm == 'jopa':
    zz = sys.argv[2]
    ping(zz)
elif comm == 'hui':
    get_info()
elif comm == 'zalupa':
    name = sys.argv[2]
    surn = sys.argv[3]
    hello(name, surn)
