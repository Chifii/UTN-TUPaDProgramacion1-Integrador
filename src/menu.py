# menu.py 
from typing import List, Dict, Any
from csv_utils import print_country, save_countries
from queries import (
    search_countries_by_name, 
    filter_countries_by_continent,
    filter_countries_by_population_range,
    filter_countries_by_surface_range,
    sort_countries_by_name,
    sort_countries_by_population,
    sort_countries_by_surface,
    get_available_continents,
    add_country,
    update_country
)
from stats import (
    get_population_stats,
    calculate_average_population,
    calculate_average_surface,
    count_countries_by_continent
)

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Buscar país")
    print("2. Filtrar")
    print("3. Ordenar países")
    print("4. Mostrar Estadísticas")
    print("5. Gestión de Países")
    print("0. Salir")
    print("Seleccione una opción: ", end="")

def obtener_opcion_valida(mensaje: str, opciones_validas: List[int]) -> int:
    """Obtiene una opción válida del usuario con validación."""
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in opciones_validas:
                return opcion
            else:
                print(f"Opción inválida. Seleccione una opción entre: {opciones_validas}")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def mostrar_resultados(paises: List[Dict[str, Any]], titulo: str):
    """Muestra los resultados de una consulta."""
    print(f"\n--- {titulo} ---")
    if not paises:
        print("No se encontraron países que coincidan con los criterios.")
    else:
        print(f"Se encontraron {len(paises)} país(es):\n")
        for pais in paises:
            print_country(pais)

def buscar_pais(data: List[Dict[str, Any]]):
    """Maneja la búsqueda de países."""
    print("\n--- Búsqueda de País ---")
    print("1. Búsqueda exacta")
    print("2. Búsqueda parcial")
    print("0. Volver")
    
    opcion = obtener_opcion_valida("Seleccione tipo de búsqueda: ", [0, 1, 2])
    
    if opcion == 0:
        return
    
    termino = input("Ingrese el nombre del país a buscar: ").strip()
    if not termino:
        print("Debe ingresar un término de búsqueda.")
        return
    
    exact_match = (opcion == 1)
    resultados = search_countries_by_name(data, termino, exact_match)
    
    tipo_busqueda = "exacta" if exact_match else "parcial"
    mostrar_resultados(resultados, f"Resultados de búsqueda {tipo_busqueda}")

def filtrar(data: List[Dict[str, Any]]):
    """Maneja el menú de filtros."""
    while True:
        print("\n--- Filtros ---")
        print("1. Filtrar países por Continente")
        print("2. Filtrar países por Rango de población")
        print("3. Filtrar países por Rango de superficie")
        print("0. Volver")
        
        opcion = obtener_opcion_valida("Seleccione una opción: ", [0, 1, 2, 3])
        
        if opcion == 0:
            break
        elif opcion == 1:
            filtrar_por_continente(data)
        elif opcion == 2:
            filtrar_por_poblacion(data)
        elif opcion == 3:
            filtrar_por_superficie(data)

def filtrar_por_continente(data: List[Dict[str, Any]]):
    """Filtra países por continente."""
    continentes = get_available_continents(data)
    
    print("\n--- Continentes disponibles ---")
    for i, continente in enumerate(continentes, 1):
        print(f"{i}. {continente}")
    
    opcion = obtener_opcion_valida("Seleccione un continente: ", list(range(1, len(continentes) + 1)))
    continente_seleccionado = continentes[opcion - 1]
    
    resultados = filter_countries_by_continent(data, continente_seleccionado)
    mostrar_resultados(resultados, f"Países de {continente_seleccionado}")

def filtrar_por_poblacion(data: List[Dict[str, Any]]):
    """Filtra países por rango de población."""
    try:
        min_pop = int(input("Ingrese población mínima: "))
        max_pop = int(input("Ingrese población máxima: "))
        
        if min_pop < 0 or max_pop < 0 or min_pop > max_pop:
            print("Rango de población inválido.")
            return
        
        resultados = filter_countries_by_population_range(data, min_pop, max_pop)
        mostrar_resultados(resultados, f"Países con población entre {min_pop:,} y {max_pop:,}")
        
    except ValueError:
        print("Por favor, ingrese números válidos.")

def filtrar_por_superficie(data: List[Dict[str, Any]]):
    """Filtra países por rango de superficie."""
    try:
        min_surface = int(input("Ingrese superficie mínima (km²): "))
        max_surface = int(input("Ingrese superficie máxima (km²): "))
        
        if min_surface < 0 or max_surface < 0 or min_surface > max_surface:
            print("Rango de superficie inválido.")
            return
        
        resultados = filter_countries_by_surface_range(data, min_surface, max_surface)
        mostrar_resultados(resultados, f"Países con superficie entre {min_surface:,} y {max_surface:,} km²")
        
    except ValueError:
        print("Por favor, ingrese números válidos.")

