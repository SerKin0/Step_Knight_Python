from time import time

from algoritm import BFS, print_mass, path_start, BFS_recursion, BFS_cycle
from visual import animate_knight_moves

# Размеры доски
size_x, size_y = 100, 100
# Координаты начала пути коня
kn_x, kn_y = 2, 0
# Координаты конца пути коня
fn_x, fn_y = 99, 99

# Создание двумерного массива/доски
mass = [[0] * size_x for _ in range(size_y)]

# Ставим начало и конец пути коня на доске
mass[kn_y][kn_x] = 1
mass[fn_y][fn_x] = -1

# Записываем в переменные минимальное количество шагов до финиша и массив со всеми вариантами передвижения
start_time = time()
min_step, mass = BFS_cycle(mass, [(kn_x, kn_y)], 1000)
print(f"Время выполнения алгоритма поиска: {time() - start_time}")

# Выводим полученные данные из функции BFS(...)
print(f"Минимальное количество шагов: {min_step}")
print_mass(mass)

# Находим путь от конца до начала
path = path_start(mass, min_step, fn_x, fn_y)

# Запускаем окно с демонстрацией наикратчайшего пути до финиша, если это возможно
if min_step != -1:
    animate_knight_moves(size_x, size_y, path)
else:
    print("Создание доски не возможно, т.к. конь не смог дойти до финиша")
