# Programa para calcular el promedio semanal del clima

def ingresar_temperaturas():
    temperaturas = []

    for i in range(7):
        temp = float(input("Ingrese la temperatura del día: "))
        temperaturas.append(temp)

    return temperaturas


def calcular_promedio(temperaturas):
    suma = 0

    for temp in temperaturas:
        suma = suma + temp

    promedio = suma / len(temperaturas)
    return promedio


# Programa principal
temps = ingresar_temperaturas()
promedio_semanal = calcular_promedio(temps)

print("El promedio semanal del clima es:", promedio_semanal)
