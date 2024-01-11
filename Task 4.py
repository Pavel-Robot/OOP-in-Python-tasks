# -*- coding: cp1251 -*-

'''
Программа получает на вход число N, далее координаты N точек. Выведите координаты точки, 
наиболее удаленной от определенной точки. Для решения этой задачи напишите
метод dist, который возвращает расстояние от точки до начала координат. 
Подсказка: расстояние до точки рассчитывается как dist=((x_1-x_0)^2+(y1-y0)^2)^0.5
-Задача оценивается в 7 баллов

#BONUS: изменить задачу: проверить порождают ли 3 точки плоскость.
#BONUS: изменить задачу: 3 точки от начала координат задают 3 вектора, найти объем параллелепипеда.
#BONUS: изменить задачу: проверить параллельны ли две плоскости.
#BONUS: нарисовать графически через matplotlib любую из бонусных задач.
'''

class Point:
    def __init__(self, name, x, y):
        pass
    
    def __sub__(self, other):
        pass

    def dist(self):
        pass

    def look(self):
        pass


Pointlist = [Point("O", 0, 0),
             Point("A", 2, 2),
             Point("B", 3, 3),
             Point("C", 4, 4),
             Point("D", 5, 5)
            ]

start = Point("StartPoint", 3, 4)
start.look()

nearestPoint = Pointlist[0]
for i in range(len(Pointlist)-1):
    pass

print("Ближайшая точка:")
nearestPoint.look() #B(3,3)



#Решение
class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    #переопределяем операцию вычитания
    def __sub__(self, other):
        return Point(self.name + other.name,
                     self.x - other.x,
                     self.y - other.y)

    def dist(self):
        return (self.x**2 + self.y**2)**(0.5)

    def look(self):
        print(f'{self.name}({self.x},{self.y})')


Pointlist = [Point("O", 0, 0),
             Point("A", 2, 2),
             Point("B", 3, 3),
             Point("C", 4, 4),
             Point("D", 5, 5)
            ]

start = Point("StartPoint", 3, 4)
start.look()

nearestPoint = Pointlist[0]
for i in range(len(Pointlist)-1):
    if (Pointlist[i]-start).dist() > (Pointlist[i+1]-start).dist():
        nearestPoint = Pointlist[i+1]

print("Ближайшая точка:")
nearestPoint.look()