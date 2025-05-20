import pandas as pd
import json
import os

INPUT_PATH = os.path.join("data", "dolar_oficial.json")
OUTPUT_PATH = os.path.join("data", "dolar_oficial_limpio.csv")

def transformar_datos():
    print("Leyendo datos desde:", INPUT_PATH)

    # carga del json
    with open(INPUT_PATH, "r") as f:
        datos = json.load(f)

    # se convierte en dataframe
    df = pd.DataFrame(datos)

    # renombrar columnas
    df.rename(columns={"d": "fecha", "v": "valor_usd"}, inplace=True)

    # transformacion de formato fecha
    df["fecha"] = pd.to_datetime(df["fecha"])

    # ordeno por fecha
    df.sort_values("fecha", inplace=True)

    print("Primeras filas:")
    print(df.head())

    # se guarda como csv
    df.to_csv(OUTPUT_PATH, index=False)
    print("✅ Datos transformados guardados en:", OUTPUT_PATH)

if __name__ == "__main__":
    transformar_datos()
