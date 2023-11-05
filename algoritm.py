# Проверяем, можно ли сходить в определенную точку. Условия:
# 1) Координаты не выходят за область двумерного массива
# 2) В точку куда мы хотим сходить уже есть некое значение
def check(x: int, y: int, mass: list) -> bool:
    length = (len(mass[0]), len(mass))
    if (0 <= x < length[0]) and (0 <= y < length[1]) and ((mass[y][x] == 0) or (mass[y][x] == -1)):
        return True
    else:
        return False


# Выводим в консоль двумерный массив
def print_mass(mass: list) -> None:
    for i in mass:
        print(*i)


# Поиск наикратчайшего пути
def BFS(mass, max_step=2):
    step = 1
    # Патерны движения коня на доске
    pattern_x, pattern_y = [1, 2, 2, 1, -1, -2, -2, -1], [-2, -1, 1, 2, 2, 1, -1, -2]
    # Пока не закончится количество шагов ищем путь
    while step < max_step:
        # Проходимся по всему массиву, чтобы найти точки с нужным шагом
        for y in range(len(mass)):
            for x in range(len(mass[0])):
                # Если мы находим, то...
                if step == mass[y][x]:
                    # Ставим во все нужные точки отметки, что он может туда сходить
                    for pat_x, pat_y in zip(pattern_x, pattern_y):
                        tmp_x, tmp_y = x + pat_x, y + pat_y
                        # Если мы можем туда поставить, то...
                        if check(tmp_x, tmp_y, mass=mass):
                            # Если же мы доходим до конца, то возвращаем минимальное количество шагов и массив
                            if -1 == mass[tmp_y][tmp_x]:
                                return step + 1, mass
                            # если нет, то просто продолжаем искать
                            mass[tmp_y][tmp_x] = step + 1
        step += 1
    # Если путь не был найден за n количество шагов, то возвращаем -1
    return -1, mass


# Поиск наикратчайшего пути по готовому массиву от конца до старта
# Внимание: Работает только при условии, что мы нашли путь от начала до конца!
def path_start(mass: list, min_step: int, fin_x: int, fin_y: int):
    # Проверка: Координаты не выходят за область двумерного массива?
    def check_on_size(x_next: int, y_next: int):
        length = (len(mass[0]), len(mass))
        if (0 <= x_next < length[0]) and (0 <= y_next < length[1]):
            return True
        else:
            return False

    x, y = fin_x, fin_y
    # Путь по которому будем идти до старта
    path = [(x, y)]

    # Патерны движения коня на доске
    pattern_x, pattern_y = [1, 2, 2, 1, -1, -2, -2, -1], [-2, -1, 1, 2, 2, 1, -1, -2]
    for i in range(min_step - 1, 0, -1):
        # Проходимся по движению коня
        for pat_x, pat_y in zip(pattern_x, pattern_y):
            tmp_x, tmp_y = x + pat_x, y + pat_y
            # Если можно идти И следующий ход соответствует следующему шагу, то добавляем в путь до старта
            if check_on_size(tmp_x, tmp_y) and mass[tmp_y][tmp_x] == i:
                path.append((tmp_x, tmp_y))
                x, y = tmp_x, tmp_y
    # Возвращаем путь до финиша
    return path[::-1]
