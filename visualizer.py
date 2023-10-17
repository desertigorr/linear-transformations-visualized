import matplotlib.patches
import matplotlib.path
import matplotlib.pyplot as plt
import numpy as np


# функция для преобразования координат точки через матрицу линейного преобразования
def transform(t_matrix, v):
    v = np.array(v)
    v_new = t_matrix.dot(v)
    return v_new


# сюда вводим матрицу линейного преобразования
matrix = np.array([[1, 2],
                   [0, 1]])

# задаем фигуру точками по координатам
polygon_dots = [(1, 0), (1, 1), (0, 1), (0, 0)]

# массив для преобразованных точек
polygon_transformed = []

for dot in polygon_dots:
    polygon_transformed.append(transform(matrix, dot))


polygon_2 = matplotlib.patches.Polygon(list(polygon_transformed), fill=True, closed=True)
axes = plt.gca()
axes.add_patch(polygon_2)
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid()
axes.set_aspect("equal")
plt.show()
