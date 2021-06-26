def areatriangulo(base,altura):
    return base*altura/2
def areacuadrado(lado):
    return lado*lado
def areacirculo(r):
    return 3.1416 * r ** 2
def edad(año):
    return 2021-año
def menu():
    print("***********************")
    print("*        MENU         *")
    print("*1. Area del triángulo*")
    print("*2. Area del cuadrado *")
    print("*3. Area del círculo  *")
    print("*4. Que edad tengo    *")
    print("*5.      Salir        *")
    print("***********************")
    opcion = int(input("Escoja la opcion: "))
    return opcion

opcion = menu()
while opcion != 5:
    if opcion == 1:
        print("Calculo del area de un Triangulo")
        base = int(input("ingrese la base: " ) )
        altura = int(input("ingrese la altura: "))
        calculo = areatriangulo(base,altura)
        print("Area del triangulo: " + str(calculo) + "\n")
    elif opcion == 2:
        print("Calculo del area de un Cuadrado")
        lado = int(input("ingrese uno de los Lados: " ) )
        CalculoC = areacuadrado(lado)
        print("Area del Cuadrado es: " + str(CalculoC) + "\n")
    elif opcion == 3:
        print("Calculo del area de un Circulo")
        r = int(input("ingrese el diametro: " ) )
        areaC =areacirculo(r)
        print("Area del Circulo: " + str(areaC) + "\n")
    elif opcion == 4:
        print("Adivinar edad")
        año = int(input("ingrese su año de Nacimiento " ) )
        edad2 =edad(año)
        print("Su edad es " + str(edad2) + "\n")
    else:
        print("Opcion no valida\n")
    opcion = menu()

