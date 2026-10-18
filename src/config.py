"""Parámetros matemáticos"""

from manim import *

# Intervalo y función
a = 0
b = PI
f = lambda x: np.sin(x)

# tupla para cambiar el valor de n
PARTICIONES = (4, 8, 16, 50)
COLOR_RECTANGULOS = BLUE_D

# Grafico puesto para dejar espacio y poner las formulas
ejes = Axes(
    x_range=[a, b + 0.3, PI / 2],
    y_range=[0, 1.25, 0.5],
    x_length=8.2,
    y_length=4.6,
    axis_config={"include_numbers": False, "font_size": 24},
).shift(LEFT * 2.35 + DOWN * 0.35)

fx = ejes.plot(
    f,
    x_range=[a, b],
    color=RED,
    use_smoothing=True,
)
