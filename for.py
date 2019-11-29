"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school_scores = [
    {'school_class': '1а', 'scores': [5,4,5,5,5]},
    {'school_class': '1б', 'scores': [5,4,4,5,5,3,4,5]},
    {'school_class': '2г', 'scores': [5,5,5,5,4,2,1,3,4,5]},
    {'school_class': '2д', 'scores': [3,4,4,4,4,5]},
    {'school_class': '3a', 'scores': [1,3,3,5,4,4,3]},
    {'school_class': '4a', 'scores': [3,4,4,5,2,5,5,5]},
    {'school_class': '5б', 'scores': [3,3,3,4,2]},
    {'school_class': '6в', 'scores': [3,3,3,3,3,1,2,3]}
    ]

def average_calc(scores): # функция расчета среднего балла по классам
    average_calc_value = 0
    scores_count = 0
    for score in scores: # считаем сумму и количество баллов
        average_calc_value += score
        scores_count += 1
    return int(round(average_calc_value/scores_count,0))

school_common_score = 0
school_class_count = 0

for school_class in school_scores:
    print(f'Класс {school_class["school_class"]}, средний балл: {average_calc(school_class["scores"])}')
    school_common_score += average_calc(school_class["scores"])
    school_class_count += 1

print(f'Общий балл по всем классам школы: {int(round(school_common_score/school_class_count))}')
