class Cuenta_Bancaria:
    def __init__(self, ID, nombre_titular,fecha_apertura, numero_cuenta, saldo):
        self.ID=ID
        self.nombre_titular=nombre_titular
        self.fecha_apertura=fecha_apertura
        self.numero_cuenta=numero_cuenta
        self.saldo=saldo
    def crear_cuenta(self):
        txt= "{0},{1},{2},{3},{4}"
        return txt.format(self.ID, self.nombre_titular,self.fecha_apertura, self.numero_cuenta, self.saldo)
A=Cuenta_Bancaria("ID1234","Diego de Santos", "10/05/2022", "ES12345678", "300€")
print(A.crear_cuenta())