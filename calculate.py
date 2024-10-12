import circle
import square


figs = ['circle', 'square'] 
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size): '''Функция принимает параметры: фигуру (fig), funcфункцию для вычисления(func) и размер фигуры(size) '''
 assert fig in figs''' проверяет , есть ли fig в figs'''
 assert func in funcs '''проверяет, есть ли func в funcs'''

 result = eval(f'{fig}.{func}(*{size})')'''f-строка, которая позволяет вставлять значения переменных в строку.      
 print(f'{func} of {fig} is {result}') '''Выводится строка с результатом вычисления'''

if name == "main": '''Проверка, является ли модуль главным'''
''' задача переменных'''
 func = ''
 fig = ''
 size = list()
'''Цикл ввода фигуры. Вводить надо корректное значение из figs'''
 while fig not in figs:
  fig = input(f"Enter figure name, avaliable are {figs}:\n")
'''Цикл ввода фигуры. Вводить надо корректное значение из funcs'''
 while func not in funcs:
  func = input(f"Enter function name, avaliable are {funcs}:\n")
'''Цикл ввода размера для фигуры. Len(size) должен совпадать с количеством аргументов fig и func'''
 while len(size) != sizes.get(f"{func}-{fig}", 1): '''получение кол-во аргументов из sizes. Если такого нет то возвращается 1'''
'''Ввод размеров через пробел. Возвращается список строк'''
  size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
 
 calc(fig, func, size) '''Вызов функции'''
