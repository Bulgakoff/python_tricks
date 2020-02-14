class Class1:
    def __init__(self, *args):
        self.params = []
        for el in args:  # вместо def __add__
            self.params.append(el)

    def __str__(self):
        return f'{self.params}'

    def __getitem__(self, item):
        return self.params[item]


ddd = {'dddd': 55}
cls1 = Class1(12, 'fgfgfgfg', ddd)
print(cls1)
print(cls1[2])