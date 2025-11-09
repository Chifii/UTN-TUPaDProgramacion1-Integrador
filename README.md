# Sistema de Gestión de Países 🌍

## Descripción del Programa

Este es un sistema de gestión y análisis de datos de países desarrollado en Python como parte del Trabajo Práctico Integrador de Programación 1. El programa permite cargar información sobre países desde un archivo CSV y realizar diversas operaciones como búsquedas, filtros, ordenamiento, estadísticas y gestión de datos.

El sistema trabaja con información básica de cada país: nombre, población, superficie y continente, ofreciendo una interfaz interactiva por consola que facilita el manejo y análisis de los datos de manera intuitiva.

## Funcionalidades Principales

- **Carga de datos**: Importa información de países desde archivos CSV
- **Búsqueda**: Permite buscar países por nombre (exacta o parcial)
- **Filtrado**: Filtra países por continente, rango de población o superficie
- **Ordenamiento**: Ordena países por nombre, población o superficie
- **Estadísticas**: Calcula promedios, máximos, mínimos y distribución por continente
- **Gestión**: Agregar, actualizar y guardar información de países

## Estructura del Proyecto

```
UTN-TUPaDProgramacion1-Integrador/
├── src/
│   ├── main.py          # Programa principal
│   ├── menu.py          # Interfaz de usuario y menús
│   ├── csv_utils.py     # Utilidades para manejo de CSV
│   ├── queries.py       # Funciones de búsqueda y filtrado
│   └── stats.py         # Funciones de estadísticas
├── data/
│   └── paises_prueba.csv # Archivo de datos de prueba
└── docs/
    └── [documentación del proyecto]
```

## Instrucciones de Uso

### Requisitos
- Python 3.7 o superior
- Sistema operativo: Windows, macOS o Linux

### Instalación y Ejecución

1. **Clonar o descargar el proyecto**:
   ```bash
   git clone <url-del-repositorio>
   cd UTN-TUPaDProgramacion1-Integrador
   ```

2. **Ejecutar el programa**:
   ```bash
   cd src
   python main.py
   ```

3. **Usar la interfaz**:
   - El programa mostrará el menú principal automáticamente
   - Ingrese el número de la opción deseada y presione Enter
   - Siga las instrucciones en pantalla para cada funcionalidad

### Navegación por Menús

**Menú Principal:**
- `1` - Buscar país
- `2` - Filtrar países  
- `3` - Ordenar países
- `4` - Mostrar estadísticas
- `5` - Gestión de países
- `0` - Salir del programa

## Ejemplos de Entrada y Salida

### Ejemplo 1: Búsqueda de País
```
--- Menú Principal ---
Seleccione una opción: 1

--- Búsqueda de País ---
1. Búsqueda exacta
2. Búsqueda parcial
Seleccione tipo de búsqueda: 2

Ingrese el nombre del país a buscar: arg

--- Resultados de búsqueda parcial ---
Se encontraron 1 país(es):

- Argentina       | Población: 45,376,763 | Superficie: 2,780,400 km² | Continente: América
```

### Ejemplo 2: Filtrado por Continente
```
--- Filtros ---
Seleccione una opción: 1

Continentes disponibles:
1. África
2. América  
3. Asia
4. Europa
5. Oceanía

Seleccione un continente: 5

--- Países filtrados por continente: Oceanía ---
Se encontraron 2 país(es):

- Australia       | Población: 25,687,041 | Superficie: 7,692,024 km² | Continente: Oceanía
- Nueva Zelanda   | Población: 5,084,300  | Superficie: 268,021 km² | Continente: Oceanía
```

### Ejemplo 3: Estadísticas
```
--- Estadísticas ---
Seleccione una opción: 1

--- Estadísticas de Población ---
País con mayor población: China (1,412,600,000 habitantes)
País con menor población: Luxemburgo (640,064 habitantes)
Población promedio: 89,234,567 habitantes
```

### Ejemplo 4: Agregar País
```
--- Gestión de Países ---
Seleccione una opción: 1

Ingrese el nombre del país: Colombia
Ingrese la población: 50880000
Ingrese la superficie (km²): 1141748
Continentes disponibles: [América, Europa, Asia, África, Oceanía]
Ingrese el continente: América

País agregado exitosamente:
- Colombia        | Población: 50,880,000 | Superficie: 1,141,748 km² | Continente: América
```

## Participación de Integrantes

Desarrollado por:

### **Franco Vencato** 👨‍💻
- **Contribuciones principales**:
  - Diseño e implementación de la interfaz de usuario (`menu.py`)
  - Desarrollo del programa principal (`main.py`)
  - Implementación de la lógica de navegación entre menús
  - Validación de entrada de datos y manejo de errores

### **Esteban Ferreyra** 👨‍💻
- **Contribuciones principales**: 
  - Implementación del sistema de carga y procesamiento de archivos CSV (`csv_utils.py`)
  - Desarrollo de las funciones de consultas y filtrado (`queries.py`)
  - Implementación del módulo de estadísticas (`stats.py`)
  - Creación de la funcionalidad de gestión de países (agregar/actualizar)

**Trabajo en equipo**: Ambos integrantes participamos en el diseño de la arquitectura del sistema, testing, debugging y documentación. La división de tareas se realizó de manera equilibrada, aprovechando las fortalezas y los tiempos de cada integrante para crear un sistema robusto y funcional.

## Notas Técnicas

- El programa utiliza archivos CSV con codificación UTF-8
- Se validan los datos de entrada para evitar errores de ejecución  
- El sistema maneja excepciones y muestra mensajes de error informativos
- Los datos se mantienen en memoria durante la ejecución
- Los cambios se pueden guardar de vuelta al archivo CSV

## Datos de Prueba

El proyecto incluye un archivo `paises_prueba.csv` con información de 50 países para facilitar las pruebas del sistema. Los datos incluyen países de todos los continentes con diversas poblaciones y superficies.

---

*Trabajo Práctico Integrador - Programación 1*  
*Universidad Tecnológica Nacional*  
*Año 2025*