def ordenar_paises(data: List[Dict[str, Any]]):
    """Maneja el menú de ordenamiento."""
    while True:
        print("\n--- Ordenamiento ---")
        print("1. Ordenar países por Nombre")
        print("2. Ordenar países por Población")
        print("3. Ordenar países por Superficie")
        print("0. Volver")
        
        opcion = obtener_opcion_valida("Seleccione una opción: ", [0, 1, 2, 3])
        
        if opcion == 0:
            break
        elif opcion == 1:
            ordenar_por_nombre(data)
        elif opcion == 2:
            ordenar_por_poblacion(data)
        elif opcion == 3:
            ordenar_por_superficie(data)

def obtener_orden():
    """Obtiene el orden de clasificación del usuario."""
    print("1. Ascendente")
    print("2. Descendente")
    opcion = obtener_opcion_valida("Seleccione el orden: ", [1, 2])
    return opcion == 1  # True para ascendente, False para descendente

def ordenar_por_nombre(data: List[Dict[str, Any]]):
    """Ordena países por nombre."""
    ascending = obtener_orden()
    resultados = sort_countries_by_name(data, ascending)
    orden_texto = "ascendente" if ascending else "descendente"
    mostrar_resultados(resultados, f"Países ordenados por nombre ({orden_texto})")

def ordenar_por_poblacion(data: List[Dict[str, Any]]):
    """Ordena países por población."""
    ascending = obtener_orden()
    resultados = sort_countries_by_population(data, ascending)
    orden_texto = "ascendente" if ascending else "descendente"
    mostrar_resultados(resultados, f"Países ordenados por población ({orden_texto})")

def ordenar_por_superficie(data: List[Dict[str, Any]]):
    """Ordena países por superficie."""
    ascending = obtener_orden()
    resultados = sort_countries_by_surface(data, ascending)
    orden_texto = "ascendente" if ascending else "descendente"
    mostrar_resultados(resultados, f"Países ordenados por superficie ({orden_texto})")

def estadisticas(data: List[Dict[str, Any]]):
    """Maneja el menú de estadísticas."""
    while True:
        print("\n--- Estadísticas ---")
        print("1. País con mayor y menor población")
        print("2. Promedio de población")
        print("3. Promedio de superficie")
        print("4. Cantidad de países por continente")
        print("0. Volver")
        
        opcion = obtener_opcion_valida("Seleccione una opción: ", [0, 1, 2, 3, 4])
        
        if opcion == 0:
            break
        elif opcion == 1:
            mostrar_estadisticas_poblacion(data)
        elif opcion == 2:
            mostrar_promedio_poblacion(data)
        elif opcion == 3:
            mostrar_promedio_superficie(data)
        elif opcion == 4:
            mostrar_paises_por_continente(data)

def mostrar_estadisticas_poblacion(data: List[Dict[str, Any]]):
    """Muestra estadísticas de población."""
    max_country, min_country = get_population_stats(data)
    
    print("\n--- Estadísticas de Población ---")
    if max_country:
        print("País con MAYOR población:")
        print_country(max_country)
    
    if min_country:
        print("\nPaís con MENOR población:")
        print_country(min_country)

def mostrar_promedio_poblacion(data: List[Dict[str, Any]]):
    """Muestra el promedio de población."""
    promedio = calculate_average_population(data)
    print(f"\n--- Promedio de Población ---")
    print(f"Promedio de población mundial: {promedio:,.2f} habitantes")

def mostrar_promedio_superficie(data: List[Dict[str, Any]]):
    """Muestra el promedio de superficie."""
    promedio = calculate_average_surface(data)
    print(f"\n--- Promedio de Superficie ---")
    print(f"Promedio de superficie mundial: {promedio:,.2f} km²")

def mostrar_paises_por_continente(data: List[Dict[str, Any]]):
    """Muestra la cantidad de países por continente."""
    estadisticas_continente = count_countries_by_continent(data)
    
    print("\n--- Cantidad de Países por Continente ---")
    for continente, cantidad in sorted(estadisticas_continente.items()):
        print(f"{continente}: {cantidad} país(es)")
    
    total = sum(estadisticas_continente.values())
    print(f"\nTotal de países: {total}")

def gestion_paises(data: List[Dict[str, Any]], csv_path: str):
    """Maneja el menú de gestión de países."""
    while True:
        print("\n--- Gestión de Países ---")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Guardar cambios")
        print("0. Volver")
        
        opcion = obtener_opcion_valida("Seleccione una opción: ", [0, 1, 2, 3])
        
        if opcion == 0:
            break
        elif opcion == 1:
            agregar_pais(data)
        elif opcion == 2:
            actualizar_pais(data)
        elif opcion == 3:
            guardar_cambios(data, csv_path)

