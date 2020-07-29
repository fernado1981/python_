from POO.Calculo.calculo import calculo


class aritmetica:
    numA = int(input("introduce altura: "))
    numB = int(input("introduce anchura: "))

    calc = calculo(numA, numB)
    area = calc.areaRectangulo()
    print("el area es :", area)
    calc.perimetroRectangulo()

    calc.mayorque()

