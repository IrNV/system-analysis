"""
    Метод полного попарного сравнения. Эксперты (в нашем случае их 2) выставляют свои оценки
альтернативам. После чего идет подсчет баллов альтернативы по каждому эксперту, как
сумму всех оценок в строке данной алтернативы, например:
для альтернативы № 1 [0, 8/15, 1/15, 14/15] оценка по 1-му эксперту 23/15.
Затем общая оценка альтернативы вычисляется как сумму оценок даанной альтернативы по
каждому из экспертов и делится на 15 как размер шкалы оценки.
"""

count_of_alternatives = 4
first_expert = [[0, 8/15, 1/15, 14/15],
                [7/15, 0, 10/15, 7/15],
                [14/15, 5/15, 0, 3/15],
                [1/15, 8/15, 12/15, 0]]

second_expert = [[0, 7/15, 3/15, 13/15],
                 [8/15, 0, 8/15, 8/15],
                 [12/15, 7/15, 0, 2/15],
                 [2/15, 7/15, 13/15, 0]]

result = []
for i in range(count_of_alternatives):
    result.append((i + 1, (sum(first_expert[i]) + sum(second_expert[i])) / 15))

result.sort(key=lambda x: x[1], reverse=True)
print(result)
