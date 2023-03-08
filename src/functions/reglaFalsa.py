import random as rnd


# Función ecuación.
def eq(xI):
    return (2 * xI**3) - 11


# Función de definición de pares de números aleatorios dentro de un rango especifico
def rndNumbers():
    xLow = rnd.randint(-1000, 1000)
    while eq(xLow) > 0:
        xLow = rnd.randint(-1000, 1000)

    xHigh = rnd.randint(xLow, 1000)
    while eq(xHigh) < 0:
        xHigh = rnd.randint(xLow, 1000)

    print(f"* El rango de búsqueda es de {xLow} a {xHigh} ")
    return xLow, xHigh


counter = 0
xLow, xHigh = rndNumbers()
while True:
    counter += 1
    xMiddle = xLow - (eq(xLow) * (xHigh - xLow) / (eq(xHigh) - eq(xLow)))

    if eq(xMiddle) > 0:
        xHigh = xMiddle
    else:
        xLow = xMiddle

    if abs(eq(xMiddle)) <= 0.001:
        print(
            f"La respuesta es {round(xMiddle, 2)} y el numero de iteraciones fue {counter}"
        )
        break
