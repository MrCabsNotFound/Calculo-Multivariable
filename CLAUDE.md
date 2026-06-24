# Cálculo Multivariable — Contexto del Proyecto

Este directorio contiene los materiales de la clase de **Cálculo Multivariable** usando Python. Todos los ejercicios y tareas se desarrollan en Jupyter Notebooks (`.ipynb`), que combinan celdas de **Markdown** (con texto y fórmulas en LaTeX) y celdas de **código Python**.

---

## Formato de los archivos

Los notebooks siguen un patrón consistente:

- **Celdas Markdown** — explican el concepto con texto, fórmulas LaTeX y encabezados.
  - Fórmulas inline: `$...$`
  - Fórmulas en bloque (display): `$$...$$`
  - Ejemplo: `$$\frac{dv}{dt} = -k\left(v - \frac{mg}{k}\right)$$`

- **Celdas de código Python** — implementan el concepto con las librerías del curso.

- **Tablas de resultados** — siempre usando la librería `tabulate` con formato `fancy_grid` o `rounded_grid` y `floatfmt` apropiado.

---

## Librerías principales

```python
import sympy as sp              # Cálculo simbólico
import numpy as np              # Cálculo numérico, vectores, matrices
import matplotlib.pyplot as plt # Gráficas
from tabulate import tabulate   # Tablas de resultados
```

---

## Convenciones de código

### SymPy — Cálculo Simbólico

```python
x, y, z = sp.symbols('x, y, z')   # Variables simbólicas

f = sp.cos(x**2 + y**2)

# Derivadas
sp.diff(f, x)           # Derivada parcial respecto a x
sp.diff(f, (x, 2))      # Segunda derivada respecto a x
sp.diff(sp.diff(f, x), y)  # Derivada cruzada fxy

# Integrales
sp.integrate(f, x)              # Integral indefinida
sp.integrate(f, (x, 0, y**3))  # Integral definida

sp.pprint(expr)   # Impresión simbólica "bonita"
sp.lambdify(x, f) # Convierte expresión simbólica a función numérica evaluable
```

### NumPy — Cálculo Numérico

```python
np.linspace(a, b, n)       # n puntos igualmente espaciados de a a b
np.arange(a, b, paso)      # vector de a a b con salto=paso
np.array([...])            # vectores y matrices
np.dot(v1, v2)             # producto punto
np.ones((m, n))            # matriz de unos
np.eye(n)                  # matriz identidad
```

### Matplotlib — Gráficas

```python
plt.plot(x, y, 'r-')                          # línea roja sólida
plt.plot(x, y, 'k--')                         # línea negra punteada
plt.title('título')
plt.xlabel('x'); plt.ylabel('y')
plt.grid()
plt.legend(['f1', 'f2'], loc='lower right')
plt.ylim([ymin, ymax]); plt.xlim([xmin, xmax])
plt.fill_between(x, y1, y2, where=(y1 > y2), alpha=0.6)  # área sombreada
plt.polar(theta, r)                           # gráficas polares
plt.figure()                                  # abre nueva ventana
```

### Tabulate — Tablas

```python
print(tabulate(
    Tabla,
    headers=['Col1', 'Col2', ...],
    numalign='center',
    tablefmt='fancy_grid',          # o 'rounded_grid'
    floatfmt=['3d', '13.10f', '6.2e', '6.3e']
))
```

---

## Métodos Numéricos implementados en clase

### Bisección

```python
def MetodoBiseccion(Funcion, xizq, xder, Precision=1e-6):
    Funcion = sp.lambdify(x, Funcion)
    ErrorAprox = 1; Pasos = 0; Tabla = []
    while ErrorAprox > Precision:
        Pasos += 1
        ErrorAprox = 0.5 * (xder - xizq)
        medio = 0.5 * (xizq + xder)
        Tabla.append([Pasos, xizq, medio, xder, ...])
        if Funcion(xizq) * Funcion(medio) < 0:
            xder = medio
        else:
            xizq = medio
```

### Newton-Raphson

```python
def MetodoNewton(Funcion, xest, Precision=1e-6):
    Derivada = sp.diff(Funcion, x)
    Funcion  = sp.lambdify(x, Funcion)
    Derivada = sp.lambdify(x, Derivada)
    while ErrorAprox > Precision:
        nuevo = xest - Funcion(xest) / Derivada(xest)
        ErrorAprox = abs(nuevo - xest)
        xest = nuevo
```

---

## Temas cubiertos

- Funciones de múltiples variables con SymPy
- Derivadas parciales y derivadas cruzadas
- Integrales simples y dobles (cambio de orden de integración)
- Vectores y matrices con NumPy
- Graficación 2D: funciones, curvas polares, áreas entre curvas
- Métodos numéricos: Bisección y Newton-Raphson
- Ecuaciones diferenciales ordinarias (resistencia al aire)

---

## Instrucciones para tareas

Cuando el usuario pida resolver ejercicios o crear notebooks:

1. **Formato `.ipynb`** — alternar celdas Markdown y Python como en los ejemplos.
2. **LaTeX en Markdown** — usar `$$...$$` para plantear el problema matemáticamente antes del código.
3. **SymPy primero** — obtener resultados simbólicos cuando sea posible; convertir con `sp.lambdify()` para evaluación numérica.
4. **Tabulate para resultados** — usar `fancy_grid` con `floatfmt` apropiado para la precisión requerida.
5. **Comentarios en español** — seguir el estilo de los notebooks de clase.
6. **Funciones reutilizables** — definir `def` con parámetros default cuando el ejercicio lo amerite, con docstring en español.
7. **Numerar los archivos** — continuar la secuencia existente (16_, 17_, etc.).
