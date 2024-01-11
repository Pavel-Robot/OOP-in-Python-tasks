# -*- coding: cp1251 -*-

'''
Задание на стек. Необходимо найти максимум в стеке после последовательности команд (после команды max).
Последовательности команд:

k1 = ['push 2', 'push 1', 'max', 'pop', 'max']
k2 = ['push 1', 'push 2', 'max', 'pop', 'max']
k3 = ['push 2', 'push 3', 'push 9', 'push 7', 'push 2',  'max', 'max', 'max', 'pop', 'max']
k4 = ['push 1', 'push 2', 'push 3', 'push 4', 'max', 'pop', 'max']

Подсказка: необходимо использовать два стека в одном классе.
-Задача оценивается в 5 баллов

#BONUS: нарисовать графически через matplotlib любую из бонусных задач.
'''

import numpy as np

k1 = ['push 2', 'push 1', 'max', 'pop', 'max']
k2 = ['push 1', 'push 2', 'max', 'pop', 'max']
k3 = ['push 2', 'push 3', 'push 9', 'push 7', 'push 2',  'max', 'max', 'max', 'pop', 'max']
k4 = ['push 1', 'push 2', 'push 3', 'push 4', 'max', 'pop', 'max']

class Stack:
    #инициализируем массив длинной size
    def __init__(self, size):
        pass
    
    #Пустой ли стек? Да/Нет
    def isEmpty(self): 
        pass

    #Выполнение операции затолкнуть (push) означает запоминание элемента в
    #позиции массива, указываемой индексом верхушки стека, а
    #затем увеличение этого индекса на единицу
    def push(self, x):
        pass
    
    #Выполнение операции вытолкнуть (pop)
    #означает уменьшение индекса на единицу
    #и извлечение элемента, обозначенного этим индексом, и стирание значения с верхушки в массиве
    def pop(self):
        pass
        
    #Что лежит на верхушке стека?
    def TopElement(self):
        pass

    #Что лежит в начале стека?
    def FirstElement(self):
        pass

    #Чтение стека
    def printStack(self):
        pass

#Обертка для двух стеков
class StackWithMax():
    def __init__(self, size):
        pass

    def push(self, x):

        if self.stack1.isEmpty():
            pass
        else:
            self.stack1.push(x)
            #Если размер стека больше 1 элемента, то можно уже сравнивать и находить максимум
            if self.stack2.TopElement() < x:
                pass
            else:
                pass
        
    def pop(self):
        if self.stack1.isEmpty():
            return 0
        else:
            pass
    
    def maximum(self):
        print()

comands = ['push', 'pop', 'max']

stack = StackWithMax(10) #Стек по кол-ву операций

for k in k1:
    s = k.split()

    if s[0] == comands[0]:
        stack.push(int(s[1]))
    elif s[0] == comands[1]:
        stack.pop()
    else:
        stack.maximum()


#Решение
class Stack:
    #инициализируем массив длинной size
    def __init__(self, size):
        self.arr = np.zeros(size, dtype=int)
        self.top = 0 #начальный индекс в стеке
        self.maximum = 0
    
    #Пустой ли стек? Да/Нет
    def isEmpty(self): 
        return self.top == 0

    #Выполнение операции затолкнуть (push) означает запоминание элемента в
    #позиции массива, указываемой индексом верхушки стека, а
    #затем увеличение этого индекса на единицу
    def push(self, x):
        #print("Push=>Вставка значения x: ", x, " в позицию top:", self.top)

        #Проверяю на максимум в стеке
        #if self.isEmpty():
        #    self.maximum = x
        #else:
        #    if self.maximum < x:
        #        self.maximum = x
        #print("===>Push -> max:" + str(self.maximum))

        self.arr[self.top] = x
        self.top+=1
    
    #Выполнение операции вытолкнуть (pop)
    #означает уменьшение индекса на единицу
    #и извлечение элемента, обозначенного этим индексом, и стирание значения с верхушки в массиве
    def pop(self):
        self.top-=1
        buf = self.arr[self.top]
        #print("Pop=>Cнять значение сверху x: ", buf, " с позиции top:", self.top)

        #Проверяю на максимум в стеке
        #if self.maximum > buf:
        #    self.maximum = self.arr[self.top]
        #print("===>Pop -> max:" + str(self.maximum))

        return self.arr[self.top+1]

    def TopElement(self):
        return self.arr[self.top-1]

    def FirstElement(self):
        return self.arr[0]+1

    def Maxim(self):
        print(self.maximum)

    #Чтение стека
    def printStack(self):
        for t in range(len(self.arr)):
            print(f'top={t}, value = {self.arr[t]}')

#Обертка для двух стеков
class StackWithMax():
    def __init__(self, size):
        self.stack1 = Stack(size)
        self.stack2 = Stack(size)

    def push(self, x):

        if self.stack1.isEmpty():
            self.stack1.push(x)
            self.stack2.push(x)
        else:
            self.stack1.push(x)
            #Если размер стека больше 1 элемента, то можно уже сравнивать и находить максимум
            if self.stack2.TopElement() < x:
                self.stack2.push(x)
            else:
                self.stack2.push(self.stack2.TopElement())
        
    def pop(self):
        if self.stack1.isEmpty():
            return 0
        else:
            self.stack1.pop()
            self.stack2.pop()
    
    def maximum(self):
        print(self.stack2.TopElement())

comands = ['push', 'pop', 'max']

stack = StackWithMax(10) #Стек по кол-ву операций

for k in k4:
    s = k.split()
    #print(s)

    if s[0] == comands[0]:
        stack.push(int(s[1]))
    elif s[0] == comands[1]:
        stack.pop()
    else:
        stack.maximum()
