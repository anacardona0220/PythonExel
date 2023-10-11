print("\nIngrese el tipo de vehiculo")
print("* Moto = 1 \n* Carro = 2 \n* Camioneta = 3")
tipo =int(input("Tipo de vehiculo: "))


tipos = {
    1: 'Moto',
    2: 'Carro',
    3: 'Camioneta'
}

def calcularPago(tipo):
    print(tipos[tipo])
    
calcularPago(tipos)