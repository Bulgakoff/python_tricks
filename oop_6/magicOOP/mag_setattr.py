
class MyClass:
    def __setattr__(self, attr, value): # ключ-- > attr
        if attr == "width":
            self.__dict__[attr] = value
            print(f"Атрибут-ключ   == {attr} ")
        else:
            print(f"Атрибут {attr} недопустим")


mc = MyClass()
mc.width = 40
