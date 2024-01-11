# -*- coding: cp1251 -*-

'''
Создайте класс Vector, который будет создавать объекты типа вектор на плоскости с двумя параметрами (x, y).
Переопределите методы:
1. Сложения - должно выполняться векторное сложение.
2. Умножения - должно выполняться скалярное произведение.
3. Должен быть метод векторного умножения.
-Задание оценивается в 5 баллов

#BONUS: нарисовать вектор используя matplotlib.
'''

class Vector:
    def __init__(self, name, x, y):
        pass
    
    #Операция сложения векторов +
    def __add__(self, other):
        pass

    #Операция скалярного умножения *
    def __mul__(self, other):
        pass
    
    #метод векторного умножения
    def vectorMul(self, other):
        pass

    def look(self):
        pass

'''
A = Point("A", 2, 2)
B = Point("B", 4, 4)

A.look()
B.look()
(A + B).look()
'''

#Решение
class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    #переопределяем операцию сложения
    def __add__(self, other):
        return Point(self.name + other.name,
                     self.x + other.x,
                     self.y + other.y)

    def look(self):
        print(f'{self.name}({self.x},{self.y})')

A = Point("A", 2, 2)
B = Point("B", 4, 4)

A.look()
B.look()
(A + B).look()

