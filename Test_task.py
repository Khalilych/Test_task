import sys
import random

def func(n):
  arrays = []   #задаю главный массив
  lengthes = []   #задаю массив размеров элементов в а

  for i in range(0, n):
    arrays.append([random.randint(1, 2 * n) for k in range(random.randint(1, 2 * n))])  #наполняю главный массив
    lengthes.append(len(arrays[i]))                                                     #наполняю массив размеров
    if lengthes.count(lengthes[i]) != 1:                                               #условие на разные размеры
      arrays[i] = [random.randint(1, 2 * n) for k in range(1, 2 * n + i + 2)]  #переписываю нужные элементы с другим размером, определяемым предыдущими результатами (рандомными, поэтому этот размер тоже технически рандомный)
      lengthes[i] = len(arrays[i])                                                     #переписываю элемент размера

  print('размеры массивов:', lengthes, '\n')  #чисто для удобства, так наглядно видно что размеры массивов разные

  for i in range(0, n):
    if lengthes.count(lengthes[i]) != 1:     #проверка работы того что сверху (можно удалить или закомментировать)
      print(lengthes[i], 'ОШИБОЧКА')


  for i in range(0, n, 2):      #сортировка
    arrays[i].sort(reverse = True)
    if i+1 < n:
      arrays[i+1].sort()
    else:                       #защита от выхода за пределы
      break

  return arrays


print("Введите количество массивов: n = ")
n = int(input()) #задаю количество массивов. Ну и от этого зависят пределы их размеров, ибо на это небыло условия. Не до бесконечного размера же делать

if n < 0:
  print('Введите натуральное число!')
  sys.exit()

print(func(n))
