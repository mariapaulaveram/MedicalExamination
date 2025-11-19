# Visualización y análisis de datos médicos

En este proyecto se visualizan y analizan datos de exámenes médicos utilizando **pandas**, **NumPy**, **matplotlib** y **seaborn**. Los valores del conjunto de datos fueron recopilados durante exámenes médicos de rutina.

---

## Archivo de datos

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

## Objetivos del proyecto

1. **Visualizar recuentos de variables categóricas** (colesterol, glucosa, alcohol, actividad física, tabaquismo, sobrepeso) separadas por presencia o ausencia de enfermedad cardiovascular.
2. **Limpiar y normalizar los datos** para análisis estadístico.
3. 

---


###  Preparación de datos
Esta etapa incluye la carga del archivo, la exploración inicial y la transformación de variables clínicas para facilitar el análisis.

**Carga del archivo:**  
Se importa el archivo `medical_examination.csv` y se asigna a la variable `df`.

**Exploración inicial:**  
Se inspecciona la forma del dataset, las primeras filas, el tipo de datos y la presencia de valores nulos.  
Esto permite verificar:  
- Cantidad de pacientes y variables  
- Tipos de datos (enteros, flotantes, categóricos)  
- Posibles columnas con valores faltantes  

**Transformación de variables clínicas:** Para garantizar la calidad de las visualizaciones, se definieron funciones auxiliares que permiten filtrar valores extremos y transformar variables clínicas.

- **Cálculo del IMC y clasificación de sobrepeso:** se agrega la columna `BMI` y se clasifica como `overweight` si el IMC supera 25.  
- **Normalización de colesterol y glucosa:** se convierten en variables binarias:  
  - `cholesterol`: 0 = normal, 1 = alto o muy alto  
  - `gluc`: 0 = normal, 1 = alto o muy alto  
- **Conversión de edad:** la edad original está en días. Se transforma a años (`age_years`) para facilitar la interpretación.
- **Filtrado de outliers:** se eliminan valores extremos de una columna numérica utilizando percentiles (1% y 99%).  Esto evita que valores atípicos distorsionen los gráficos y el análisis estadístico.


### Visualizaciones Mathplotlib




## 📌 Notas

- Este proyecto forma parte del módulo de análisis de datos médicos de [freeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer).

---

