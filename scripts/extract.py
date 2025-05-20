import requests
import os
import json

TOKEN = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzkzMTE5NjEsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJtc2FsYW5pOThAZ21haWwuY29tIn0.qGmbvk0wH4Jdzy7FahVPMYp9HsasOB_Kgxp1QIzz0e870nyiAH-7Hu5yKZzUcAJe2G5ss1KfSTyaYiCW2R9CVA"  # reemplazalo por el real
URL = "https://api.estadisticasbcra.com/usd"
HEADERS = {"Authorization": f"BEARER {TOKEN}"}
OUTPUT_PATH = os.path.join("data", "dolar_oficial.json")  # uso ruta relativa simple

def descargar_datos():
    print("Descargando datos del BCRA...")
    respuesta = requests.get(URL, headers=HEADERS)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        
        # ves que el directorio exista
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

        with open(OUTPUT_PATH, "w") as f:
            json.dump(datos, f, indent=2)
        print("✅ Datos guardados en", OUTPUT_PATH)
    else:
        print("❌ Error al descargar datos:", respuesta.status_code)

if __name__ == "__main__":
    descargar_datos()
