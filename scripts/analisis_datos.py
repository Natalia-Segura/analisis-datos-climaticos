
import pandas as pd
import matplotlib.pyplot as plt

#Cargar dataset desde URL (temperaturas globales)
url = "http://datahub.io/core/global-temp/r/monthly.csv"
df = pd.read_csv(url)

#Mostrar primeras filas para verificar carga
print(df.head())


#Ver nombres de columnas:
print("Columnas del dataset: ", df.columns)

#Información general
print(df.info())

#Estadísticas básicas
print(df.describe())


#Normalizar nombres de columnas
df.columns = df.columns.str.lower()

#Renombrar columna "mean" para mayor claridad
df = df.rename(columns={"mean": "temperature"})

#Verificar cambios
print(df.head())


#Promedio global de temperatura
print("Promedio de temperatura: ", df["temperature"].mean())

#Temperatura máxima registrada
print("Máxima: ", df["temperature"].max())

#Temperatura mínima registrada
print("Mínima: ", df["temperature"].min())

#Agrupar por año para análisis anual
df_year = df.groupby("year")["temperature"].mean()
print(df_year.head())


#Gráfico de evolución anual de temperatura
plt.figure(figsize=(10,5))
plt.plot(df_year.index, df_year.values)

plt.title("Evolución de temperatura global")
plt.xlabel("Año")
plt.ylabel("Temperatura promedio")

plt.grid()
plt.show()


#Guardar resumen anual en CSV dentro del proyecto
df_year.to_csv("resultados/resumen_anual.csv")
