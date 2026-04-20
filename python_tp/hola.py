def eje1():
    n1 = int(input("ingrese un numero: "))
    n2 = int(input("ingrese un segundo numero: "))
    r = n1 + n2
    print("el resultado es: ", r)
#eje1()

def eje2():
    n1 = int(input("ingrese un numero: "))
    n2 = int(input("ingrese un segundo numero: "))
    n3 = int(input("ingrese un tercer numero: "))
    n4 = int(input("ingrese un cuarto numero: "))
    r = n1 + n2 + n3 + n4
    print("el resultado es: ", r)
#eje2()

def eje3():
    n1 = int(input("ingrese un num: "))
    n2 = int(input("ingrese otro: "))
    r = n1 * n2
    print("la superficie es: ", r)
#eje3()

def eje4():
    n = float(input("ingrese un número con decimales: "))
    A = n * n
    print("el Area del cuadrado es: ", A)
#eje4()

def eje5():
    s = int(input("ingrese una cantidad de segundos: "))
    m = int(input("ingrese una cantidad de minutos: "))
    h = int(input("ingrese una cantidad de horas: "))
    hs = h * 3600
    ms = m * 60
    R = hs + ms + s
    print("hay un total de ", R, " segundos")
#eje5()

def eje6():
    n1 = int(input("ingresar base: "))
    n2 = int(input("ingresar altura: "))
    R = (n1 * n2) / 2
    print("La superficie es: ", R)
#eje6()

def eje7():
    n1 = int(input("ingrese el primer número: "))
    n2 = int(input("ingrese el segundo número: "))
    n3 = int(input("ingrese el tercer número: "))
    n4 = int(input("ingrese el cuarto número: "))
    n5 = int(input("ingrese el quinto número: "))
    n6 = int(input("ingrese el sexto número: "))
    R = (n1 + n2 + n3 + n4 + n5 + n6) / 6
    print("El promedio es de: ", R)
#eje7()

def eje8():
    n1 = int(input("ingrese un número base: "))
    n2 = int(input("ingrese el número a calcular: "))
    R = (n1/n2)*100
    print("El resultado es: ", R, "%")
#eje8()


def eje9():
    F = int(input("ingrese una fecha: "))
    A = F % 10000
    M = (F // 10000) % 100
    MD = (F // 1000000) % 100
    D = F // 1000000
    print("el año es: ", A)
    print("el mes es: ", M)
    print("el día es: ", D)
#eje9()

def eje10():
    EX = int(input("Ingresa nota de los examenes principales: "))
    TPS = int(input("ingresa nota de los trabajos practicos: "))
    EXI = int(input("ingresa nota de los examenes integradores: "))
    r1 = EXI * 0.5
    r2 = TPS * 0.2
    r3 = EX * 0.3
    RE = r1 + r2 + r3
    print("el rendimiento es de: ",RE)
#eje10()

def eje11():
    SM = 5500
    CV = 200
    VA = 0.05
    NV = int(input("ingrese el numero de autos vendidos: "))
    VV = int(input("ingrese el valor de venta de la unidad: "))
    R = SM + (CV * NV) + (VA * VV * NV)
    print("el salario total del vendedor es: ", R)   
#eje11()