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
