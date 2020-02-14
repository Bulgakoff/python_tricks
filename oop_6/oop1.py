class Phone:
    # первое и начало исходная точка и чертеж
    # - корструктор (комутаторный узел) от куда поток к объекту):
    def __init__(self, my_model):  # my_model свойство (что знает)
        self.mod_phone = my_model  # self ссылка на будущий объект
        self._seria_number = 5689725
        self._load()  # на момент создания объекта происходит автоматический запуск
        # '_'  это "защищенный " -> _load
        # self.call()
        self.__qwerty = 'qwe'  # пасхалочка веселая супер безопасность__qwerty

    def call(self):  # метод (что умеет) РУЧНОЙ вызов метода
        print(self.mod_phone, 'calling!!!!!!!')  # или сразу к объекту

    def _load(self):  # если естть в конструкторе то запуск только через конструктор
        #  + (автомат запуск )
        print(self.mod_phone, 'loading........................,.............')

    def get_seria_number(self):
        # print(self._seria_number)
        return self._seria_number


my_phone1 = Phone('sony 3100')
# my_phone1._load()  # если естть в конструкторе то запуск только через конструктор
# #  + (автомат запуск )
# my_phone1.call()
# print(my_phone1.get_seria_number())
# print(my_phone1._Phone__qwerty)# пасхалочка веселая
# my_phone1.call()
my_phone2 = Phone('nokia 6600')


# my_phone2.call()__qwerty
class SmartPhone(Phone):
    def sms(self):
        print('smsing/.........../')

    def send_email(self):
        print('emailing/......>>>>>>>>>>>>>>...../')


my_phone3 = SmartPhone('nokia 66661')
my_phone3.send_email()
my_phone1.call()
my_phone2.call()
my_phone3.call()
my_phone1.call()


class IPhone(SmartPhone):
    def __init__(self, my_model):
        # self.mod_phone = my_model  # self ссылка на будущий объект
        # self._seria_number = 5689725
        # self._load()  # на момент создания объекта происходит автоматический запуск
        # self.__qwerty = 'qwe'
        super().__init__(my_model)
        self.show_logo()

    def player(self):
        print('music play !!!!!!!!!!!!!!')

    def browser(self):
        print('browsering')

    def sms(self):
        print('Imasseging  sms')

    def show_logo(self):
        print(self.mod_phone, 'Apple...........loading........loading........loading........>')


iphone1 = IPhone('6')
iphone1.call()
iphone1.sms()


class NextGenerationPhone(IPhone):
    def __init__(self, my_model):
        super().__init__(my_model)  # без self
        self.touch()

    def touch(self):
        print('Touching is working loading/////loading////.........loading.....loading.......')

    def _load(self):
        print(self.mod_phone, 'loading/////loading////.........loading.....loading=========>>>>')


ngp1 = NextGenerationPhone('NEXT_1')


class Player:
    def player_me(self):
        print('Родительский метод Player')


class Navigator:
    def nav_meth(self):
        print('Родительский метод NavigatorNavigatorNavigator')


class Mobile(Player, Navigator):  # кто левее тот главнее
    def mob_method(self):
        print('Родительский метод Player')


# mobile = Mobile()
# mobile.mob_method()
# mobile.nav_meth()
# mobile.player_me()
class Auto:
    def start_auto(self, param1, param2=None):
        if param2 is not None:
            print(param1 + param2)
        else:
            print(param1)


auto1 = Auto()
auto2 = Auto()
auto1.start_auto(10, 70)
auto2.start_auto(10)
