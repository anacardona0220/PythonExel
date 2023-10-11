class Book:
    # method 'Constructor, _ protegido |  __ para dejarlo privado'
    def __init__(self, title, author, price, stock, id):
        self._title = title
        self._author = author
        self._price = price
        self._stock = stock
        self._id = id

    def getInfo(self):
        return f"Titulo : {self._title} \nAutor  : {self._author} \nPrecio : {self._price} \nStock : {self._stock} \nIdentificacion : {self._id}"


# ------------------- Metodos getter Obtener (Lectura) -----------------

    def get_title(self):
     return self._title
 
    def get_price(self):
     return self._price

     

# ---------- Metodos setter setear/establecer (Escritura) -----------------

    def set_title(self, new_title):
     self._title = new_title
     
    def set_price(self, new_price):
        if new_price > 0:
          self._price = new_price
        
        else:
          print('\nEl precio no puede ser Cero!\n')



# ----------------- Para herencia ----------------------
class Comic(Book):
    def __init__(self, title, author, price, stock, id, ilustrators, vol):
        super().__init__(title, author, price, stock, id )
        self._ilustrators = ilustrators
        self._vol = vol
        
    def getInfo(self):
       info = super().getInfo()
       return info + f"""\nIlustradores : { self._ilustrators}\nVolumen :{self._vol} """



book1 = Book('Biblia', 'Dios', 20000, 100, 111)

comic = Comic('Leyendas de la Biblia', 'Carlos', 1000, 50, 50, 'Norma', 3 )


# --------------------------- Herencia -----------------------------------
print('')
print(book1.getInfo())
print('\n--- get title :')
print(book1.get_title()) 

print('\nModificar title :')
book1.set_title('La biblia')
book1.set_price(0)
print(book1.getInfo())

# --------------------------- Herencia -----------------------------------

print('')
print(comic.getInfo())
