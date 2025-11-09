# src/queries.py
from typing import List, Dict, Any, Optional

def search_countries_by_name(countries: List[Dict[str, Any]], search_term: str, exact_match: bool = False) -> List[Dict[str, Any]]:
    """
    Busca países por nombre (búsqueda parcial o exacta).
    
    Args:
        countries: Lista de diccionarios con datos de países
        search_term: Término de búsqueda
        exact_match: Si True, busca coincidencia exacta; si False, busca coincidencia parcial
    
    Returns:
        Lista de países que coinciden con el término de búsqueda
    """
    results = []
    search_term_lower = search_term.lower().strip()
    
    if not search_term_lower:
        return results
    
    for country in countries:
        country_name = country['nombre'].lower()
        
        if exact_match:
            if country_name == search_term_lower:
                results.append(country)
        else:
            if search_term_lower in country_name:
                results.append(country)
    
    return results

def filter_countries_by_continent(countries: List[Dict[str, Any]], continent: str) -> List[Dict[str, Any]]:
    """
    Filtra países por continente.
    
    Args:
        countries: Lista de diccionarios con datos de países
        continent: Nombre del continente
    
    Returns:
        Lista de países del continente especificado
    """
    continent_lower = continent.lower().strip()
    results = []
    
    for country in countries:
        if country['continente'].lower() == continent_lower:
            results.append(country)
    
    return results

def filter_countries_by_population_range(countries: List[Dict[str, Any]], min_pop: int, max_pop: int) -> List[Dict[str, Any]]:
    """
    Filtra países por rango de población.
    
    Args:
        countries: Lista de diccionarios con datos de países
        min_pop: Población mínima
        max_pop: Población máxima
    
    Returns:
        Lista de países dentro del rango de población
    """
    results = []
    
    for country in countries:
        population = country['poblacion']
        if min_pop <= population <= max_pop:
            results.append(country)
    
    return results

def filter_countries_by_surface_range(countries: List[Dict[str, Any]], min_surface: int, max_surface: int) -> List[Dict[str, Any]]:
    """
    Filtra países por rango de superficie.
    
    Args:
        countries: Lista de diccionarios con datos de países
        min_surface: Superficie mínima en km²
        max_surface: Superficie máxima en km²
    
    Returns:
        Lista de países dentro del rango de superficie
    """
    results = []
    
    for country in countries:
        surface = country['superficie']
        if min_surface <= surface <= max_surface:
            results.append(country)
    
    return results

def sort_countries_by_name(countries: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    """
    Ordena países por nombre.
    
    Args:
        countries: Lista de diccionarios con datos de países
        ascending: Si True ordena ascendente, si False descendente
    
    Returns:
        Lista de países ordenada por nombre
    """
    return sorted(countries, key=lambda x: x['nombre'].lower(), reverse=not ascending)

def sort_countries_by_population(countries: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    """
    Ordena países por población.
    
    Args:
        countries: Lista de diccionarios con datos de países
        ascending: Si True ordena ascendente, si False descendente
    
    Returns:
        Lista de países ordenada por población
    """
    return sorted(countries, key=lambda x: x['poblacion'], reverse=not ascending)

def sort_countries_by_surface(countries: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    """
    Ordena países por superficie.
    
    Args:
        countries: Lista de diccionarios con datos de países
        ascending: Si True ordena ascendente, si False descendente
    
    Returns:
        Lista de países ordenada por superficie
    """
    return sorted(countries, key=lambda x: x['superficie'], reverse=not ascending)

def get_available_continents(countries: List[Dict[str, Any]]) -> List[str]:
    """
    Obtiene la lista de continentes disponibles en el dataset.
    
    Args:
        countries: Lista de diccionarios con datos de países
    
    Returns:
        Lista de continentes únicos
    """
    continents = set()
    for country in countries:
        continents.add(country['continente'])
    
    return sorted(list(continents))

def add_country(countries: List[Dict[str, Any]], nombre: str, poblacion: int, superficie: int, continente: str) -> bool:
    """
    Agrega un nuevo país a la lista de países.
    
    Args:
        countries: Lista de diccionarios con datos de países
        nombre: Nombre del país
        poblacion: Población del país
        superficie: Superficie del país en km²
        continente: Continente del país
    
    Returns:
        True si el país fue agregado exitosamente, False si ya existe
    """
    existing_countries = search_countries_by_name(countries, nombre, exact_match=True)
    if existing_countries:
        return False
    
    if not nombre.strip() or poblacion <= 0 or superficie <= 0 or not continente.strip():
        raise ValueError("Todos los campos deben ser válidos y positivos")
    
    new_country = {
        'nombre': nombre.strip(),
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente.strip()
    }
    
    countries.append(new_country)
    return True

def update_country(countries: List[Dict[str, Any]], nombre: str, nueva_poblacion: Optional[int] = None, nueva_superficie: Optional[int] = None) -> bool:
    """
    Actualiza la población y/o superficie de un país existente.
    
    Args:
        countries: Lista de diccionarios con datos de países
        nombre: Nombre del país a actualizar
        nueva_poblacion: Nueva población (opcional)
        nueva_superficie: Nueva superficie (opcional)
    
    Returns:
        True si el país fue actualizado exitosamente, False si no se encontró
    """
    for country in countries:
        if country['nombre'].lower() == nombre.lower().strip():
            if nueva_poblacion is not None:
                if nueva_poblacion <= 0:
                    raise ValueError("La población debe ser positiva")
                country['poblacion'] = nueva_poblacion
            
            if nueva_superficie is not None:
                if nueva_superficie <= 0:
                    raise ValueError("La superficie debe ser positiva")
                country['superficie'] = nueva_superficie
            
            return True
    
    return False
