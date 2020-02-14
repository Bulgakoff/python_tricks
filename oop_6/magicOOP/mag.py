
#
# class MyClass:
#     def __init__(self, param):
#         self.param = param
#
#
# mc = MyClass("text")
# print(mc.param)
# print(mc.param)

# __del__
# В Python разработчик может участвовать как в создании, так и в удалении объекта.

class MyClass:
    def __init__(self, param):
        self.param = param

    def __del__(self):
        print(f"Удаляем объект {self.param} класса MyClass")


mc = MyClass("text")
print(mc.param)
print(mc.param)

del mc