def agregar_pais(data: List[Dict[str, Any]]):
    """Agrega un nuevo país al sistema."""
    print("\n--- Agregar Nuevo País ---")
    
    try:
        nombre = input("Ingrese el nombre del país: ").strip()
        if not nombre:
            print("El nombre del país no puede estar vacío.")
            return
        
        poblacion_str = input("Ingrese la población: ").strip()
        poblacion = int(poblacion_str)
        
        superficie_str = input("Ingrese la superficie (km²): ").strip()
        superficie = int(superficie_str)
        
        continentes_disponibles = get_available_continents(data)
        print("\nContinentes disponibles:")
        for i, cont in enumerate(continentes_disponibles, 1):
            print(f"{i}. {cont}")
        print(f"{len(continentes_disponibles) + 1}. Ingresar nuevo continente")
        
        cont_opcion = obtener_opcion_valida("Seleccione un continente: ", 
                                          list(range(1, len(continentes_disponibles) + 2)))
        
        if cont_opcion == len(continentes_disponibles) + 1:
            continente = input("Ingrese el nuevo continente: ").strip()
            if not continente:
                print("El continente no puede estar vacío.")
                return
        else:
            continente = continentes_disponibles[cont_opcion - 1]
        
        if add_country(data, nombre, poblacion, superficie, continente):
            print(f"\nPaís '{nombre}' agregado exitosamente!")
            print("Nuevo país:")
            print_country({'nombre': nombre, 'poblacion': poblacion, 'superficie': superficie, 'continente': continente})
        else:
            print(f"\nEl país '{nombre}' ya existe en el sistema.")
            
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")

def actualizar_pais(data: List[Dict[str, Any]]):
    """Actualiza la población y/o superficie de un país existente."""
    print("\n--- Actualizar País ---")
    
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()
    if not nombre:
        print("El nombre del país no puede estar vacío.")
        return
    
    paises_encontrados = search_countries_by_name(data, nombre, exact_match=True)
    if not paises_encontrados:
        print(f"No se encontró el país '{nombre}'. Verifique el nombre.")
        return
    
    pais_actual = paises_encontrados[0]
    print(f"\nPaís encontrado:")
    print_country(pais_actual)
    
    try:
        print(f"\nDatos actuales:")
        print(f"Población: {pais_actual['poblacion']:,}")
        print(f"Superficie: {pais_actual['superficie']:,} km²")
        
        # Obtener nuevos valores
        print("\n--- Ingrese los nuevos valores (Enter para mantener actual) ---")
        
        nueva_poblacion = None
        poblacion_input = input("Nueva población: ").strip()
        if poblacion_input:
            nueva_poblacion = int(poblacion_input)
        
        nueva_superficie = None
        superficie_input = input("Nueva superficie (km²): ").strip()
        if superficie_input:
            nueva_superficie = int(superficie_input)
        
        if nueva_poblacion is None and nueva_superficie is None:
            print("Debe actualizar al menos un campo.")
            return
        
        if update_country(data, nombre, nueva_poblacion, nueva_superficie):
            print(f"\nPaís '{nombre}' actualizado exitosamente!")
            print("Datos actualizados:")
            # Buscar el país actualizado para mostrarlo
            pais_actualizado = search_countries_by_name(data, nombre, exact_match=True)[0]
            print_country(pais_actualizado)
        else:
            print(f"Error al actualizar el país '{nombre}'.")
            
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")

def guardar_cambios(data: List[Dict[str, Any]], csv_path: str):
    """Guarda los cambios en el archivo CSV."""
    print("\n--- Guardar Cambios ---")
    print("¿Está seguro que desea guardar todos los cambios en el archivo CSV?")
    print("Esta acción sobrescribirá el archivo actual.")
    
    confirmacion = input("Escriba 'SI' para confirmar: ").strip().upper()
    
    if confirmacion == 'SI':
        if save_countries(data, csv_path):
            print("Cambios guardados exitosamente en el archivo.")
        else:
            print("Error al guardar los cambios.")
    else:
        print("Operación cancelada. Los cambios no se guardaron.")

def menu_principal(data: List[Dict[str, Any]], csv_path: str = ""):
    """Menú principal de la aplicación."""
    if not data:
        print("No hay datos disponibles.")
        return
    
    while True:
        mostrar_menu()
        opcion = obtener_opcion_valida("", [0, 1, 2, 3, 4, 5])
        
        if opcion == 0:
            print("\n¡Gracias por usar el sistema de consulta de países!")
            break
        elif opcion == 1:
            buscar_pais(data)
        elif opcion == 2:
            filtrar(data)
        elif opcion == 3:
            ordenar_paises(data)
        elif opcion == 4:
            estadisticas(data)
        elif opcion == 5:
            gestion_paises(data, csv_path)