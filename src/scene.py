from manim import *

config.tex_compiler = "pdflatex"
config.output_format = ".pdf"

class SumaRiemann(Scene):
    def construct(self):
        ejes = Axes(
            x_range=[-5, 5, 3.14],
            y_range=[0, 3, 1],
            x_length=9,
            y_length=5.5,
            axis_config={"include_numbers": True, "font_size": 13,},
        )

        graph = ejes.plot(lambda x: np.sin(x), color=RED, x_range=[-5, 5], use_smoothing=False)
        a_label = ejes.get_T_label(x_val=0.2, graph=graph, label=Tex("a"))
        b_label = ejes.get_T_label(x_val=2, graph=graph, label=Tex("b"), line_color=PINK)

        rects = ejes.get_riemann_rectangles(
            graph,
            x_range=[0.2, 2],
            dx=0.1,
            color= (TEAL, BLUE_B, DARK_BLUE),
            input_sample_type="right"
            )
        

        self.play(Create(ejes, run_time=5))
        self.play(Create(graph, run_time=2), Create(a_label), Create(b_label))
        self.play(Create(rects, run_time=2))
        self.wait(5)