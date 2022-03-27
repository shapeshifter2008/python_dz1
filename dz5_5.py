from time import perf_counter_ns

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# Тест скорости = 4291
start = perf_counter_ns()
result = [el for el in src if src.count(el) == 1]
end = perf_counter_ns()
print(result, end - start)

# Тест скорости = 3792 (может быть на равне с прошлым)
start = perf_counter_ns()
result = []
for num in src:
    if (src.count(num) == 1):
        result.append(num)

end = perf_counter_ns()
print(result, end - start)

# Тест скорости = 3041 (всегда быстрее прошлых в среднем на 20%)
# Локально самый быстрый вариант
start = perf_counter_ns()
result = []
for num in src:
    if num in result:
        result.remove(num)
        continue

    result.append(num)

end = perf_counter_ns()
print(result, end - start)