"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    answer=input('Как дела?')
    return answer
 
while True:
    ask_user()
    if ask_user() == 'Хорошо':
        break
