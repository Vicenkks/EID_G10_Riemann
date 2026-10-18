from manim import *

from config import COLOR_RECTANGULOS, PARTICIONES, a, b, ejes, fx
from utils import crear_particion, crear_rectangulos, elementos_rectangulo, suma_por_punto_medio


class SumaRiemann(Scene):
    def construct(self):
        n_inicial, n_8, n_16, n_final = PARTICIONES

        # 00:00–00:23 — Pregunta y contexto.
        titulo = Title("Leer una suma de Riemann desde un gráfico", font_size=34)
        pregunta = Tex(
            "¿Cómo aproximamos el área bajo una curva?", font_size=34
        ).next_to(titulo, DOWN)
        grupo = Tex(
            "Grupo 10\\ ¿Qué información matemática está contenida en cada elemento de una suma de Riemann?", font_size=34
        ).center()
        self.play(FadeIn(titulo, shift=DOWN), Write(pregunta), Write(grupo), run_time=3)
        self.wait(18)
        self.play(FadeOut(pregunta), FadeOut(grupo), run_time=2)

        # 00:23–01:09 — Función, intervalo y área exacta.
        funcion = MathTex(r"f(x)=\sin(x)", color=RED, font_size=38).to_corner(UR)
        intervalo = MathTex(r"[a,b]=[0,\pi]", font_size=34).next_to(
            funcion, DOWN, aligned_edge=LEFT
        )
        etiqueta_a = MathTex("a=0", font_size=28).next_to(ejes.c2p(a, 0), DOWN, buff=0.55)
        etiqueta_b = MathTex(r"b=\pi", font_size=28).next_to(
            ejes.c2p(b, 0), DOWN, buff=0.55
        )

        self.play(
            Create(ejes),
            Create(fx),
            Write(funcion),
            Write(intervalo),
            FadeIn(etiqueta_a),
            FadeIn(etiqueta_b),
            run_time=6,
        )
        self.wait(18)

        area = ejes.get_area(
            fx,
            x_range=[a, b],
            color=(GREEN_B, GREEN_D),
            opacity=0.36,
        )
        self.play(Create(area), run_time=4)
        self.wait(18)

        texto_aproximacion = Tex(
            "Dividimos el intervalo en subintervalos", font_size=28
        ).next_to(intervalo, DOWN, aligned_edge=RIGHT, buff=0.35)
        formula_dx = MathTex(
            r"\Delta x=\frac{b-a}{n}", font_size=34
        ).next_to(texto_aproximacion, DOWN, buff=0.25)
        puntos, etiquetas = crear_particion(n_inicial)
        rects_4 = crear_rectangulos(n_inicial)

        self.play(Write(texto_aproximacion), Write(formula_dx), run_time=3)
        self.play(FadeIn(puntos), Write(etiquetas), run_time=4)
        self.play(
            LaggedStart(
                *[Create(rectangulo) for rectangulo in rects_4], lag_ratio=0.24
            ),
            run_time=8,
        )
        self.wait(16)

        indice_destacado = 1
        rectangulo_destacado = SurroundingRectangle(
            rects_4[indice_destacado], color=YELLOW, buff=0.05, stroke_width=4, fill_opacity=0.4
        )
        elementos = elementos_rectangulo(indice_destacado, n_inicial)
        etiqueta_rectangulo = Tex("Un rectángulo", color=YELLOW, font_size=28).next_to(
            rectangulo_destacado, UP, buff=0.15
        )

        intervalo_x = MathTex(
            r"[x_{i-1}, x_i]", font_size=30
        ).next_to(
        elementos[4], DOWN, buff=0.08
        )

        self.play(
            Create(rectangulo_destacado),
            FadeIn(elementos[0]),
            Create(elementos[1]),
            Write(etiqueta_rectangulo),
            run_time=4,
        )
        self.play(
            Write(elementos[2]),
            GrowFromCenter(elementos[3]),
            Write(elementos[4]),
            Write(intervalo_x),
            run_time=4,
        )
        self.wait(20)
        self.play(
            GrowFromCenter(elementos[5]),
            Write(elementos[6]),
            run_time=4,
        )
        self.wait(25)

        formula_area_rectangulo = MathTex(
            r"\text{Área del rectángulo } i"
            r"=f(x_i^*)\,\Delta x",
            font_size=34,
        ).next_to(formula_dx, DOWN, buff=0.45)
        self.play(Write(formula_area_rectangulo), run_time=4)
        self.wait(20)

        self.play(
            FadeOut(elementos),
            FadeOut(rectangulo_destacado),
            FadeOut(etiqueta_rectangulo),
            FadeOut(texto_aproximacion),
            FadeOut(formula_area_rectangulo),
            FadeOut(etiquetas),
            FadeOut(puntos),
            FadeOut(intervalo_x),
            run_time=3,
        )
        termino = MathTex(
            r"f(x_1^*)\Delta x+f(x_2^*)\Delta x+\cdots+f(x_n^*)\Delta x",
            font_size=29,
        ).next_to(intervalo, DOWN, aligned_edge=RIGHT, buff= 0.55)
        suma = MathTex(
            r"S_n=\sum_{i=1}^{n}f(x_i^*)\,\Delta x",
            color=YELLOW,
            font_size=38,
        ).move_to(termino)
        mensaje_suma = Tex(
            "Sumamos las áreas de todos los rectángulos.", font_size=27
        ).next_to(termino, DOWN, buff=0.45)

        self.play(FadeOut(formula_dx))
        self.play(Write(termino), Write(mensaje_suma), run_time=4)
        self.wait(20)
        self.play(TransformMatchingTex(termino, suma), run_time=4)
        self.wait(30)
        self.play(FadeOut(mensaje_suma), run_time=3)

        etiqueta_n = MathTex(r"n=4", font_size=34).next_to(suma, DOWN, buff=0.35)
        self.play(Write(etiqueta_n), run_time=2)
        self.wait(8)

        rects_8 = crear_rectangulos(n_8)
        nuevo_n = MathTex(r"n=8", font_size=34).move_to(etiqueta_n)
        self.play(ReplacementTransform(rects_4, rects_8), Transform(etiqueta_n, nuevo_n), run_time=5)
        self.wait(15)

        rects_16 = crear_rectangulos(n_16)
        nuevo_n = MathTex(r"n=16", font_size=34).move_to(etiqueta_n)
        self.play(ReplacementTransform(rects_8, rects_16), Transform(etiqueta_n, nuevo_n), run_time=5)
        self.wait(15)

        rects_finales = crear_rectangulos(n_final)
        nuevo_n = MathTex(rf"n={n_final}", font_size=34).move_to(etiqueta_n)
        self.play(
            ReplacementTransform(rects_16, rects_finales),
            Transform(etiqueta_n, nuevo_n),
            run_time=6,
        )
        self.wait(25)

        aproximacion = suma_por_punto_medio(n_final)
        resultado = MathTex(
            rf"S_{{{n_final}}}\approx {aproximacion:.4f}",
            font_size=34,
        ).next_to(nuevo_n, DOWN, aligned_edge=LEFT, buff=0.35)
        comparacion = MathTex(
            r"\int_0^\pi\sin(x)\,dx=2",
            color=GREEN_C,
            font_size=34,
        ).next_to(resultado, DOWN, aligned_edge=LEFT, buff=0.22)
        conclusion = Tex(
            r"Al disminuir $\Delta x$,\\ la suma se aproxima al área exacta.",
            font_size=28,
        ).next_to(comparacion, DOWN, buff=0.4)

        self.play(Write(resultado), Write(comparacion), run_time=4)
        self.wait(20)
        self.play(Write(conclusion), run_time=3)
        self.wait(7)
