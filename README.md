<h1 align="center">POO con archivos</h1>

*He usado la Programación Orientada a Objetos para resolver este examen*

---

En este [repositorio](https://github.com/Diegodesantos1/Examen_parcial) queda resuelto el examen.
***

## Índice
1. [Ejercicio 1](#id1)
2. [Ejercicio 2](#id1)
3. [Ejercicio 3](#id1)

***

## Ejercicio 1<a name="id1"></a>

Enunciado: Escriba una clase que permita describir un libro y situar los valores asociados. Dar un ejemplo de uso en Python.

```python
class Libro:
    def __init__(self, autor, año,nombre, codigo):
        self.autor=autor
        self.año=año
        self.nombre=nombre
        self.codigo=codigo
    def ocurrir_Libro(self):
        txt= "{0},{1},{2},{3}"
        return txt.format(self.nombre, self.autor,self.año, self.codigo)

A=Libro("Don Quijote","Cervantes", "1534", "12345678") ; B=Libro("La sombra del viento","Carlos Ruiz Zafón","2002", "536792") ; C=Libro("Harry Potter","J.K Rowling","1985", "6157368179")
print(A.ocurrir_Libro()) ; print(B.ocurrir_Libro()) ; print(C.ocurrir_Libro())
```

## Ejercicio 2<a name="id2"></a>

Considere los objetos siguientes:
Animal
Mamífero
Ovíparo
Pollo
Gato
Ornitorrinco
Describa las relaciones entre los diferentes objetos. El diagrama asociado se llama diagrama de clases.
Dar un ejemplo de descripción algorítmica de las clases asociadas (únicamente la declaración de clase XXX).
¿Es posible implementar estos objetos en Python?

```python
class Animal:
    print("Soy un animal")

class Mamífero(Animal):
    super(Animal)
    print("Soy un mamífero")

class Ovíparo(Mamífero):
    super(Mamífero)
    print("Soy ovíparo")
class Pollo(Ovíparo):
    super(Ovíparo)
    print("Soy un pollo")

class Gato (Mamífero):
    super(Mamífero)
    print("Soy un gato")
class Ornitorrinco(Ovíparo):
    super(Ovíparo)
    print("Soy ornitorrinco")

Animal
Mamífero
Ovíparo
Pollo
Gato
Ornitorrinco
```

## Ejercicio 3<a name="id2"></a>

Enunciado: Se pide crear una clase que refleje una cuenta bancaria. Esta clase va a tener cómo atributos el ID de la cuenta bancaria, el nombre de titular, una fecha de apertura, un número de cuenta y un saldo. Por favor, aplique el tipo que mejor corresponda a cada atributo. 

La cuenta bancaria deberá tener como mínimo un método para retirar dinero, otro para ingresar dinero y otro para transferir dinero de una cuenta bancaria a otra cuenta bancaria. De una cuenta bancaria no se podrá retirar nunca dinero (ni transferir) si la cantidad de dinero a retirar o transferir es mayor que el saldo.

Crea una cuenta bancaria a Plazo Fijo, en la cual cuando se retira dinero de algún modo antes de una Fecha de Vencimiento además del dinero a retirar se penaliza con un 5% adicional.

Crea además una cuenta Vip, que tendrá un atributo adicional que es el saldo negativo máximo que puede tener. En las cuentas Vip uno podrá tener saldo negativo siempre que no supere este valor.

 A continuación, construye una aplicación que permita crear los tres tipos de cuentas. El ID tiene que ser un número entero incremental, el nombre del titular puede ser inventado, la fecha de apertura y fecha de vencimiento deben ser aleatorias siendo la fecha de apertura más antigua que la fecha de vencimiento, y el número de cuenta tiene que ser un número aleatorio de 12 dígitos. Cuando las cuentas estén iniciadas a un sueldo inicial de 10.000 €, transferir dinero de unas a otras las cantidades de 2000 €, ingresar 575 € y retirar dinero 78 €. 


```python
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
        global datos
        datos=[]
        numero_cuenta= random.randint(100000000000,999999999999)
        nombre_titular = "Diego de Santos"
        numero = random.randint(0,3)
        numero2 = random.randint(4,6)
        numero3= random.randint(7,9)
        ID = f"{numero}{numero2}{numero3}"
        fecha_apertura = random.randint(1900,2000)
        fecha_vencimiento = random.randint(2001, 2022)
        saldo = "10000"
        datos.append(ID) ; datos.append(nombre_titular) ; datos.append(fecha_apertura) ; datos.append(fecha_vencimiento) ; datos.append(numero_cuenta) ; datos.append(saldo)
        hora_actual=str(datetime.now().time())
        print(f"\nBienvenido a tu banco de confianza, son las {hora_actual}\nLos datos de su cuenta bancaria son los siguientes: {datos}\n")
    crear_datos_cuentas()
    def ingresar_dinero():
        print("¿Cuánto dinero quiere ingresar a su cuenta?")
        saldo = datos.pop(5)
        print(f"Su saldo actual es de {saldo}€")
        saldo = float(saldo)
        dinero_añadir=float(input())
        dinero_total=saldo + dinero_añadir
        print(f"El saldo de su cuenta es {dinero_total} €")
    def retirar_dinero():
        saldo = datos.pop(5)
        saldo = float(saldo)
        dinero_retirar=float(input(f"Su saldo actual es de {saldo}\n¿Cuánto dinero desea retirar?\n"))
        if saldo - dinero_retirar < 0:
            print("\nOperación no válida, no tienes tanto capital")
        else:
            saldo_final = saldo - dinero_retirar
            print(f"Su saldo final es {saldo_final}")
    def trasferir_dinero():
        saldo = datos.pop(5)
        saldo = float(saldo)
        dinero_trasferir=float(input(f"Su saldo actual es de {saldo}\n¿Cuánto dinero desea trasferir?\n"))
        if saldo - dinero_trasferir < 0:
            print("\nOperación no válida, no tienes tanto capital")
        else:
            saldo_final = saldo - dinero_trasferir
            print(f"Su saldo final es {saldo_final} € y ha enviado a la cuenta de Rubén {dinero_trasferir} €")
    def retirar_dinero_fijo():
        print("Cómo el plazo fijo estaba vigente hasta el mes que viene, me temo que le cobraremos una comisión")
        saldo = datos.pop(5)
        saldo = float(saldo)
        dinero_retirar=float(input(f"Su saldo actual es de {saldo}\n¿Cuánto dinero desea retirar?\n"))
        if saldo - dinero_retirar < 0:
            print("\nOperación no válida, no tienes tanto capital")
        else:
            saldo_final = saldo - (dinero_retirar + saldo * 0.05)
            print(f"Su saldo final es {saldo_final}")
    def retirar_dinero_VIP():
        saldo = datos.pop(5)
        saldo = float(saldo)
        dinero_retirar=float(input(f"Su saldo actual es de {saldo}\n¿Cuánto dinero desea retirar?\n"))
        saldo_final = saldo - dinero_retirar
        print(f"Su saldo final es {saldo_final}")
    def trasferir_dinero_VIP():
        saldo = datos.pop(5)
        saldo = float(saldo)
        dinero_trasferir=float(input(f"Su saldo actual es de {saldo}\n¿Cuánto dinero desea trasferir?\n"))
        saldo_final = saldo - dinero_trasferir
        print(f"Su saldo final es {saldo_final} € y ha enviado a la cuenta de Rubén {dinero_trasferir} €")
    print("\nQué desea hacer con su cuenta bancaria\n --> 1: Cuenta corriente\n --> 2: Cuenta Plazo\n --> 3: Cuenta Vip")
    tipo_cuenta = int(input())
    if tipo_cuenta == 1:
        print("\nQué desea hacer con su cuenta bancaria\n --> 1: Ingresar Dinero\n --> 2: Retirar Dinero\n --> 3: Trasferir Dinero\n")
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
```
