#menu.py 
from typing import List, Dict, Any
def mostrar_menu():
    print("\n--- Categorías ---")
    print("1. Buscar país")
    print("2. Filtrar")
    print("3. Ordenar país")
    print("4. Mostrar Estadística")
    print("5. Para salir presione 0 ")

def Filtrar():

    while True:
        print("\n--- Categorías ---")
        print("1. Filtrar paises por Continentes")
        print("2. Filtrar paises por Rango de poblacion")
        print("3. Filtrar paises por Rango de superficie")
        print("4. Para salir presione 0 ")

        opciones=int(input())
        if opciones==1:
            print("opcion1")
        elif opciones==2:
            print("opcion2")
        elif opciones==3:
            print("opcion3")   
        elif opciones==0:
            break
        else:
            print("Ingrese opcion valida")
            
        
    
    
def Ordenar_paises():
    
    while True:
        print("\n--- Categorías ---")
        print("1. Ordenar paises por Nombre")
        print("2. Ordenar paises por poblacion")
        print("3. Ordenar paises por superficie ascendente o descendente")
        print("4. Para salir presione 0 ")
        
        opciones=int(input())
        if opciones==1:
            print("opcion1")
        elif opciones==2:
            print("opcion2")
        elif opciones==3:
            print("opcion3")   
        elif opciones==0:
            break
        else:
            print("Ingrese opcion valida")
    
def Estadisticas():
    
    while True:
        print("\n--- Categorías ---")
        print("1. País con mayor y menor población")
        print("2. Promedio de población") 
        print("3. Promedio de superficie") 
        print("4. Cantidad de países por continente")
        print("5. Para salir presione 0 ")
        opciones=int(input())
        if opciones==1:
            print("opcion1")
        elif opciones==2:
            print("opcion2")
        elif opciones==3:
            print("opcion3") 
        elif opciones==4:
            print("opcion4")  
        elif opciones==0:
            break
        else:
            print("Ingrese opcion valida")
    
def menu_principal(data: List[Dict[str, Any]]):
    
    while True:
        mostrar_menu()
        opciones=int(input())
        if opciones==1:
            print("Buscar paises")
        elif opciones==2:
            Filtrar()  
        elif opciones==3:
            Ordenar_paises()
        elif opciones==4:
            Estadisticas()
        elif opciones==0:
            break
        else:
            print("Ingrese opcion valida")

        