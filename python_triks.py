# 1. обединение листов без циклов.  так СМОТРИ intertools и collections тут оперрациии над последовательностями
lst = [[1, 2], [4, 'bob', 5], [6, 7, 8]]
lst2 = sum(lst, [])
print(lst2)  # [1, 2, 4, 4, 5, 6, 7, 8]
# 2.обмен местами
a, s = 1, 3
a, s = s, a

print(a, s)

# 3. обмен местами при помощи кортежей
for ((q, w), e) in [((1, 2), 4), ((5, 6), 9)]:
    print(q, w, e)
print()
for [[z, x], [r, t]] in [[[1, 3], [2, 4]], [[2, 4], [6, 7]]]:
    print(z, x, r, t)
for [z, x] in [[1, 3], [2, 4], [2, 4], [6, 7]]:
    print(z, x)  # классссссссссссссссссссссссссссссссссс

# срезы
lst = [1, 2, 2, 2, 3, 3]
lst = sum(lst[:3])
print(f'c 0 по 3 индекс не включая 3й sum ===  {lst}')
# 4. распаковывание
lst = [[1, 2], [4, 'bob', 5], [6, 7, 8]]
q, w, e = lst
print(q, w, e)
tup = (1, 2, 3)
z, x, c = tup
print(z, x, c)
dict_my = {'w': 25, "r": "V"}
for p in dict_my.keys():
    dict_my[p] = 55
print(f'---------------{dict_my}')
q, w = dict_my
print(q, w)  # переменную предаются только ключи
q = {1, 2, 3}
w, e, r = q
print(w, e, r)


# 5. тернарный опреатор для ункций
def summ(a, b):
    return a + b


def mult(a, b):
    return a * b


c = False
print((summ if c else mult)(3, 2))
# 6. генератор словаря
q = {i: a ** 2 for i in range(10)}
print(q)
tup = (1, 2, 3, 4)
q = {p: a ** 2 for p in tup}
print(q)
lst = [1, 2, 4, 10, 2, 4, 3, 11]
q = {p: a ** 10 for p in lst}
print(q)
lst_from_dict = [p for p in q]
print(lst_from_dict)  # обратнов в лист но только ключи (значения в выражении вычисляются)

print('# ////////////////////////////////////////////////////////////////')
from functools import reduce

a = [4, 8, 5, 4, 9, 2]
qwe = reduce(lambda q, w: q if q > w else w, a)
print(f'--------------------reduce------------------{qwe}')

qwe = list(map(lambda q: q + 100, a))
print(qwe)

qwe = list(filter(lambda q: q % 2 == 0, a))
print(qwe)

qwe = list(map(lambda q: q % 2 == 0, a))
print(qwe)

qwe = reduce(lambda q, w: q if q > w else w, a)
print(qwe)

# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

lst1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
lst0 = [p for p in lst1 if lst1.count(p) == 1]
print(f'----------------{lst0}')
lst2 = [p for i, p in enumerate(lst1) if lst1.count(p) == 1]
print(lst2)
lst3 = [lst1[i] for i in range(len(lst1)) if lst1.count(lst1[i]) == 1]
print(lst3)
lst4 = list(filter(lambda x: lst1.count(x) == 1, lst1))
print(lst4)
# /////////////////////////////////////
str_1 = [1, 2, 3, 4]
str_2 = [4, 5, 6]
str_3 = [8, 7, 56]
sets = [i + j + k for i in str_1 for j in str_2 for k in str_3]
print(sets)


# ////////////////////////
def generator():
    for el in (10, 20, 30):
        yield el


g = generator()
print(f'-----------{list(g)}')

for el in g:
    print(el)
# //////////partial  - Позволяет создать новую функцию с частичным указанием передаваемых аргументов.////////
from functools import partial


def my_func(param_1, param_2, o):
    return param_1 + param_2 * o


new_my_func = partial(my_func, 10)
print(new_my_func)
print(f'--------------{new_my_func(3, 5)}')
# ////////////////бесконечного цикла набора значения конечно со счетчиком/////////////
from itertools import cycle

