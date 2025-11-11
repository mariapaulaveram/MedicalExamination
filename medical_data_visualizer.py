import pandas as pd
import matplotlib.pyplot as plt

# Cargar y preparar los datos
def cargar_datos(ruta):
    df = pd.read_csv(ruta)
    df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
    df["gluc"] = (df["gluc"] > 1).astype(int)
    df["age_years"] = (df["age"] / 365).astype(int)
    return df

def agregar_bmi(df):
    """Calcula el IMC y agrega las columnas 'BMI' e 'overweight' al DataFrame."""
    bmi = df["weight"] / ((df["height"] / 100) ** 2)
    df["BMI"] = bmi
    df["overweight"] = (bmi > 25).astype(int)
    return df

# Mostrar exploración inicial
def explorar(df):
    print("\nForma:", df.shape)
    print("\nPrimeras filas:\n", df.head())
    print("\nInfo:\n", df.info())
    print("\nNulos:\n", df.isnull().sum())

# Función de estilo general
def estilo_grafico(titulo, xlabel, ylabel):
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()

# Línea de presión sistólica por rangos de edad
def presion_por_rangos(df):
    df["age_group"] = pd.cut(df["age_years"], bins=[30, 40, 50, 60, 70], labels=["30–40", "40–50", "50–60", "60–70"])
    df.groupby("age_group", observed=True)["ap_hi"].mean().plot(kind="line", marker="o", color="orange")
    estilo_grafico("Presión sistólica promedio por rangos de edad", "Grupo etario", "Presión sistólica (mmHg)")
    plt.show()
    plt.close()

# Comparar presión entre grupos con y sin enfermedad
def comparar_por_cardio(df):
    df.groupby(["age_years", "cardio"])["ap_hi"].mean().unstack().plot()
    estilo_grafico("Presión sistólica por edad y grupo cardiovascular", "Edad (años)", "Presión sistólica (mmHg)")
    plt.show()
    plt.close()

# Línea general de presión por edad
def presion_general(df):
    df.groupby("age_years")["ap_hi"].mean().plot(color="blue", linewidth=2)
    estilo_grafico("Promedio de presión sistólica por edad", "Edad (años)", "Presión sistólica (mmHg)")
    plt.show()
    plt.close()

# Gráfico de barras de cantidad de pacientes por edad
def barras_por_edad(df):
    df["age_years"].value_counts().sort_index().plot(kind="bar", color="lightblue")
    estilo_grafico("Cantidad de pacientes por edad", "Edad (años)", "Cantidad")
    plt.show()
    plt.close()

# Histograma de edad en años, visualiza la distribución de edades
def histograma_edad(df):
    plt.hist(df["age_years"], bins=20, color="skyblue", edgecolor="black")
    estilo_grafico("Distribución de edad", "Edad (años)", "Cantidad de pacientes")
    plt.show()
    plt.close()

# Histograma de IMC
def histograma_imc_filtrado(df):
    df_filtrado = df[(df["BMI"] >= 10) & (df["BMI"] <= 50)]
    plt.hist(df_filtrado["BMI"], bins=20, color="mediumseagreen", edgecolor="black")
    estilo_grafico("Distribución de IMC (filtrada)", "IMC", "Cantidad de pacientes")
    plt.show()
    plt.close()

# Histograma IMC por grupo cardiovascular
def histograma_imc_por_cardio(df):
    df_filtrado = df[(df["BMI"] >= 10) & (df["BMI"] <= 50)]

    grupo_0 = df_filtrado[df_filtrado["cardio"] == 0]["BMI"]
    grupo_1 = df_filtrado[df_filtrado["cardio"] == 1]["BMI"]

    plt.hist([grupo_0, grupo_1], bins=20, label=["Sin enfermedad", "Con enfermedad"],
             color=["lightgreen", "tomato"], edgecolor="black", alpha=0.7)
    estilo_grafico("IMC por grupo cardiovascular", "IMC", "Cantidad de pacientes")
    plt.legend()
    plt.show()
    plt.close()


# Histograma de edad por grupo cardiovascular, compara la edad entre pacientes con y sin enfermedad
def histograma_edad_por_cardio(df):
    plt.hist([df[df["cardio"] == 0]["age_years"], df[df["cardio"] == 1]["age_years"]],
             bins=20, label=["Sin enfermedad", "Con enfermedad"], color=["lightgreen", "tomato"], edgecolor="black")
    estilo_grafico("Distribución de edad por grupo cardiovascular", "Edad (años)", "Cantidad de pacientes")
    plt.legend()
    plt.show()
    plt.close()

# Scatter visualiza cómo varía el IMC con la edad
def scatter_imc_vs_edad(df):
    plt.scatter(df["age_years"], df["BMI"], alpha=0.3, c="mediumseagreen")
    estilo_grafico("IMC en función de la edad", "Edad (años)", "IMC")
    plt.show()
    plt.close()

# Presión sistólica vs Edad
def scatter_presion_vs_edad(df):
    plt.scatter(df["age_years"], df["ap_hi"], alpha=0.3, c="orange")
    estilo_grafico("Presión sistólica en función de la edad", "Edad (años)", "Presión sistólica (mmHg)")
    plt.show()
    plt.close()

