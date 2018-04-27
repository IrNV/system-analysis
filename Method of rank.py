"""
    Метод ранга. Каждым экспертом выставляются оценки для всех альтернатив. Затем
оценки нормируются (оценка кадого эксперта делится на сумму всех данных ним оценок, а не на
общую сумму оценок). После чего расчитываем оценку каждой альтернативы как сумму оценок
всех экспертов по данной альтернативе и делим на кол-во экспертов.
"""

count_of_alternatives = 4
count_of_experts = 3
matrix_of_marks = [[3, 2, 4, 1],
                   [1, 4, 3, 2],
                   [2, 3, 4, 1]]


normalize_matrix = []
for marks in matrix_of_marks:
    normalize_matrix.append([mark / sum(marks) for mark in marks])

print(normalize_matrix)

result = []
for i in range(count_of_alternatives):
    result.append((i + 1, sum(marks[i] for marks in normalize_matrix) / count_of_experts))

print(result)
