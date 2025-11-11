# 🩺 Visualización y análisis de datos médicos

En este proyecto se visualizan y analizan datos de exámenes médicos utilizando **pandas**, **NumPy**, **matplotlib** y **seaborn**. Los valores del conjunto de datos fueron recopilados durante exámenes médicos de rutina.

---

## 📁 Archivo de datos

**Nombre del archivo:** `medical_examination.csv`  
Cada fila representa un paciente. Las columnas contienen medidas corporales, resultados de análisis de sangre y hábitos de vida.

| Característica                          | Tipo de variable         | Variable       | Tipo de valor                          |
|----------------------------------------|---------------------------|----------------|----------------------------------------|
| Edad                                   | Objetiva                  | `age`          | Entero (días)                          |
| Altura                                 | Objetiva                  | `height`       | Entero (cm)                            |
| Peso                                   | Objetiva                  | `weight`       | Flotante (kg)                          |
| Género                                 | Objetiva                  | `gender`       | Código categórico                      |
| Presión arterial sistólica             | Función de examen         | `ap_hi`        | Entero                                 |
| Presión arterial diastólica            | Función de examen         | `ap_lo`        | Entero                                 |
| Colesterol                             | Función de examen         | `cholesterol`  | 1: normal, 2: alto, 3: muy alto        |
| Glucosa                                | Función de examen         | `gluc`         | 1: normal, 2: alto, 3: muy alto        |
| Fumador                                 | Subjetiva                 | `smoke`        | Binario                                |
| Consumo de alcohol                     | Subjetiva                 | `alco`         | Binario                                |
| Actividad física                       | Subjetiva                 | `active`       | Binario                                |
| Enfermedad cardiovascular              | Variable objetivo         | `cardio`       | Binario                                |

---

## 📊 Objetivos del proyecto

1. **Visualizar recuentos de variables categóricas** (colesterol, glucosa, alcohol, actividad física, tabaquismo, sobrepeso) separadas por presencia o ausencia de enfermedad cardiovascular.
2. **Limpiar y normalizar los datos** para análisis estadístico.
3. **Generar un mapa de calor** con correlaciones entre variables clínicas.

---

## 🧪 Instrucciones técnicas

### 🔹 Preparación de datos

- Importar el archivo `medical_examination.csv` y asignarlo a la variable `df`.
- Agregar una columna `overweight` calculando el IMC:  
  

\[
  \text{IMC} = \frac{\text{peso (kg)}}{(\text{altura (m)})^2}
  \]

  
  Si IMC > 25 → `overweight = 1`, si no → `overweight = 0`.

- Normalizar las variables `cholesterol` y `gluc`:  
  - Si el valor es 1 → bueno → asignar 0  
  - Si el valor es 2 o 3 → malo → asignar 1

---

### 🔹 Gráfico categórico (`draw_cat_plot`)

- Usar `pd.melt()` para transformar las variables: `cholesterol`, `gluc`, `smoke`, `alco`, `active`, `overweight`.
- Agrupar por `cardio`, `variable`, `value` y contar ocurrencias.
- Renombrar columnas para que `sns.catplot()` funcione correctamente.
- Crear el gráfico con `sns.catplot()` y guardar en la variable `fig`.

---

### 🔹 Mapa de calor (`draw_heat_map`)

- Filtrar datos incorrectos:
  - `ap_lo` ≤ `ap_hi`
  - `height` entre percentiles 2.5 y 97.5
  - `weight` entre percentiles 2.5 y 97.5

- Calcular la matriz de correlación con `df.corr()` → guardar en `corr`.
- Generar una máscara para el triángulo superior → guardar en `mask`.
- Configurar la figura y graficar con `sns.heatmap()`.

---

## 📌 Notas

- No modificar las dos líneas finales de cada función (`draw_cat_plot`, `draw_heat_map`) para asegurar compatibilidad con el entorno de evaluación.
- Este proyecto forma parte del módulo de análisis de datos médicos de [freeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer).

---

