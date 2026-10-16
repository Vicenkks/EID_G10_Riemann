from manim import *
from config import a, b, ejes, fx

config.tex_compiler = "pdflatex"
config.output_format = ".pdf"

a_label = ejes.get_T_label(
    x_val=a,
    graph=fx,
    label=Tex("a").scale(0.7),
    line_color=RED,
    triangle_size=0.1
)

b_label = ejes.get_T_label(
    x_val=b,
    graph=fx,
    label=Tex("b").scale(0.55),
    line_color=PINK,
    triangle_size=0.1
)

x1 = MathTex(r"x_{i-1}", font_size=16).next_to(
    ejes.c2p(0.6, 0),  # coordenada matemática (x=0.6, y=0)
    direction=DOWN,
    buff=0.15
)

punto_x1 = Dot(
    ejes.c2p(0.6, 0),
    color=WHITE,
    radius=0.07,
)

x2 = MathTex(r"x_{i}", font_size=16).next_to(
    ejes.c2p(1, 0),  # coordenada matemática (x=0.6, y=0)
    direction=DOWN,
    buff=0.15,
)

punto_x2 = Dot(
    ejes.c2p(1, 0),
    color=WHITE,
    radius=0.07,
)

x3 = MathTex(r"x_{i}", font_size=16).next_to(
    ejes.c2p(1.3, 0),  # coordenada matemática (x=0.6, y=0)
    direction=DOWN,
    buff=0.15,
)

punto_x3 = Dot(
    ejes.c2p(1.3, 0),
    color=WHITE,
    radius=0.07,
)