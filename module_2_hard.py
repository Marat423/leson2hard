n = int(input('Введите число: от 3 до 20! '))  # Прошу вести число
def password(): # Создаю функцию

    pas = '' # создаем переменую со строковым типом
    if n < 3 or n > 20:  # проверяем число
        print('Не то число.')
    else:   # continue
        for i in range(1, 21):  # цикл
             for j in range(1, 21):  # внутрений цик
                if n % (i + j) == 0 and j > i: # проверяем числа без остатка
                    pas += str(i) + str(j) # добавляем в переменную
                    continue

    return pas  #возврашаем
#print(pas)
result = password()
print(result)