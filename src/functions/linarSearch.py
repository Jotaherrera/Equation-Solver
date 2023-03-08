import random as rnd

xI = rnd.randint(-1000, 1000)


def eq(xI):
    return (2 * xI**3) - 11


if eq(xI) == 0:
    print(
        f"» La X de la ecuación corresponde a {round(xI, 2)} y el número de iteraciones fue 1"
    )

else:
    count = 0
    while True:
        if eq(xI) > 0:
            count += 1
            x1 = xI - 0.001
            xI = x1
            if eq(xI) <= 0.001:
                print(
                    f"» La X de la ecuación corresponde a {round(xI, 2)} y el número de iteraciones fue {count}"
                )
                break
        else:
            count += 1
            x1 = xI + 0.001
            xI = x1
            if eq(xI) >= 0.001:
                print(
                    f"» La X de la ecuación corresponde a {round(xI, 2)} y el número de iteraciones fue {count}"
                )
                break
