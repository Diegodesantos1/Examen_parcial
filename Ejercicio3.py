class Cuenta_Bancaria:
    def __init__(self, ID, nombre_titular,fecha_apertura, numero_cuenta, saldo):
        self.ID=ID
        self.nombre_titular=nombre_titular
        self.fecha_apertura=fecha_apertura
        self.numero_cuenta=numero_cuenta
        self.saldo=saldo
    def crear_cuenta():
        datos=["ID1234","Diego de Santos", "10/05/2022", "ES12345678", "300€"]
        print(datos)
Cuenta_Bancaria.crear_cuenta()
class Operaciones_cuenta(Cuenta_Bancaria):
    print("Qué desea hacer con su cuenta bancaria\n --> 1: Ingresar Dinero\n --> 2: Retirar Dinero\n --> 3: Trasferir Dinero\n")
    eleccion=int(input())
    if eleccion == 1:
        def ingresar_dinero():
            print("¿Cuánto dinero quiere ingresar a su cuenta?")

            dinero_añadir=float(input())
            dinero_total=float(saldo) + dinero_añadir





Operaciones_cuenta