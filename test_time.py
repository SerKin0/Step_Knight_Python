from time import time
import matplotlib.pyplot as plt
import numpy as np

from algoritm import BFS, BFS_recursion, BFS_cycle


def time_fun(function, *args, **kwargs):
    start_time = time()
    try:
        function(*args, **kwargs)
    except None:
        return -1
    end_time = time() - start_time
    return end_time


time_cycles = {}
time_simply = {}
time_recursion = {}

flag = {"c": True, "s": True, "r": True}

for size in range(10, 200):
    # Координаты начала пути коня
    kn_x, kn_y = 0, 0


    def creat_map(size: int) -> list:
        # Координаты конца пути коня
        fn_x, fn_y = size - 1, size - 1

        # Создание двумерного массива/доски
        mass = [[0] * size for _ in range(size)]

        # Ставим начало и конец пути коня на доске
        mass[kn_y][kn_x] = 1
        mass[fn_y][fn_x] = -1
        return mass


    def app(d: dict, ind: int, time: float, name: str):
        if time == -1:
            flag[name] = False
            print(f"Error: {name}, step: {ind}")
            d[ind] = 0
        else:
            if time == 0:
                print(f"Problems: {ind}")
            d[ind] = time

    # Записываем в переменные минимальное количество шагов до финиша и массив со всеми вариантами передвижения
    mass = creat_map(size)
    time_c = time_fun(BFS_cycle, mass, [(kn_x, kn_y)], 1000) if flag["c"] else 0

    mass = creat_map(size)
    time_s = time_fun(BFS, mass, 10000) if flag["s"] else 0

    mass = creat_map(size)
    time_r = time_fun(BFS_recursion, mass, 1, [(kn_x, kn_y)], 10000) if flag["r"] else 0

    app(time_cycles, size, time_c, "c")
    app(time_simply, size, time_s, 's')
    app(time_recursion, size, time_r, "r")

print(f"time_c = {time_cycles}\n"
      f"time_s = {time_simply}\n"
      f"time_r = {time_recursion}")

# Создание списков ключей и значений для каждого словаря
keys_cycles, values_cycles = zip(*time_cycles.items())
keys_simply, values_simply = zip(*time_simply.items())
keys_recursion, values_recursion = zip(*time_recursion.items())

# Построение графика
plt.figure(figsize=(10, 6))

plt.plot(keys_cycles, values_cycles, marker='o', linestyle='-', label='Cycles')
plt.plot(keys_simply, values_simply, marker='s', linestyle='--', label='Simply')
plt.plot(keys_recursion, values_recursion, marker='^', linestyle='-.', label='Recursion')

# Вычисление линии тренда для каждого словаря
z_cycles = np.polyfit(keys_cycles, values_cycles, 1)
p_cycles = np.poly1d(z_cycles)
plt.plot(keys_cycles, p_cycles(keys_cycles), "r--", label='Trend line (Cycles)')

z_simply = np.polyfit(keys_simply, values_simply, 1)
p_simply = np.poly1d(z_simply)
plt.plot(keys_simply, p_simply(keys_simply), "g--", label='Trend line (Simply)')

z_recursion = np.polyfit(keys_recursion, values_recursion, 1)
p_recursion = np.poly1d(z_recursion)
plt.plot(keys_recursion, p_recursion(keys_recursion), "b--", label='Trend line (Recursion)')

plt.title('Сравнение времени выполнения и линии тренда для различных методов')
plt.xlabel('Ключи')
plt.ylabel('Время выполнения')
plt.legend()
plt.grid(True)

plt.show()
