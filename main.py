
def eleccion_ejercicio():
    variable = int(input("Seleccione que ejercicio desea ejecutar: (1-3)\n"))
    if variable == 1:
        import Ejercicio1
    if variable == 2:
        import Ejercicio2
    if variable == 1:
        import Ejercicio3
    else:
        eleccion_ejercicio()

eleccion_ejercicio()