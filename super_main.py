'''
Un supermercado maneja el catálogo de los productos que vende. De cada producto se conoce su nombre, precio, y si el mismo es parte del programa Precios Cuidados o no. Por defecto, el producto no es parte del programa, a menos que se especifique lo contrario.

Para ayudar a los clientes, el supermercado quiere realizar descuentos en productos de Primera Necesidad. Es por eso que al calcular el precio de un producto de Primera Necesidad, se aplica un descuento del 10%. Es decir:

    precioProductoPrimeraNecesidad = precioBaseDelProducto * 0.9

El supermercado, del cual se conoce el nombre y la dirección, desea conocer la cantidad total de productos que comercializa y la suma total de los precios de los mismos.
Implementar un programa en Python que resuelva este requerimiento.

Suponga ahora que el descuento a aplicar en cada producto de primera necesidad puede ser distinto y se debe poder definir al momento de crear el mismo. Por ejemplo, el arroz puede ser un producto de primera necesidad con un descuento del 8%, mientras que leche podría ser otro producto de primera necesidad con un decuento del 11%. Esto es sólo un ejemplo. El descuento a aplicar en cada producto de primera necesidad debe ser configurable al momento de crearlo.

Implementar un programa en Python basado en el anterior que ahora incorpore este nuevo requerimiento.
'''
class Supermercado:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

class Producto:
    def __init__(self, nombre, precio, descuento, ppc = False):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento
        self.ppc = ppc

    def precio_final(self):
        if self.ppc == True:
            self.precio = self.precio - (self.precio*self.descuento/100)
        return self.precio

def calcular_precio(list):
    precio_total = 0.0
    for x in list:
        precio_total += x.precio_final()
    return precio_total

el_chino = Supermercado("EL Chino", "Avenida X Nº 200")

arroz = Producto("La Arrocera", 30, 10, ppc = True)
fideo = Producto("Fidelin", 25, 8, ppc = True)
galletitas = Producto("Oreo", 15, 2, ppc = False)
arvejas = Producto("Bolas Verdes", 10, 15, ppc = False)
atun = Producto("Atulin", 17, 20, ppc = True)
pan = Producto("Panuca", 7.5, 13, ppc = True)
carne = Producto("El Lomo", 40, 6, ppc = True)
desodorante = Producto("Avon", 8, 30, ppc = False)
talco = Producto("Talco", 5, 10, ppc = False)

productos = [arroz, fideo, galletitas, arvejas, atun, pan, carne, desodorante, talco]

print(f"Bienvenido al Supermercado {el_chino.nombre}")
print(f"Tenemos un total de {len(productos)}")
print(f"La suma del precio total de los productos es {calcular_precio(productos)}")
