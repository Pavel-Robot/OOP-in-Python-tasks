# -*- coding: cp1251 -*-

'''
Создайте классы наследники от родительского класса Human (человек): 
1. Student (студент) с атрибутами принадлежности к группе (group), 
2. Elder (староста)
3. Teacher (преподаватель)
-Задача оценивается в 4 балла

#BONUS: используя Pandas сделайте красивый вывод табличку
'''

class Human:
    def __init__(self, name):
        pass

    def lookName(self):
        print(f'My name is {self.name}')

    def whoIam(self):
        print(f'I am human')

class Student:
    group = "None"

    def setGroup(self, nameGroup = "None"):
        pass

    def lookGroup(self):
        print(f'My group is {self.group}')

    def whoIam(self):
        print(f'I am student')

class Elder:
    pass

class Teacher:
    degree = "None"

    def setDegree(self, nameGroup = "None"):
        pass

    def lookDegree(self):
        print(f'My degree is {self.degree}')

    def whoIam(self):
        print(f'I am teacher')

Pasha = Student("Pasha")
Masha = Elder("Masha")
Alex = Teacher("Alexandr")

Pasha.lookName()
Pasha.setGroup("BMT22-01")
Pasha.lookGroup()
Pasha.whoIam()
print("--------------------")

Masha.lookName()
Masha.setGroup("JSK22-02")
Masha.lookGroup()
Masha.whoIam()
print("--------------------")

Alex.lookName()
Alex.setDegree("Doctor of Technical Sciences")
Alex.lookDegree()
Alex.whoIam()



#Решение
class Human:
    def __init__(self, name):
        self.name = name

    def lookName(self):
        print(f'My name is {self.name}')

    def whoIam(self):
        print(f'I am human')

class Student(Human):
    group = "None"

    def setGroup(self, nameGroup = "None"):
        self.group = nameGroup

    def lookGroup(self):
        print(f'My group is {self.group}')

    def whoIam(self):
        print(f'I am student')

class Elder(Student):
    def whoIam(self):
        print(f'I am elder')

class Teacher(Human):
    degree = "None"

    def setDegree(self, nameGroup = "None"):
        self.degree = nameGroup

    def lookDegree(self):
        print(f'My degree is {self.degree}')

    def whoIam(self):
        print(f'I am teacher')

Pasha = Student("Pasha")
Masha = Elder("Masha")
Alex = Teacher("Alexandr")

Pasha.lookName()
Pasha.setGroup("BMT22-01")
Pasha.lookGroup()
Pasha.whoIam()
print("--------------------")

Masha.lookName()
Masha.setGroup("JSK22-02")
Masha.lookGroup()
Masha.whoIam()
print("--------------------")

Alex.lookName()
Alex.setDegree("Doctor of Technical Sciences")
Alex.lookDegree()
Alex.whoIam()


#BONUS: используя Pandas сделайте красивый вывод табличку