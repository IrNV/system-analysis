"""
    Каждый эксперт выставляет альтернативам свои оценку, а сам эксперт характеризируется
компетентностью в данной области, которая задается числом.
    Что бы узнать оценку
"""


def normalize_competence(experts):
    """
    Функция нормирования компетенций экспертов
    """
    sum_competence = 0
    for expert in experts:
        sum_competence += expert["competence"]
    for expert in experts:
        expert["competence"] /= sum_competence


def expert_assessments():
    count = 3
    experts = [{"competence": 7, "marks": [0.3, 0.6, 0.1]},
               {"competence": 8, "marks": [0.1, 0.6, 0.3]}]

    normalize_competence(experts)  # Нормируем компетентность экпертов

    alternatives = []
    for i in range(count):
        result_marks = 0
        for expert in experts:
            result_marks += expert["competence"] * expert["marks"][i]

        alternatives.append((i + 1, result_marks))

    alternatives.sort(key=lambda x: x[1], reverse=True)

    return alternatives

print(expert_assessments())
