from manim import *
from config import fx, ejes, dx, a, b
from utils import a_label, b_label, etiquetas_x, puntos_x, lines, etiquetas_p, labels

config.tex_compiler = "pdflatex"
config.output_format = ".pdf"

class EjemploArea(Scene):
    def construct(self):
        area = ejes.get_area(
            fx,
            x_range=[a, b],
            color=(GREEN_B, GREEN_D),
            opacity=1,
        )
        title = Title(r"Area bajo la curva y = f(x) en el intervalo [a, b]", font_size=32)

        self.play(FadeIn(title, run_time= 5))
        self.wait(6)
        self.play(Create(ejes, run_time=4), Create(fx, run_time=4), FadeIn(labels, run_time= 10), FadeIn(a_label, run_time = 10), FadeIn(b_label, run_time = 10))
        self.wait(20)
        self.play(Create(area, run_time=4))


class SumaRiemann(Scene):
    def construct(self):
        title = Title(r"Area bajo la curva y = f(x) en el intervalo [a, b]", font_size=32)
        area = ejes.get_area(
            fx,
            x_range=[a, b],
            color=(GREEN_B, GREEN_D),
            opacity=0.4,
        )
        
        rects = ejes.get_riemann_rectangles(
            fx,
            x_range=[a, b],
            dx=dx,
            color= DARK_BLUE,
            input_sample_type="center",
            fill_opacity=0.4
            )
        

        self.play(FadeIn(title, run_time= 5))
        self.wait(6)
        self.play(Create(ejes, run_time=4), Create(fx, run_time=4), FadeIn(labels, run_time= 10), FadeIn(a_label, run_time = 10), FadeIn(b_label, run_time = 10))
        self.play(Create(area, run_time=4))
        self.wait(3)
        self.play(Create(rects, run_time=2))
        self.wait(20)
        self.play(FadeOut(a_label), FadeOut(b_label) ,FadeIn(puntos_x), Write(etiquetas_x), Write(etiquetas_p), FadeIn(lines))
        self.wait(5)