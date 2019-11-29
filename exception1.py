"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
question_answer = {
    "Как дела?": "Хорошо",
    "Что делаешь?": "Программирую",
    "Как настроение?": "Отлично!",
    "Что будет завтра?": "Завтра будет завтра" }

def ask_user_dict():
    while True:
        try:
            question = input("Введите вопрос: ")
            print(question_answer.get(question, 'Вопрос отсутствует'))
        except KeyboardInterrupt:
            print('Пока')
            break

ask_user_dict()

