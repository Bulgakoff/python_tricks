class Car:
    def __init__(self):
        self.modules = []  # тут получается результат какой то
        self.f_c = 10
    def __add__(self, other):
        self.modules.append(other)# это когда нужно добавить не экземпляр класса

    def __str__(self):  # всегда стринговый формат перед принтом
        return f'авто с модулями {"||||".join(self.modules)}'  # всегда return

    def __setattr__(self, key, value):  # =  # =  # =  # =  # =  # =  # =  # =  # =
        # print(f'добвляю по ключу {key} значение {value}')
        # super().__setattr__(key, value)
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.modules[item]  # если принт то нужен return

    def __call__(self, price = None ):
       print(f'Машина {self.model} с типом коробки {self.type_box}  опциями {self.modules} и ценой {price}' )
    def __eq__(self, other):
        return self.f_c == other

print('...........////////////////////////////////внешний код много///////////////////////////' )
my_car = Car()
my_car + 'теплый руль'
my_car + 'теплый пол'
my_car + 'теплый потолок'
print(my_car.modules)
print(f'return передает из  __str__ {my_car}')
print('# //////__setattr__//////__setattr__//////__setattr__////////////////////')
my_car.model = 'BMW'# по [ключу -> model]  вставка значения = 'BMW'
my_car.type_box = 'automat'
print(my_car.model)
print(my_car.type_box)
print('# //////__getitem__/////__getitem__/////__getitem__/////__getitem__///////////')
print(f'return передает из def __getitem__ {my_car[2]}')  # вызываем системный метод def __getitem__
a = 1  # a = 1 + 2
print(a.__add__(2))
print('# ////////////////__call__////////__call__////////__call__////////__call__/////////')
my_car(7000)
print('////////__eq__////__eq__////__eq__////__eq__////__eq__////__eq__///////////')
print('Расход нормальный' if my_car ==7 else 'не норма ')
print(my_car)
