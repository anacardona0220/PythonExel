

class Vehiculo:
    placa: str = ''
    tipo: str = ''
    hora: int = 0
    minuto: int = 0
    valorPagar: float = 0

    def __init__(self, placa, tipo, hora, minuto, valoPagar) -> None:
        self.placa = placa
        self.tipo = tipo
        self.hora = hora
        self.minuto = minuto
        self.valorPagar = valoPagar

    def calcularPago(self):
        valor_minuto = 0
        if self.tipo == 'Moto':
            valor_minuto = 90
        elif self.tipo == 'Carro':
            valor_minuto = 110
        else:
            valor_minuto = 130

        tiempo = self.hora * 60 * valor_minuto + self.minuto * valor_minuto
        self.valorPagar = tiempo
        
         

    def __str__(self) -> str:
        return ("PLaca : {}\nTipo : {}\nValor a pagar : {}". format(self.placa, self.tipo, self.valorPagar))


class Parqueadero:
    def __init__(self) -> None:
        while True:
            print("Ingrese el tipo de vehiculo")
            print("Moto = 1 \nCarro = 2 \nCamioneta = 3")
            tipoIn = input("tipo : ")

            tipos = {
                '1': 'Moto',
                '2': 'Carro',
                '3': 'Camioneta'
            }
            
            tipo = tipos[tipoIn]

            placa = input("Ingresa la placa :")
            hora = int(input("Ingrese las horas del vehiculo :"))
            minuto = int(input("Ingrese los minutos del vehiculo :"))

            vehiculo = Vehiculo(placa, tipo, hora, minuto, 0)
            vehiculo.calcularPago()
            print(vehiculo)

            otro_vehiculo = int(
                input("Desea ingresar otro vehiculo? SI: 1 | NO: 2"))
            if otro_vehiculo == 2:
                break


Parqueadero()