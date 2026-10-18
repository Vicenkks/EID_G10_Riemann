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
├── .gitignore                         # Archivos ignorados por Git
│
├── src/                               # Código fuente principal
│   ├── __init__.py
│   ├── scene.py                       # Escena principal de Manim
│   ├── config.py                      # Parámetros matemáticos (f, a, b, n)
│   └── utils.py                       # Funciones auxiliares
│
├── media/                             # Archivos generados (no versionados)
│   ├── Tex/                       
│   └── videos/                        # Videos renderizados                
│
└── docs/                              # Documentación adicional
    └── referencias.md                 # Fuentes matemáticas utilizadas    