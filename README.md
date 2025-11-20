# Visualización y análisis de datos médicos

Este proyecto aplica técnicas de análisis de datos clínicos y visualización utilizando librerías de Python como NumPy, pandas, matplotlib y seaborn. El dataset (medical_examination.csv) contiene información de pacientes obtenida en exámenes médicos de rutina: edad, peso, altura, presión arterial, colesterol, glucosa y hábitos de vida.
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

Este proyecto tiene como propósito aplicar y consolidar conocimientos adquiridos en el curso [Python para Data Science – Udemy](https://www.udemy.com/course/python-para-data-science/), utilizando un conjunto de datos clínicos del proyecto [Medical Data Visualizer – FreeCodeCamp](https://www.freecodecamp.org/espanol/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer).

Los objetivos específicos son:

1. **Practicar el uso de librerías clave** para análisis de datos: `pandas`, `NumPy`, `matplotlib` y `seaborn`.  
2. **Aplicar funciones modulares en Python** para cargar, transformar y visualizar datos clínicos.  
3. **Explorar y limpiar el dataset** para preparar variables relevantes como edad, IMC, colesterol y glucosa.  
4. **Visualizar relaciones clínicas** mediante gráficos de línea, barras, histogramas, tortas y dispersión.  
5. **Comparar grupos con y sin enfermedad cardiovascular** en función de variables como edad, IMC y presión arterial.  
6. **Estandarizar el estilo gráfico** para presentaciones profesionales y facilitar la interpretación institucional.  
7. **Preparar el entorno para futuros modelos de machine learning**, normalizando variables y entendiendo correlaciones.  

---

##  Preparación de datos

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

---

