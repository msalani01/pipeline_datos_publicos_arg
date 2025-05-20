import pandas as pd
import sqlite3
import os

INPUT_PATH = os.path.join("data", "dolar_oficial_limpio.csv")
DB_PATH = os.path.join("data", "dolar.db")
TABLE_NAME = "dolar_oficial"

def cargar_datos():
    print("Cargando datos desde:", INPUT_PATH)

    # primero se lee el csv
    df = pd.read_csv(INPUT_PATH)

    # se crea la conexion con sqlite
    conn = sqlite3.connect(DB_PATH)

    # carga de datos de la tabla
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

    print("✅ Datos cargados en la base SQLite:", DB_PATH)

    # ver primeras filas
    consulta = pd.read_sql(f"SELECT * FROM {TABLE_NAME} LIMIT 5", conn)
    print("Primeras filas en la base:")
    print(consulta)

    conn.close()

if __name__ == "__main__":
    cargar_datos()
