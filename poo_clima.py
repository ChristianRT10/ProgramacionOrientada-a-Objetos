# Programa para calcular el promedio semanal del clima

class Clima:
    def __init__(self):
        # Lista privada para guardar temperaturas
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input("Ingrese la temperatura del día: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        suma = 0

        for temp in self.temperaturas:
            suma = suma + temp

        promedio = suma / len(self.temperaturas)
        return promedio


# Programa principal
clima = Clima()
clima.ingresar_temperaturas()
promedio_semanal = clima.calcular_promedio()

print("El promedio semanal del clima es:", promedio_semanal)
