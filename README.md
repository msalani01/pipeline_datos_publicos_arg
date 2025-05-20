# Pipeline de Datos Públicos Argentinos

Este proyecto extrae, transforma y carga datos del dólar oficial desde la API del BCRA. Se almacenan en una base SQLite y se visualizan con Python.

## Tecnologías
- Python
- Pandas
- SQLite
- Requests
- Matplotlib / Seaborn
- Virtualenv
- Linux

## Cómo correrlo

1. Cloná el repositorio
2. Activá el entorno virtual
3. Ejecutá:

```bash
python scripts/extract.py
python scripts/transform.py
python scripts/load.py

Autor

Marco Salani
Estudiante de Ingeniería en Sistemas | Analista de Datos en formación
LinkedIn: linkedin.com/in/marco-salani-aa4332185