# src/csv_utils.py
from typing import List, Dict, Any
import csv

REQUIRED_FIELDS = ("nombre", "poblacion", "superficie", "continente")

def load_countries(csv_path: str) -> List[Dict[str, Any]]:
    data: List[Dict[str, Any]] = []
    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            headers = [h.strip().lower() for h in (reader.fieldnames or [])]
            if any(req not in headers for req in REQUIRED_FIELDS):
                raise ValueError("CSV inválido: faltan columnas requeridas.")
            for i, row in enumerate(reader, start=2):
                try:
                    nombre = (row.get("nombre") or "").strip()
                    continente = (row.get("continente") or "").strip()
                    poblacion = int((row.get("poblacion") or "0").strip())
                    superficie = int((row.get("superficie") or "0").strip())
                    if not nombre or not continente or poblacion <= 0 or superficie <= 0:
                        raise ValueError("Valores vacíos o no positivos.")
                    data.append({
                        "nombre": nombre,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente
                    })
                except Exception as e:
                    print(f"[WARN] Fila {i} omitida: {e}")
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {csv_path}")
    except Exception as e:
        print(f"[ERROR] Error al leer CSV: {e}")
    return data

def print_country(p: dict) -> None:
    print(
        f"- {p['nombre']:15} | "
        f"Población: {p['poblacion']:,} | "
        f"Superficie: {p['superficie']:,} km² | "
        f"Continente: {p['continente']}"
    )

def save_countries(countries: List[Dict[str, Any]], csv_path: str) -> bool:
    """
    Guarda la lista de países en un archivo CSV.
    
    Args:
        countries: Lista de diccionarios con datos de países
        csv_path: Ruta del archivo CSV donde guardar
    
    Returns:
        True si se guardó exitosamente, False en caso contrario
    """
    try:
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            if not countries:
                print("[WARN] No hay países para guardar")
                return False
            
            fieldnames = ['nombre', 'poblacion', 'superficie', 'continente']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for country in countries:
                writer.writerow(country)
        
        print(f"[INFO] Se guardaron {len(countries)} países en {csv_path}")
        return True
        
    except Exception as e:
        print(f"[ERROR] Error al guardar CSV: {e}")
        return False