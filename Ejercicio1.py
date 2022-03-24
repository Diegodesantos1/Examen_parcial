
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