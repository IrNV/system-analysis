"""
    Метод преимуществ.
Каждый эксперт выставляет оценки n альтернативам, где 1 - самая лучашя по его мнения,
а n самая худшая оценка. Затем строим модифицированную матрицу, где каждый элемент
заменяется на n - оценка эксперта. После чего находится общая оценка альтернативы путем
суммирования оценок данной альтренативы каждым экспертом в модифицированной матрице.
На последнем шаге идет нормирование результатов.
"""


def modify_weight(weights, count_of_alternatives):
    """
    Модифицируем веса путем замены текущего веса на (n - текущий вес), где
    n - кол-во альтернатив
    """
    modified_weights = []
    for expert_marks in weights:
        modified_weights.append([count_of_alternatives - mark for mark in expert_marks])

    return modified_weights


def calculate_sum_of_marks(modified_weights):
    """
    Находим сумму всех оценок
    """
    sum_of_marks = 0
    for marks in modified_weights:
        sum_of_marks += sum(marks)

    return sum_of_marks


def superiority_method():
    count_of_alternatives = 6
    weights = [[1, 5, 4, 2, 6, 3],
               [3, 4, 1, 6, 5, 2],
               [5, 2, 4, 6, 3, 1]]

    modified_weights = modify_weight(weights, count_of_alternatives)
    print("Modified weights:", modified_weights)

    sum_of_marks = calculate_sum_of_marks(modified_weights)
    print(sum_of_marks)

    result = []
    for i in range(count_of_alternatives):
        result.append((i + 1, sum(marks[i] for marks in modified_weights) / sum_of_marks))

    result.sort(key=lambda x: x[1], reverse=True)

    return result

print("Result:", superiority_method())
