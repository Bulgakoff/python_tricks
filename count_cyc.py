
from itertools import count
from itertools import cycle
# должно быть условие прерывания бесконечнонго цикла
# 1. это по счетчику (индекс, ключ, порядковый номер)
# 2. по значению
# 3. по встроенной фции next()
lst = []
for p in count(3):
    if p > 10:
        break
    else:
        lst.append(p)
print(lst)
iter1 = count(10)
print(type(iter1))

from itertools import cycle

i = 0
for el in cycle("ABCDE"): # для бесконечного зацикливания (нужен счетчик)
    if i > 4:
        break
    print(el, end=' ')
    i += 1
print()
from itertools import cycle

progr_lang = ["python", "java", "perl", "javascript"]
iter = cycle(progr_lang)

print(next(cycle(progr_lang)))# ручное управление next
print(next(iter))# ручное управление next
print(next(iter))# ручное управление next


