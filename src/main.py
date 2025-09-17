# src/main.py
import os
from csv_utils import load_countries
from csv_utils import print_country
from menu import menu_principal

def default_csv_path() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "..", "data", "paises_prueba.csv")

if __name__ == "__main__":
    path = default_csv_path()
    data = load_countries(path)
    if not data:
        print("No se pudo cargar el dataset. Verifique el CSV.")
    else:
        print(f"Se cargaron {len(data)} países:\n")
        for p in data:
            print_country(p)
    print("--------------------------------------------------------------------------------------------------")
    menu_principal()
        