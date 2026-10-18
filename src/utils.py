"""Objetos de Manim reutilizables para explicar una suma de Riemann."""

from manim import *

from config import COLOR_RECTANGULOS, a, b, ejes, f, fx


def crear_rectangulos(n: int) -> VGroup:
    """Devuelve la suma de Riemann por puntos medios con n rectángulos."""
    return ejes.get_riemann_rectangles(
        fx,
        x_range=[a, b],
        dx=(b - a) / n,
        input_sample_type="center",
        color=COLOR_RECTANGULOS,
        fill_opacity=0.48,
        stroke_width=1.2,
    )


def crear_particion(n: int) -> tuple[VGroup, VGroup]:
    """Crea los puntos x_0, ..., x_n para una partición legible."""
    puntos = VGroup()
    etiquetas = VGroup()
    dx = (b - a) / n

    for indice in range(n + 1):
        x = a + indice * dx
        punto = Dot(ejes.c2p(x, 0), color=YELLOW, radius=0.055)
        etiqueta = MathTex(rf"x_{{{indice}}}", font_size=28).next_to(
            punto, DOWN, buff=0.12
        )
        puntos.add(punto)
        etiquetas.add(etiqueta)

    return puntos, etiquetas


def elementos_rectangulo(indice: int, n: int) -> VGroup:
    dx = (b - a) / n
    x_izq = a + indice * dx
    x_der = x_izq + dx
    x_muestra = (x_izq + x_der) / 2
    altura = f(x_muestra)

    punto_muestra = Dot(ejes.c2p(x_muestra, altura), color=YELLOW, radius=0.07)
    linea_muestra = DashedLine(
        ejes.c2p(x_muestra, 0),
        ejes.c2p(x_muestra, altura),
        color=YELLOW,
        dashed_ratio=0.65,
    )
    etiqueta_muestra = MathTex(r"x_i^*", color=YELLOW, font_size=30).next_to(
        ejes.c2p(x_muestra, 0), DOWN, buff=0.1
    )

    base = Line(ejes.c2p(x_izq, 0), ejes.c2p(x_der, 0)).set_stroke(opacity=0)
    llave_dx = Brace(base, DOWN, color=YELLOW, buff=0.35)
    etiqueta_dx = MathTex(r"\Delta x", color=YELLOW, font_size=30).next_to(
        etiqueta_muestra, DOWN, buff=0.22
    )

    linea_altura = Line(ejes.c2p(x_muestra, 0), ejes.c2p(x_muestra, altura))
    llave_altura = Brace(linea_altura, RIGHT, color=YELLOW)
    etiqueta_altura = MathTex(
        r"f(x_i^*)", color=YELLOW, font_size=30
    ).next_to(llave_altura, RIGHT, buff=0.08)

    return VGroup(
        punto_muestra,
        linea_muestra,
        etiqueta_muestra,
        llave_dx,
        etiqueta_dx,
        llave_altura,
        etiqueta_altura,
    )


def suma_por_punto_medio(n: int) -> float:
    dx = (b - a) / n
    muestras = a + (np.arange(n) + 0.5) * dx
    return float(np.sum(f(muestras) * dx))
