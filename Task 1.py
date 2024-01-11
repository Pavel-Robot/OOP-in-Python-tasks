# -*- coding: cp1251 -*-

'''
Создайте класс R2Geometry, который будет считать периметр
и площадь квадрата при создании экземпляра класса.
-Задача оценивается в 4 балла

#Bonus: Нарисуйте этот квадрата в виде графа через NetworkX (также задайте цвет и название)
'''

class R2Geometry:
    def __init__(self, lenA):
        pass

    def SquareLen(self, lenA):
        pass
    
    def SquareArea(self, lenA):
        pass

SquareObj1 = R2Geometry(10)

print("Экземпляр класса SquareObj1")
print("lenA = ",SquareObj1.lenA, " m") #10
print("SquareLenght = ", SquareObj1.SquareLenght, " m") #40
print("SquareArea = ", SquareObj1.SquareArea, " m^2") #100


#Решение
class R2Geometry:
    def __init__(self, lenA):
        self.lenA = lenA
        self.SquareLenght = self.SquareLen(self.lenA)
        self.SquareArea = self.SquarePlace(self.lenA)

    def SquareLen(self, lenA):
        return 4*lenA
    
    def SquarePlace(self, lenA):
        return lenA**2

SquareObj1 = R2Geometry(10)


print("Экземпляр класса SquareObj1")
print("lenA = ",SquareObj1.lenA, " m")
print("SquareLenght = ",SquareObj1.SquareLenght, " m")
print("SquareArea = ",SquareObj1.SquareArea, " m^2")

#bonus: Нарисуйте этот квадрата в виде графа через NetworkX (также задайте цвет и название)