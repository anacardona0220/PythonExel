# Definir una clase
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def size(self):
        return self.__width * self.__height

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value

# Crear una instancia de la clase
rectangle = Rectangle(5, 10)

# Obtener el valor de la propiedad "size"
print(rectangle.size)  # Salida: 50

# Establecer el valor de la propiedad "size"
rectangle.size = 20

# Obtener el valor actualizado de la propiedad "size"
print(rectangle.size)  # Salida: 400