# Presión sistólica vs IMC
def scatter_presion_vs_imc(df):
    plt.scatter(df["BMI"], df["ap_hi"], alpha=0.3, c="tomato")
    estilo_grafico("Presión sistólica en función del IMC", "IMC", "Presión sistólica (mmHg)")
    plt.show()
    plt.close()

# Glucosa vs Colesterol
def scatter_glucosa_vs_colesterol(df):
    plt.scatter(df["gluc"], df["cholesterol"], alpha=0.3, c="purple")
    estilo_grafico("Glucosa vs Colesterol (normalizados)", "Glucosa", "Colesterol")
    plt.show()
    plt.close()

# Función única para gráficos de torta
def pie_chart(df, columna, etiquetas, titulo, colores=None):
    """
    Genera un gráfico de torta para una variable categórica o binaria.

    Parámetros:
    - df: DataFrame
    - columna: nombre de la columna a graficar
    - etiquetas: lista de etiquetas para los valores
    - titulo: título del gráfico
    - colores: lista opcional de colores
    """
    valores = df[columna].value_counts()
    plt.pie(valores, labels=etiquetas, autopct="%1.1f%%", colors=colores, startangle=90)
    plt.title(titulo)
    plt.axis("equal")
    plt.tight_layout()
    plt.show()
    plt.close()

# Subplots 4 histogramas en una figura
# Distribución de edad, Distribución de IMC, Edad por grupo cardiovascular,  IMC por grupo cardiovascular
def subplots_histogramas(df):
    df_filtrado = df[(df["BMI"] >= 10) & (df["BMI"] <= 50)]

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Distribuciones clínicas", fontsize=16)

    # Histograma de edad
    axs[0, 0].hist(df["age_years"], bins=20, color="skyblue", edgecolor="black")
    axs[0, 0].set_title("Edad")
    axs[0, 0].set_xlabel("Años")
    axs[0, 0].set_ylabel("Cantidad")

    # Histograma de IMC
    axs[0, 1].hist(df_filtrado["BMI"], bins=20, color="mediumseagreen", edgecolor="black")
    axs[0, 1].set_title("IMC (filtrado)")
    axs[0, 1].set_xlabel("IMC")
    axs[0, 1].set_ylabel("Cantidad")

    # Edad por grupo cardiovascular
    axs[1, 0].hist([df[df["cardio"] == 0]["age_years"], df[df["cardio"] == 1]["age_years"]],
                  bins=20, label=["Sin enfermedad", "Con enfermedad"],
                  color=["lightgreen", "tomato"], edgecolor="black", alpha=0.7)
    axs[1, 0].set_title("Edad por grupo cardiovascular")
    axs[1, 0].set_xlabel("Edad (años)")
    axs[1, 0].set_ylabel("Cantidad")
    axs[1, 0].legend()

    # IMC por grupo cardiovascular
    axs[1, 1].hist([df_filtrado[df_filtrado["cardio"] == 0]["BMI"],
                    df_filtrado[df_filtrado["cardio"] == 1]["BMI"]],
                   bins=20, label=["Sin enfermedad", "Con enfermedad"],
                   color=["lightgreen", "tomato"], edgecolor="black", alpha=0.7)
    axs[1, 1].set_title("IMC por grupo cardiovascular")
    axs[1, 1].set_xlabel("IMC")
    axs[1, 1].set_ylabel("Cantidad")
    axs[1, 1].legend()

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
    plt.close()


# BLOQUE FIJO — Carga y transformación
ruta = "C:/Users/trezz/Desktop/proyectosDeDesarrolloWeb/MedicalExamination/data/medical_examination.csv"
df = cargar_datos(ruta)
df = agregar_bmi(df)

# Exploración inicial
# explorar(df)

# Gráficos de líneas
# presion_por_rangos(df)
# comparar_por_cardio(df)
# presion_general(df)

# Gráficos de barras
# barras_por_edad(df)

# Histogramas simples
# histograma_edad(df)
# histograma_imc_filtrado(df)

#Histogramas comparativos por grupo
# histograma_edad_por_cardio(df)
# histograma_imc_por_cardio(df)

# Scatter
# scatter_imc_vs_edad(df)
# scatter_presion_vs_edad(df)
# scatter_presion_vs_imc(df)
# scatter_glucosa_vs_colesterol(df)

# Gráficos de torta
# pie_chart(df, "cardio", ["Sin enfermedad", "Con enfermedad"], "Distribución cardiovascular", ["lightgreen", "tomato"])
# pie_chart(df, "smoke", ["No fumador", "Fumador"], "Distribución de fumadores")
# pie_chart(df, "alco", ["No consume", "Consume"], "Consumo de alcohol")
# pie_chart(df, "active", ["Inactivo", "Activo"], "Actividad física")
# pie_chart(df, "overweight", ["IMC ≤ 25", "IMC > 25"], "Distribución de sobrepeso")

# Subplots
# subplots_histogramas(df)




