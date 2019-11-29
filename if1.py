"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

age = int(input("Введите Ваш возраст: "))

def occupation_determiner(age):

    work = "Вы работаете."
    retirement = "Вы на пенсии."
    baby = "Совсем скоро Вы будете ходить в детский сад, а пока гуляйте, спите и хорошо питайтесь."
    kindergarten = "Вы учитесь в детском саду."
    school = "Вы учитесь в школе."
    university = "Вы учитесь в ВУЗе."
    sex_error = "Неверно указан пол. Попробуйте сначала."
    congrats = "Поздравляю! Вы неплохо сохранились. Отдыхайте."
    age_error = "Ошибка! Возраст не может быть отрицательным."

    if 0 <= age < 4:
        return baby
    elif 4 <= age < 7:
        return kindergarten
    elif 7 <= age < 17:
        return school
    elif 17 <= age < 22:
        return university
    elif 22 <= age < 60:
        return work
    elif age >= 100:
        return congrats
    elif age >= 65:
        return retirement
    elif age >= 60:
        sex = str(input("Введите Ваш пол (рус. М/Ж):"))
        if sex == "М" and age < 65 or sex == "Ж" and age < 60:
            return work
        elif sex == "М" and age >= 65 or sex == "Ж" and age >= 60:
            return retirement
        else:
            return sex_error
    else:
        return age_error

print(occupation_determiner(age))
