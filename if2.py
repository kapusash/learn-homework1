"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def strings_compare(string1,string2):
    if type(string1) is str and type(string2) is str:
        if string1 == string2:
            return 1
        elif string1 != string2 and string2 == 'learn':
            return 3
        elif string1 != string2 and len(string1) > len(string2):
            return 2
        else:
            return 4
    else:
        return 0

print(strings_compare('python','python'))
print(strings_compare('python!','python'))
print(strings_compare('python','learn'))
print(strings_compare('python','nohtyp'))
print(strings_compare(1,1))
