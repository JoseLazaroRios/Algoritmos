import math

conversion = input("'r' para convertir de grados a radianes o 'g' para convertir de radianes a grados: ")

if conversion == "r":
    grados = float(input("Ingrese los grados a convertir: "))
    radianes = math.radians(grados)
    print(f"{grados} grados equivalen a {radianes} radianes.")
elif conversion == "g":
    radianes = float(input("Ingrese los radianes a convertir: "))
    grados = math.degrees(radianes)
    print(f"{radianes} radianes equivalen a {grados} grados.")
else:
    print("Opción no válida.")