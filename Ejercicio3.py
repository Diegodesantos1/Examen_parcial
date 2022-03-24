import random
from datetime import datetime
class Cuenta_Bancaria:
    def __init__(self, ID, nombre_titular,fecha_apertura, numero_cuenta, saldo):
        self.ID=ID
        self.nombre_titular=nombre_titular
        self.fecha_apertura=fecha_apertura
        self.numero_cuenta=numero_cuenta
        self.saldo=saldo
    def crear_datos_cuentas():
        datos=[]
        numero_cuenta= random.randint(100000000000,999999999999)
        nombre_titular = "Diego de Santos"
        numero = random.randin(0,3)
        numero2 = random.randint(4,6)
        numero3= random.randint(7,9)
        ID = f"{numero}{numero2}{numero3}"
        fecha_apertura = random.randint(1900,2000)
        fecha_vencimiento = random.randint(2001, 2022)
        saldo = "10000"
        datos.append(ID) ; datos.append(nombre_titular) ; datos.append(fecha_apertura) ; datos.append(fecha_vencimiento) ; datos.append(numero_cuenta) ; datos.append(saldo)

    def ingresar_dinero():
        datos =["ID1234","Diego de Santos", "10/05/2022", "ES12345678", "10000"]
        print("¿Cuánto dinero quiere ingresar a su cuenta?")
        saldo = datos.pop(4)
        print(f"Su saldo actual es de {saldo}€")
        saldo = float(saldo)
        dinero_añadir=float(input())
        dinero_total=saldo + dinero_añadir
        print(f"El saldo de su cuenta es {dinero_total} €")
    def retirar_dinero():
        datos =["ID1234","Diego de Santos", "10/05/2022", "ES12345678", "10000"]
        saldo = datos.pop(4)
        saldo = float(saldo)
        dinero_retirar=float(input(f"Su saldo actual es de {saldo}\n¿Cuánto dinero desea retirar?\n"))
        if saldo - dinero_retirar < 0:
            print("\nOperación no válida, no tienes tanto capital")
        else:
            saldo_final = saldo - dinero_retirar
            print(f"Su saldo final es {saldo_final}")
    def trasferir_dinero():
        datos =["ID1234","Diego de Santos", "10/05/2022", "ES12345678", "10000"]
        saldo = datos.pop(4)
        saldo = float(saldo)
        dinero_trasferir=float(input(f"Su saldo actual es de {saldo}\n¿Cuánto dinero desea trasferir?\n"))
        if saldo - dinero_trasferir < 0:
            print("\nOperación no válida, no tienes tanto capital")
        else:
            saldo_final = saldo - dinero_trasferir
            print(f"Su saldo final es {saldo_final} € y ha enviado a la cuenta de Rubén {dinero_trasferir} €")
    def retirar_dinero_fijo():
        datos =["ID1234","Diego de Santos", "10/05/2022", "ES12345678", "3000"]
        hora_actual=str(datetime.now().time())
        print(f" la hora actual es {hora_actual} y cómo el plazo fijo estaba vigente hasta el mes que viene, me temo que le cobraremos una comisión")
        saldo = datos.pop(4)
        saldo = float(saldo)
        dinero_retirar=float(input(f"Su saldo actual es de {saldo}\n¿Cuánto dinero desea retirar?\n"))
        if saldo - dinero_retirar < 0:
            print("\nOperación no válida, no tienes tanto capital")
        else:
            saldo_final = saldo - (dinero_retirar + saldo * 0.05)
            print(f"Su saldo final es {saldo_final}")
    def retirar_dinero_VIP():
        datos =["ID1234","Diego de Santos", "10/05/2022", "ES12345678", "10000"]
        saldo = datos.pop(4)
        saldo = float(saldo)
        dinero_retirar=float(input(f"Su saldo actual es de {saldo}\n¿Cuánto dinero desea retirar?\n"))
        saldo_final = saldo - dinero_retirar
        print(f"Su saldo final es {saldo_final}")
    def trasferir_dinero_VIP():
        datos =["ID1234","Diego de Santos", "10/05/2022", "ES12345678", "10000"]
        saldo = datos.pop(4)
        saldo = float(saldo)
        dinero_trasferir=float(input(f"Su saldo actual es de {saldo}\n¿Cuánto dinero desea trasferir?\n"))
        saldo_final = saldo - dinero_trasferir
        print(f"Su saldo final es {saldo_final} € y ha enviado a la cuenta de Rubén {dinero_trasferir} €")
    datos=["ID1234","Diego de Santos", "10/05/2022", "ES12345678", "1000€"]
    print(f"\nLos datos de su cuenta bancaria son los siguientes: {datos}\n")
    print("\nQué desea hacer con su cuenta bancaria\n --> 1: Cuenta corriente\n --> 2: Cuenta Plazo\n --> 3: Cuenta Vip")
    tipo_cuenta = int(input())
    if tipo_cuenta == 1:
        print("\nQué desea hacer con su cuenta bancaria\n --> 1: Ingresar Dinero\n --> 2: Retirar Dinero\n --> 3: Trasferir Dinero\n --> 4: Plazo fijo (Sólo válido para cuentas Plazo)\n")
        eleccion=int(input())
        if eleccion == 1:
            ingresar_dinero()
        elif eleccion == 2:
            retirar_dinero()
        elif eleccion == 3:
            trasferir_dinero()
        else:
            exit()
    elif tipo_cuenta == 2:
        print("\nQué desea hacer con su cuenta Plazo Fijo\n --> 1: Ingresar Dinero\n --> 2: Retirar Dinero\n --> 3: Trasferir Dinero\n")
        eleccion=int(input())
        if eleccion == 1:
            ingresar_dinero()
        elif eleccion == 2:
            retirar_dinero_fijo()
        elif eleccion == 3:
            trasferir_dinero()
        else:
            exit()
    elif tipo_cuenta == 3:
        print("\nQué desea hacer con su cuenta VIP\n --> 1: Ingresar Dinero\n --> 2: Retirar Dinero\n --> 3: Trasferir Dinero\n")
        eleccion=int(input())
        if eleccion == 1:
            ingresar_dinero()
        elif eleccion == 2:
            retirar_dinero_VIP()
        elif eleccion == 3:
            trasferir_dinero_VIP()
        else:
            exit()


Cuenta_Bancaria
