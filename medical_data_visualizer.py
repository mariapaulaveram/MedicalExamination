import pandas as pd

# Cargar el archivo
df = pd.read_csv("C:/Users/trezz/Desktop/proyectosDeDesarrolloWeb/MedicalExamination/data/medical_examination.csv")

#Exploracion Inicial
print("\n *Forma del DataFrame (filas, columnas):")
print(df.shape)
print("\n *Primeras filas del dataset:")
print(df.head())
print("\n *Información general del DataFrame:")
print(df.info())
print("\n *Cantidad de valores nulos por columna:")
print(df.isnull().sum())
print("\n")

#Agregar columna 'overweight' Convierte la altura de centímetros a metros y calcula el IMC para cada paciente.
# Devuelve True o False.Convierte True en 1 y False en 0.
df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2) > 25).astype(int)

#Normalizar colesterol y glucosa
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)