с = 0
for el in cycle("ABC"):
    if с > 3:  # не больше 3 итераций
        break
    print(el, end=' ')
    с += 1
    # ////////////////////////////////
    from itertools import cycle

    progr_lang = ["python", "java", "perl", "javascript"]
    iter = cycle(progr_lang)

    print(next(iter))
    print(next(iter))
    print(next(iter))
#
# ceil(N)
# Округлить число N до ближайшего большего числа
# fabs(N)
# Определить модуль числа N
# factorial(N)
# Найти факториал числа N
# floor(N)
# Округлить число вниз
# fmod(a, b)
# Получить остаток от деления a на b
# isfinite(N)
# Является ли N числом
# //////////////////////передача бесконечного цикла на ручное упаравление...........:))))))))
progr_lang = ["python", "java", "perl", "javascript"]
iter = cycle(progr_lang)
print(next(iter))
print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# //////////////////////////////////использование генератора как иттерируемого объекта//////////////
# при использовании генератора значения не хранятся в памяти, а формируются в процессе обращения к ним,
# по мере запроса(вызывается только один раз).......,,////////////////////////////////////////////////////////////////
generator = (param * param for param in range(5))  # кортеж это только иттерируемый объект?

for el in generator:
    print(el)


def generator():
    for el in (10, 20, 30):
        yield el


g = generator()
print(g)

for el in g:
    print(el)
# ///////////////////////////////факториал /////////////////////
n = 4


def fact(nn):
    f = 1
    for i in range(1, nn + 1):
        f = i * f
        yield f


for el in fact(n):
    print(el)
from random import randint, choice, shuffle, sample

# ЛАТЕРЕЯЛАТЕРЕЯЛАТЕРЕЯЛАТЕРЕЯЛАТЕРЕЯЛАТЕРЕЯЛАТЕРЕЯЛАТЕРЕЯЛАТЕРЕЯЛАТЕРЕЯ
# 1. загадать случайное число от 0 до 100
n = randint(0, 100)
print(n)
# . выбрать победителей
p = ['do', 'doa', 'dos', 'dod', 'dof']
pp = randint(0, len(p))
for i in range(len(p)):
    if i == pp:
        print(f'winner {p[i]}')
        break

# /////////////////////choice случайный элемент последвательности /////////////////
pp = choice(p)
print(f'winner {pp}')
# /////////////////////////////sample  выводит случайный  список к из последовательности //////////////////////////////////////////
for i in range(len(p)):
    if i < 3:
        pp = choice(p)
        print(pp)
    elif i == 4:
        break

# ////////////////////////sample ///sample ///sample ///sample ///sample
pp = sample(p, 3)
q, w, e = pp
print(pp)
print(q, w, e)
# 4. премешать список shuffle

p = ['1', '2', '3', '4', '5']
shuffle(p)  # !!!!!!!!!!!!!!!!!!!!!   МЕНЯЕТ САМ СПИСОКК!!   МЕНЯЕТ САМ СПИСОКК!!   МЕНЯЕТ САМ СПИСОКК
print(p)
# /////////////////////////empty forms  и перебор по словарю   и перебор по словарю   и перебор по словарю /////////
goods = []  # goods.append((num, features))
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
# features[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
# analitics[f].append(features[f])
num = 0  # num += 1
for key, value in analitics.items():
    print(key, value)
# /////////////////быстрая сортировка ///////////////////////////////////////////////////////////////////////////////////////////////
qwe = [6, 50, 5, 3, 5, 53]


def qsort_merge(lst):
    if len(lst) < 2:
        return lst
    else:
        # pivot = arr[0]
        low = 0
        high = len(lst) - 1
        mid = (low + high) // 2
        pivot = lst[mid]
        less = [p for p in lst if pivot > p]
        more = [p for p in lst if pivot < p]
        return qsort_merge(less) + [pivot] + qsort_merge(more)


res_qsort_merge = qsort_merge(qwe)
print(res_qsort_merge)

# /////////////////////// последнее число в числе выделяечтся и отсекается распределяясь в списке
nn = 7636
lst5 = []
while nn > 0:
    qwe = nn % 10
    lst5.append(qwe)
    nn //= 10
print(lst5)
