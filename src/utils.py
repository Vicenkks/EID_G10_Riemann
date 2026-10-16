from manim import *
from config import a, b, n, ejes, fx, valores_x

config.tex_compiler = "pdflatex"
config.output_format = ".pdf"

textos_label = [
    r"0",
    r"\frac{\pi}{2}",
    r"\pi",
    r"\frac{3\pi}{2}",
    r"2\pi",
]

labels = VGroup()
pi_sum = 0
for texto in range(5):
    label = ejes.get_graph_label(
        graph= fx,
        label= MathTex(textos_label[texto]),
        x_val= pi_sum,
        direction= UP,
        dot=True
    )
    pi_sum += PI/2

    labels.add(label)


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

etiquetas_x = VGroup()
puntos_x = VGroup()
lines = VGroup()
etiquetas_p = VGroup()


for i, valor in enumerate(valores_x):
    punto = Dot(
        ejes.c2p(valor, 0),
        color=YELLOW,
        radius=0.06,
    )

    etiqueta = MathTex(
        fr"x_{{{i}}}",
        font_size=20,
    ).next_to(
        punto,
        DOWN,
        buff=0.05,
    )

    puntos_x.add(punto)
    etiquetas_x.add(etiqueta)


for i in range(1, len(valores_x)):
    punto_medio = (valores_x[i - 1] + valores_x[i]) / 2

    etiqueta_medio = MathTex(
        fr"x_{{{i}}}^*",
        font_size=20,
    ).next_to(
        ejes.c2p(punto_medio, 0),
        DOWN,
        buff=0.35,
    )

    linea = DashedLine(
        ejes.c2p(punto_medio, 0),
        ejes.i2gp(punto_medio, fx),
        color=WHITE,
        dashed_ratio=0.85,
    )

    etiquetas_p.add(etiqueta_medio)
    lines.add(linea)