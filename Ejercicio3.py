class Cuenta_Bancaria:
    def __init__(self, ID, nombre_titular,fecha_apertura, numero_cuenta, saldo):
        self.ID=ID
        self.nombre_titular=nombre_titular
        self.fecha_apertura=fecha_apertura
        self.numero_cuenta=numero_cuenta
        self.saldo=saldo
    def ingresar_dinero():
        datos =["ID1234","Diego de Santos", "10/05/2022", "ES12345678", "300"]
        print("¿Cuánto dinero quiere ingresar a su cuenta?")
        saldo = datos.pop(4)
        print(f"Su saldo actual es de {saldo}€")
        saldo = float(saldo)
        dinero_añadir=float(input())
        dinero_total=saldo + dinero_añadir
        print(f"El saldo de su cuenta es {dinero_total} €")
    def retirar_dinero():
        datos =["ID1234","Diego de Santos", "10/05/2022", "ES12345678", "300"]
        saldo = datos.pop(4)
        saldo = float(saldo)
        dinero_retirar=float(input(f"Su saldo actual es de {saldo}\n¿Cuánto dinero desea retirar?\n"))
        if saldo - dinero_retirar < 0:
            print("\nOperación no válida, no tienes tanto capital")
        else:
            saldo_final = saldo - dinero_retirar
            print(f"Su saldo final es {saldo_final}")
    def trasferir_dinero():
        datos =["ID1234","Diego de Santos", "10/05/2022", "ES12345678", "300"]
        saldo = datos.pop(4)
        saldo = float(saldo)
        dinero_trasferir=float(input(f"Su saldo actual es de {saldo}\n¿Cuánto dinero desea trasferir?\n"))
        if saldo - dinero_trasferir < 0:
            print("\nOperación no válida, no tienes tanto capital")
        else:
            saldo_final = saldo - dinero_trasferir
            print(f"Su saldo final es {saldo_final} € y ha enviado a la cuenta de Rubén {dinero_trasferir} €")
    datos=["ID1234","Diego de Santos", "10/05/2022", "ES12345678", "300€"]
    print(f"\nLos datos de su cuenta bancaria son los siguientes: {datos}\n")
    print("\nQué desea hacer con su cuenta bancaria\n --> 1: Ingresar Dinero\n --> 2: Retirar Dinero\n --> 3: Trasferir Dinero\n")
    eleccion=int(input())
    if eleccion == 1:
        ingresar_dinero()
    if eleccion == 2:
        retirar_dinero()
    if eleccion == 3:
        trasferir_dinero()
    else:
        exit()
class Plazo_fijo(Cuenta_Bancaria):
    pass
Cuenta_Bancaria
