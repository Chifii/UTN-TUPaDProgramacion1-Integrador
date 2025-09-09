# 📌 Plan de trabajo – TPI Programación 1

## 🎯 Objetivo
Desarrollar una aplicación en **Python 3.x** que permita gestionar datos de países a partir de un archivo CSV, aplicando listas, diccionarios, funciones, condicionales, ordenamientos y estadísticas.  
Entrega final: **30/09/2025**.

## 🗂️ Estructura del repositorio
```
UTN-TUPaDProgramacion1-Integrador/
├─ data/                # Dataset de países en formato CSV
│  └─ paises.csv
├─ src/                 # Código fuente Python
│  ├─ main.py
│  ├─ menu.py
│  ├─ csv_utils.py
│  ├─ queries.py
│  └─ stats.py
├─ docs/                # Documentación
│  ├─ plan_de_trabajo.md
│  ├─ marco_teorico.md
│  ├─ conclusiones.md
│  └─ capturas/
├─ README.md            # Descripción general del proyecto
```

## 🛠️ Funcionalidades requeridas
1. **Búsqueda**: por nombre de país (parcial o exacta).
2. **Filtros**:
   - Continente
   - Rango de población
   - Rango de superficie
3. **Ordenamientos**:
   - Nombre
   - Población
   - Superficie (asc/desc)
4. **Estadísticas**:
   - País con mayor y menor población
   - Promedio de población
   - Promedio de superficie
   - Cantidad de países por continente
5. **Validaciones**:
   - Manejo de errores en el CSV
   - Entradas inválidas del usuario (sin romper el programa)

## 📑 Entregables obligatorios
- **Código Python** (modular, comentado, validado).
- **Marco teórico** explicando:
  - Listas
  - Diccionarios
  - Funciones
  - Condicionales y repetitivas
  - Ordenamientos
  - Estadísticas
  - Archivos CSV
- **Capturas de pantalla** mostrando cada funcionalidad.
- **Conclusiones grupales** (aprendizajes y dificultades).
- **Repositorio GitHub**.
- **Video (10–15 min)** explicando:
  1. Problema planteado
  2. Estructura de datos
  3. Demostración del programa
  4. Reflexión final

## 👥 Distribución de tareas

- Estructura del repositorio
- `csv_utils.py` (lectura/validación de CSV)
- `menu.py` (interfaz por consola)
- `queries.py` (búsquedas, filtros y ordenamientos)
- `stats.py` (estadísticas)
- `docs/marco_teorico.md`
- `docs/conclusiones.md`
- Coordinación general y armado del README
- Capturas de pantalla
- Guion del video
- Participación en la grabación del video

## 📆 Posible cronograma
- **Semana 1:** Armar repositorio, dataset CSV, menú inicial y carga de datos.
- **Semana 2:** Implementar búsquedas, filtros y ordenamientos.
- **Semana 3:** Implementar estadísticas y validaciones.
- **Semana 4:** Documentación (marco teórico + README + capturas). Preparar video

## ✅ Criterios de evaluación
- Correcta funcionalidad de todas las opciones.
- Uso correcto de listas, diccionarios y funciones.
- Código modular, claro y comentado.
- Documentación completa y coherente.
- Video claro con participación de ambos.