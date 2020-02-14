class Car:
    def __init__(self):
        self.fc = 7
        self.moduls = []

    def __str__(self):
        return f'данные о машине {self.moduls}'

    def __call__(self, price=None):
        return f'машина {self.model} имеет цену  {price}'


car1 = Car()
car1.model = 'AUDI'
print(car1(6000))
