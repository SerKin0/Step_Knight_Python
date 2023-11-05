import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def animate_knight_moves(x_size, y_size, coords):
    fig, ax = plt.subplots(figsize=(y_size, x_size))

    # Создаем шахматную доску
    squares = [
        [plt.Rectangle((i, j), 1, 1, color='white' if (i + j) % 2 == 0 else 'lightgray')
         for i in range(x_size)] for j in range(y_size)]

    for row in squares:
        for square in row:
            ax.add_patch(square)

    # Функция для обновления доски при передвижении ползунка
    def update(frame):
        x, y = coords[frame]
        knight.set_xy((x, y))

    # Фигура коня
    initial_x, initial_y = coords[0]
    knight = plt.Rectangle((initial_x, initial_y), 1, 1, facecolor='darkgray')
    # Ставим номер хода коня в клетку
    for i, var in enumerate(coords):
        tmp_x, tmp_y = var
        ax.text(tmp_x + 0.5, tmp_y + 0.5, str(i), color='black', fontsize=25, ha='center', va='center')
    ax.add_patch(knight)

    # Оси и метки
    ax.set_xlim(0, x_size)
    ax.set_ylim(y_size, 0)

    # Ползунок для выбора количества ходов
    ax_slider = plt.axes((0.2, 0.03, 0.6, 0.03))
    slider = Slider(ax_slider, 'Step', 1, len(coords), valinit=1, valstep=1)

    # Обновление анимации при изменении ползунка
    def on_slider_changed(val):
        frame = int(slider.val) - 1
        update(frame)
        fig.canvas.draw_idle()

    slider.on_changed(on_slider_changed)

    # Отображаем анимацию
    plt.show()
