class Person: #
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + ' ' + self.surname


class Teacher(Person):# склад
    def to_teach(self, subj, *pupils):
        for pupil in pupils:
            pupil.to_take(subj)


class Students(Person): # отделы_компании
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledge = []

    def to_take(self, subj):
        self.knowledge.append(subj)


class Subject:
    def __init__(self, *subjects):
        self.subjects = list(subjects)

    def my_list(self):
        return self.subjects


s = Subject('math', 'physics', 'chemistry')
t = Teacher('Ivan', 'Ivanov')
print(t)
p_1 = Students('Petr1', 'Petrov1')
p_2 = Students('Petr2', 'Petrov2')
p_3 = Students('Petr3', 'Petrov3')
print(p_1, p_2, p_3)

t.to_teach(s, p_1, p_2, p_3)
print(p_1.knowledge[0].my_list())
