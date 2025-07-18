# Trabajo01EQ5RNABI
# Trabajo 01: Optimización Heurística

Este proyecto explora y compara diversas metodologías de optimización, abordando tanto problemas de optimización numérica de funciones continuas como un problema clásico de optimización combinatoria. Se utilizan métodos basados en gradientes, algoritmos heurísticos y metaheurísticos para encontrar soluciones óptimas o cercanas a las óptimas.

---

* **`Trabajo1.Rmd`**: El archivo R Markdown principal que contiene todo el código, las implementaciones de los algoritmos, las visualizaciones y la discusión de resultados.

---

## Parte 1: Optimización Numérica

Esta sección se enfoca en la optimización de funciones de prueba continuas.

### 🧪 Funciones de Prueba Seleccionadas

Se optimizarán las siguientes funciones en **dos (2D)** y **tres (3D)** dimensiones:

* **Función de Rosenbrock**:
 
    *Esta función es conocida por su mínimo global ubicado en un valle parabólico estrecho y es un desafío para muchos algoritmos de optimización.*

* **Función de Rastrigin**:

    *Esta función es multimodal, lo que significa que tiene muchos mínimos locales que pueden atrapar a los algoritmos de optimización.*

### Métodos de Optimización Aplicados

Se emplearán y compararán los siguientes algoritmos:

* **Método de Descenso por Gradiente**: Un método de optimización de primer orden que sigue la dirección de la pendiente más pronunciada de la función.
* **Algoritmos Heurísticos / Metaheurísticos**:
    * **Algoritmos Evolutivos (EA)**
    * **Optimización por Enjambre de Partículas (PSO)**
    * **Evolución Diferencial (DE)**


**Visualizaciones**:
Se generarán **GIFs animados** que representen el proceso de optimización para el **descenso por gradiente** y al menos uno de los **métodos heurísticos** (por ejemplo, PSO o EA).

---

## Parte 2: Optimización Combinatoria

Esta sección aborda un problema clásico de optimización discreta.

### Problema del Vendedor Viajero (TSP) en Colombia

Un vendedor debe recorrer  **13 ciudades principales de Colombia**, visitando cada una exactamente una vez y regresando al punto de partida, con el objetivo de **minimizar el costo total del recorrido**.



## 🖥️ Requisitos

Para poder ejecutar el `Trabajo1.Rmd`,se debe tener instalado **R** y las siguientes librerías:

* `ggplot2`
* `gifski`
* `tidyverse`
* `plotly` 
* `readr`
* `sf`
* `geosphere`
* `pracma`
* `GA`
* `NMOF`
* `optimx`
* `DEoptim`
* `pso`
* `TSP`
* `rnaturalearth`
* 
Para cualquier pregunta o sugerencia, no dudar en contactar al equipo del proyecto.

Aunque se recomienda mirar cuáles se tienen instaladas también se pueden instalar la mayoría de estas librerías ejecutando el siguiente comando en R:

```R
install.packages(c("ggplot2", "gifski", "tidyverse", "plotly", "readr", "sf", "geosphere", "pracma", "GA", "NMOF", "optimx", "DEoptim", "pso", "TSP", "rnaturalearth"))


