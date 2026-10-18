# Suma de Riemann - Manim

# Proyecto EID - Cálculo Intermedio 2026
## Grupo 10: Leer una suma de Riemann desde una representación gráfica

### Información del Curso
- **Curso:** Cálculo Intermedio
- **Carrera:** Ingeniería Civil Informática
- **Periodo:** Segundo semestre, 2026
- **Evaluación:** Evaluación Integrada de Desempeño (EID)

### Integrantes
| Nombre | Cuenta GitHub | Rol Principal |
|--------|---------------|---------------|
| Annan John | @annan-7 | Matemática y explicación |
| Vicente Huilcaman | @Vicenkks | Visualización y código |
| Matias Espinoza | @Mati-3spin | Revisión e integración |

### Tema y Pregunta Central
**Tema:** Leer una suma de Riemann desde una representación gráfica

**Pregunta Central:** ¿Qué información matemática está contenida en cada elemento de una suma de Riemann?

**Objetivo:** A partir de una función y una partición concreta, conectar visualmente cada rectángulo con:
- El subintervalo $[x_{i-1}, x_i]$
- El punto muestra $x^*_i$
- La altura $f(x^*_i)$
- El área $f(x^*_i)\Delta x$

Y explicar cómo estos elementos se relacionan con los términos de la sumatoria $\sum f(x^*_i)\Delta x$.

---

## Arquitectura del Proyecto

### Estructura de Directorios

```text
EID_G10_Riemann/
│
├── README.md                          # Documentación principal del proyecto
├── requirements.txt                   # Dependencias de Python
├── .gitignore                         # Archivos ignorados por Git
│
├── src/                               # Código fuente principal
│   ├── __init__.py
│   ├── scene.py                       # Escena principal de Manim
│   ├── config.py                      # Parámetros matemáticos (f, a, b, n)
│   └── utils.py                       # Funciones auxiliares
│
├── media/                             # Archivos generados (no versionados)
│   ├── videos/                        # Videos renderizados
│   └── images/                        # Imágenes generadas
│
└── docs/                              # Documentación adicional
    ├── referencias.md                 # Fuentes matemáticas utilizadas
    └── declaracion_ia.md              # Declaración de uso de IA
```
---

## Dependencias Esternas

* LaTeX (no instalables con pip):

### Windows
* LaTeX: Descarga e instala [MiKTeX](https://miktex.org/?spm=a2ty_o01.29997173.0.0.7e07c921CX8wvU).
### MacOS
Desde la terminal:
* brew install --cask mactex
### Linux
Desde la terminal:
* sudo apt install ffmpeg texlive-full libpango1.0-dev libcairo2-dev
