"""
 Метод последовательного сравнения:
 альтернативам присваивются начальные веса, где самая лучшая получает 100, а остальные
 относительно нее свои оценки. Выставляется экспертом.
 После этого если есть такая пара альтернатив какая в сумме лучше или равна по баллам
 альтернативе, что стоит выше в рейтингу, то мы коректируем оценку данной альтернативы,
 добавляя, например, константу (в нашем случе 30 для примера)
"""
count = 3
alternatives_weights = [[1, 60], [2, 100], [3, 40]]
alternatives_weights.sort(key=lambda x: x[1], reverse=True)

for i in range(count):
    for j in range(1, count):
        for c in range(2, count):
            if ((alternatives_weights[i][1] <= alternatives_weights[j][1] + alternatives_weights[c][1]) and
                    ((i < j) and (c > j))):
                alternatives_weights[i][1] += 30  # Добавляем любую константку, например 30

weight_sum = sum([value[1] for value in alternatives_weights])
result_data_of_alternative = [[alternative[0], alternative[1] / weight_sum] for alternative in alternatives_weights]
print("Result: ", result_data_of_alternative)
