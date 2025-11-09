# src/stats.py
from typing import List, Dict, Any, Tuple, Optional

def get_country_with_max_population(countries: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    Encuentra el país con mayor población.
    
    Args:
        countries: Lista de diccionarios con datos de países
    
    Returns:
        Diccionario con los datos del país con mayor población, o None si la lista está vacía
    """
    if not countries:
        return None
    
    return max(countries, key=lambda x: x['poblacion'])

def get_country_with_min_population(countries: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    Encuentra el país con menor población.
    
    Args:
        countries: Lista de diccionarios con datos de países
    
    Returns:
        Diccionario con los datos del país con menor población, o None si la lista está vacía
    """
    if not countries:
        return None
    
    return min(countries, key=lambda x: x['poblacion'])

def get_population_stats(countries: List[Dict[str, Any]]) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """
    Obtiene estadísticas de población (mayor y menor).
    
    Args:
        countries: Lista de diccionarios con datos de países
    
    Returns:
        Tupla con (país_mayor_población, país_menor_población)
    """
    max_country = get_country_with_max_population(countries)
    min_country = get_country_with_min_population(countries)
    
    return max_country, min_country

def calculate_average_population(countries: List[Dict[str, Any]]) -> float:
    """
    Calcula el promedio de población de los países.
    
    Args:
        countries: Lista de diccionarios con datos de países
    
    Returns:
        Promedio de población, o 0 si la lista está vacía
    """
    if not countries:
        return 0.0
    
    total_population = sum(country['poblacion'] for country in countries)
    return total_population / len(countries)

def calculate_average_surface(countries: List[Dict[str, Any]]) -> float:
    """
    Calcula el promedio de superficie de los países.
    
    Args:
        countries: Lista de diccionarios con datos de países
    
    Returns:
        Promedio de superficie en km², o 0 si la lista está vacía
    """
    if not countries:
        return 0.0
    
    total_surface = sum(country['superficie'] for country in countries)
    return total_surface / len(countries)

def count_countries_by_continent(countries: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Cuenta la cantidad de países por continente.
    
    Args:
        countries: Lista de diccionarios con datos de países
    
    Returns:
        Diccionario con continente como clave y cantidad de países como valor
    """
    continent_count = {}
    
    for country in countries:
        continent = country['continente']
        continent_count[continent] = continent_count.get(continent, 0) + 1
    
    return continent_count

def get_continent_with_most_countries(countries: List[Dict[str, Any]]) -> Tuple[Optional[str], int]:
    """
    Encuentra el continente con más países.
    
    Args:
        countries: Lista de diccionarios con datos de países
    
    Returns:
        Tupla con (nombre_continente, cantidad_países)
    """
    continent_count = count_countries_by_continent(countries)
    
    if not continent_count:
        return None, 0
    
    max_continent = max(continent_count.items(), key=lambda x: x[1])
    return max_continent[0], max_continent[1]

def get_continent_with_least_countries(countries: List[Dict[str, Any]]) -> Tuple[Optional[str], int]:
    """
    Encuentra el continente con menos países.
    
    Args:
        countries: Lista de diccionarios con datos de países
    
    Returns:
        Tupla con (nombre_continente, cantidad_países)
    """
    continent_count = count_countries_by_continent(countries)
    
    if not continent_count:
        return None, 0
    
    min_continent = min(continent_count.items(), key=lambda x: x[1])
    return min_continent[0], min_continent[1]

def get_total_world_population(countries: List[Dict[str, Any]]) -> int:
    """
    Calcula la población total mundial (suma de todos los países).
    
    Args:
        countries: Lista de diccionarios con datos de países
    
    Returns:
        Población total
    """
    return sum(country['poblacion'] for country in countries)

def get_total_world_surface(countries: List[Dict[str, Any]]) -> int:
    """
    Calcula la superficie total mundial (suma de todos los países).
    
    Args:
        countries: Lista de diccionarios con datos de países
    
    Returns:
        Superficie total en km²
    """
    return sum(country['superficie'] for country in countries)

def get_population_density_stats(countries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Calcula la densidad poblacional de cada país (población/superficie).
    
    Args:
        countries: Lista de diccionarios con datos de países
    
    Returns:
        Lista de países con densidad poblacional agregada
    """
    countries_with_density = []
    
    for country in countries:
        country_copy = country.copy()
        density = country['poblacion'] / country['superficie'] if country['superficie'] > 0 else 0
        country_copy['densidad_poblacional'] = round(density, 2)
        countries_with_density.append(country_copy)
    
    return countries_with_density
