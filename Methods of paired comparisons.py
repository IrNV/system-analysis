"""
    Метод попарного сравнивания альтернатив
"""
table_weight = [[0, 0, 1], [1, 0, 1], [0, 0, 0]]


def calculate_goals_weight(table):
    """
     Вычисление веса каждого критерия
    """
    goals_weights = []
    for marks in table:
        goals_weights.append(sum(marks))

    return goals_weights


def paired_method(table):
    goals_weights = calculate_goals_weight(table)
    normalize_goals_weights = []
    for index, value in enumerate(goals_weights):
        normalize_goals_weights.append((index, value / sum(goals_weights)))  # нормализация весов

    normalize_goals_weights.sort(key=lambda x: x[1], reverse=True)  # сортировка критериев по весам
    return normalize_goals_weights

print(paired_method(table_weight))
