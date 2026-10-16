from manim import *

# Plano de cordenadas
ejes = Axes(
    x_range=[-5, 5, 3.14],
    y_range=[0, 3, 1],
    x_length=9,
    y_length=5.5,
    axis_config={"include_numbers": True, "font_size": 13,},
    )

# Puntos para ser representados en PI, PI/2, etc.

# Función f(x) = sen(x)
fx = ejes.plot(
    lambda x: np.sin(x), 
    color=RED,
    x_range=[-5, 5],
    use_smoothing=True
    )

a, b = 0.2, 2
dx = 0.4
