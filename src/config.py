from manim import *

# Plano de cordenadas
ejes = Axes(
    x_range=[0, 2*PI+0.3, 3.14/2],
    y_range=[0, 2, 1],
    x_length=9,
    y_length=5,
    axis_config={"include_numbers": False, "font_size": 13,}
    )

# Puntos para ser representados en PI, PI/2, etc.

# Función f(x) = sen(x)
fx = ejes.plot(
    lambda x: np.sin(x), 
    color=RED,
    x_range=[0, 2*PI],
    use_smoothing=True
    )

a, b = 0, PI
n = 50
dx = (b-a)/n
avance = b/n

valores_x = np.arange(a, b+avance, avance)