from manim import *
from config import fx, ejes, dx
from utils import a_label, b_label, x1, x2, x3, punto_x1, punto_x2, punto_x3

config.tex_compiler = "pdflatex"
config.output_format = ".pdf"

class EjemploArea(Scene):
    def construct(self):
        area = ejes.get_area(
            fx,
            x_range=[0.2, 2],
            color=(GREEN_B, GREEN_D),
            opacity=1,
        )
        title = Title(r"Area bajo la curva y = f(x) en el intervalo [a, b]", font_size=32)

        self.add(title)
        self.add(ejes, fx, area, a_label, b_label)


class SumaRiemann(Scene):
    def construct(self):
        rects = ejes.get_riemann_rectangles(
            fx,
            x_range=[0.6, 1.3],
            dx=dx,
            color= (TEAL, BLUE_B, DARK_BLUE),
            input_sample_type="right"
            )
        

        self.play(Create(ejes, run_time=5))
        self.play(Create(fx, run_time=2), Create(a_label), Create(b_label))
        self.play(Create(rects, run_time=2))
        self.play(FadeIn(punto_x1), Write(x1), FadeIn(punto_x2), Write(x2), FadeIn(punto_x3), Write(x3))
        self.wait(5)