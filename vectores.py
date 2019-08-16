import math
import cairo
import os
import sys



def pedirVector():
    vector = [1,1,1]
    print("Introdzca vector")
    vector[0] = input("Inserte coordenada x: ")
    vector[1] = input("Inserte coordenada y: ")
    vector[2] = input("Inserte coordenada z: ")
    return vector

def pedirPunto():
    punto = [1,1,1]
    print("Introdzca punto")
    punto[0] = input("Inserte coordenada x: ")
    punto[1] = input("Inserte coordenada y: ")
    punto[2] = input("Inserte coordenada z: ")
    return punto

def crearVector(punto1, punto2):
    vector = [1,1,1]
    vector[0] = punto2[0] - punto1[0]
    vector[1] = punto2[1] - punto1[1]
    vector[2] = punto2[2] - punto1[2]
    return vector

def mostrarRecta(punto, vector):
    print("x = {} {} {} t".format(punto[0], asignarSigno(vector[0]), vector[0]))
    print("y = {} {} {} t".format(punto[1], asignarSigno(vector[1]), vector[1]))
    print("z = {} {} {} t".format(punto[2], asignarSigno(vector[2]), vector[2]))


def multiplicacionEscalar(vector1, vector2):
    return (vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2])


def multiplicacionVectorial(vector1, vector2):
    return (vector1[1] * vector2[2] - vector1[2] * vector2[1], vector1[2] * vector2[0] - vector1[0] * vector2[2], vector1[0] * vector2[1] - vector1[1] *vector2[0])

def vectorCubo(vector1, vector2, vector3):
    return vector1[0] * vector2[1] * vector3[2] + vector1[2] * vector2[0] * vector3[1] + vector1[1] * vector2[2] * vector3[0] - vector1[2] * vector2[1] * vector3[0] - vector1[0] * vector2[2] * vector3[1] - vector1[1] * vector2[0] *vector3[2]

def magnitud(vector):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)

def asignarSigno(valor):
    if valor >= 0:
        return "+"
    else:
        return ""

def construccionVector(punto1, punto2):
    vector = [1,1,1]
    vector[0] = punto2[0] - punto1[0]
    vector[1] = punto2[1] - punto1[1]
    vector[2] = punto2[2] - punto1[2]
    print(vector)
    return vector

def menuv():

    os.system('clear')
    print ("Selecciona una opcion")
    print ("\t1 - Magnitud")
    print ("\t2 - Vector unitario")
    print ("\t9 - salir")

def vectorO(vector):

    while True:

        menuv()
        vector2 = [1,1,1]
        opcionMenu = str(raw_input("inserta un numero valor >> "))
        print(opcionMenu)
        if opcionMenu== "1":
            escalar = magnitud(vector)
            print("la magnitud de {} es:".format(vector))
            print(escalar)
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu== "2":
            escalar = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
            vector2[0] = vector[0] / escalar
            vector2[1] = vector[1] / escalar
            vector2[2] = vector[2] / escalar
            print(vector2)
            opcionMenu = str(raw_input("Pulse una tecla"))

        elif opcionMenu == "9":
            print ("")
            break
        else:
            print("opcion incorrecta")

def menuvye():

    os.system('clear')
    print ("Selecciona una opcion")
    print ("\t1 - producto escalar")
    print ("\t9 - salir")

def vectoryescalar():

    while True:

        menuvye()
        opcionMenu = str(raw_input("inserta un numero valor >> "))
        print(opcionMenu)
        if opcionMenu== "1":
            vector2 = [1,1,1]
            vector2[0] = vector[0] * escalar
            vector2[1] = vector[1] * escalar
            vector2[2] = vector[2] * escalar
            print(vector2)
            print ("")
            break
        elif opcionMenu == "9":
            print ("")
            break
        else:
            print("opcion incorrecta")

def menuvyv():

    os.system('clear')
    print (vector1)
    print(vector2)
    print ("Selecciona una opcion")
    print ("\t1 - Suma")
    print ("\t2 - Resta")
    print ("\t3 - Multiplicacion escalar")
    print ("\t4 - Multiplicacion vectorial")
    print ("\t5 - Dependencia lineal")
    print ("\t6 - Angulo entre ellos")
    print ("\t7 - Proyeccion de vector 1 sobre vector 2")
    print ("\t9 - salir")


def vectoryvector():

    while True:

        menuvyv()
        vector3 = [1,1,1]
        esclar = 1
        opcionMenu = str(raw_input("inserta un numero valor >> "))
        print(opcionMenu)
        if opcionMenu== "1":
            vector3[0] = vector1[0] + vector2[0]
            vector3[1] = vector1[1] + vector2[1]
            vector3[2] = vector1[2] + vector2[2]
            print(vector3)
            opcionMenu = str(raw_input("Para operaciones con este vector pulse 1, para regresar pulse 0>> "))
            if opcionMenu == "1" :
                vectorO(vector3)
            else:
                opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu== "2":
            vector3[0] = vector1[0] - vector2[0]
            vector3[1] = vector1[1] - vector2[1]
            vector3[2] = vector1[2] - vector2[2]
            print(vector3)
            opcionMenu = str(raw_input("Para operaciones con este vector pulse 1, para regresar pulse 0>>"))
            if opcionMenu == "1" :
                vectorO(vector3)
            else:
                opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu== "3":
            escalar = multiplicacionEscalar(vector1,vector2)
            print(escalar)
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu== "4":
            vector3 = multiplicacionVectorial(vector1,vector2)
            print(vector3)
            opcionMenu = str(raw_input("Para operaciones con este vector pulse 1, para regresar pulse 0>> "))
            if opcionMenu == "1" :
                vectorO(vector3)
            else:
                opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu== "5":
            alfa = vector2[0]/vector1[0]
            if (vector1[1] * alfa == vector2[1] and vector1[2] * alfa == vector2[2]):
                print("son linealmente dependientes a razon de ")
                print(alfa)
            else:
                print("no son linealmente dependientes")
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu == "6":
            productoPunto = multiplicacionEscalar(vector1,vector2)
            productoMagnitud = magnitud(vector1) * magnitud(vector2)
            o = math.acos(productoPunto/productoMagnitud)
            print(o)
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu == "7":
            vProy = [1,1,1]
            productoEscalar = multiplicacionEscalar(vector1,vector2)
            moduloC = magnitud(vector2) ** 2
            operacion = productoEscalar/moduloC
            vProy[0] = round(vector2[0] * operacion, 2)
            vProy[1] = round(vector2[1] * operacion, 2)
            vProy[2] = round(vector2[2] * operacion, 2)
            print(vProy)
            opcionMenu = str(raw_input("Para operaciones con este vector pulse 1, para regresar pulse 0>>"))
            if opcionMenu == "1" :
                vectorO(vector2)
            else:
                opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu == "9":
            print ("")
            break
        else:
            print("opcion incorrecta")

def menuOpPlanos():
    print ("Selecciona una opcion")
    print ("\t1 - Comprobar si punto pertenece al plano")
    print ("\t2 - Distancia del punto al plano")
    print ("\t9 - salir")

def opPlanos(punto, vector):
    while True:
        os.system('clear')
        print("{}x {} {}y {} {}z = {}".format(vector[0], asignarSigno(vector[1]) ,vector[1],asignarSigno(vector[2]) ,vector[2], vector[0] * punto[0] + vector[1] * punto[1] + vector[2] * punto[2]) )
        menuOpPlanos()
        opcionMenu = str(raw_input("inserta un numero valor >> "))
        print(opcionMenu)
        if opcionMenu== "1":
            print("Punto a comprobar")
            puntoP = pedirPunto()
            r = vector[0] * puntoP[0] + vector[1] * puntoP[1] + vector[2] * punto[2]
            if (r ==  vector[0] * punto[0] + vector[1] * punto[1] + vector[2] * punto[2]):
                print ("Si pretenece al plano")
            else:
                print ("No pertenece al plano")
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu== "2":
            print("Punto a comprobar")
            puntoP = pedirPunto()
            d = 1
            d = (vector[0] * puntoP[0]) + (vector[1] * puntoP[1]) + (vector[2] * punto[2])
            d = vector[0] * puntoP[0]
            d += vector[2] * puntoP[2]
            d += vector[1] * puntoP[1]
            d = d - (vector[0] * punto[0] + vector[1] * punto[1] + vector[2] * punto[2])
            print(d/math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2))
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu == "9":
            print ("")
            break
        else:
            print("opcion incorrecta")


def menuplanos():

    os.system('clear')
    print ("Selecciona una opcion")
    print ("\t1 - Comprobar si 3 puntos son coplanares")
    print ("\t2 - Comprobar si 3 vectores son coplanares")
    print ("\t3 - Plano dado vector normal y punto")
    print ("\t4 - Plano dado 3 puntos")
    print ("\t5 - Operaciones dado un plano (vector y punto)")
    print ("\t9 - salir")


def planos():

    while True:

        menuplanos()

        opcionMenu = str(raw_input("inserta un numero valor >> "))
        print(opcionMenu)
        if opcionMenu== "1":
            punto1 = pedirPunto()
            punto2 = pedirPunto()
            punto3 = pedirPunto()
            vector1 = crearVector(punto1,punto2)
            vector2 = crearVector(punto1,punto3)
            vector3 = crearVector(punto2,punto3)
            multVectorial = vector1[0] * vector2[1] * vector3[2] + vector1[2] * vector2[0] * vector3[1] + vector1[1] * vector2[2] * vector3[0] - vector1[2] * vector2[1] * vector3[0] - vector1[0] * vector2[2] * vector3[1] - vector1[1] * vector2[0] *vector3[2]
            if multVectorial == 0:
                print("Pertenecen al mismo plano")
            else:
                print("No pertenecen al mismo plano")
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu== "2":
            vectorN = [1,1,1]
            vector1 = pedirVector()
            vector2 = pedirVector()
            vector3 = pedirVector()
            multVectorial = vector1[0] * vector2[1] * vector3[2] + vector1[2] * vector2[0] * vector3[1] + vector1[1] * vector2[2] * vector3[0] - vector1[2] * vector2[1] * vector3[0] - vector1[0] * vector2[2] * vector3[1] - vector1[1] * vector2[0] *vector3[2]
            if multVectorial == 0:
                print("Pertenecen al mismo plano")
            else:
                print("No pertenecen al mismo plano")
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu == "3":
            punto = pedirPunto()
            vector = pedirVector()
            print("{}x {} {}y {} {}z = {}".format(vector[0], asignarSigno(vector[1]) ,vector[1],asignarSigno(vector[2]) ,vector[2], vector[0] * punto[0] + vector[1] * punto[1] + vector[2] * punto[2]) )
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu == "4":
            print("Punto 1")
            p1 = pedirPunto()
            p2 = pedirPunto()
            p3 = pedirPunto()
            a1 = p2[0] - p1[0]
            b1 = p2[1] - p1[1]
            c1 = p2[2] - p1[2]
            a2 = p3[0] - p1[0]
            b2 = p3[1] - p1[1]
            c2 = p3[2] - p1[2]
            a = b1 * c2 - b2 * c1
            b = a2 * c1 - a1 * c2
            c = a1 * b2 - b1 * a2
            d = (- a * p1[0] - b * p1[1] - c * p1[2])
            print ("Ecuacion del plano es ")
            print a, "x +",
            print b, "y +",
            print c, "z +",
            print d, "= 0."
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu == "5":
            punto = pedirPunto()
            vector = pedirVector()
            opPlanos(punto, vector)
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu == "9":
            print ("")
            break
        else:
            print("opcion incorrecta")


def menu2rectas(punto1, vector1, punto2, vector2):
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    print("recta 1")
    mostrarRecta(punto1,vector1)
    print("recta 2")
    mostrarRecta(punto2,vector2)
    print ("Selecciona una opcion")
    print ("\t1 - Angulo entre recta 1 y recta 2")
    print ("\t2 - Posicion relativa")
    print ("\t3 - Distancia entre recta 1 y recta 2")
    print ("\t9 - Salir")

def rectayrecta(punto1, vector1, punto2, vector2):
    while True:

        menu2rectas(punto1, vector1, punto2, vector2)
        opcionMenu = str(raw_input("inserta un numero valor >> "))
        print(opcionMenu)
        if opcionMenu== "1":
            o = 1
            vector3 = [1,1,1]
            magV3 = multiplicacionEscalar(vector1,vector2)
            magV1 = magnitud(vector1)
            magV2 = magnitud(vector2)
            o = math.acos(magV3/(magV1 * magV2))
            print("El angulo es {}".format(o))
            opcionMenu = str(raw_input("Pulse una tecla"))

        elif opcionMenu== "2":
            if (vector1 == vector2):
                "Son paralelas"
            else:
                print"Se cortan o se cruzan"
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu== "3":
            puntoR = [1,1,1]
            puntoR[0] = punto1[0] * punto2[0]
            puntoR[1] = punto1[1] * punto2[1]
            puntoR[2] = punto1[2] * punto2[2]
            d = (vectorCubo(vector1, vector2, puntoR)) / magnitud(multiplicacionVectorial(vector1,vector2))
            print"La distancia entre ambas rectas es de unidades "
            print(d)
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu == "9":
            print ("")
            break
        else:
            print("opcion incorrecta")

def menuRectas():

    os.system('clear')
    print ("Selecciona una opcion")
    print ("\t1 - Ecuacion en forma parametrica")
    print ("\t2 - Operaciones entre dos rectas")
    print ("\t3 - Distancia de un punto a una recta")
    print ("\t9 - salir")

def rectas():

    while True:
        menuRectas()
        opcionMenu = str(raw_input("inserta un numero valor >> "))
        print(opcionMenu)
        if opcionMenu== "1":
            opcionMenu = str(raw_input("1 para vector y punto o 2 para punto y punto"))
            if opcionMenu == "1":
                punto = pedirPunto()
                vector = pedirVector()
            else:
                punto = pedirPunto()
                punto1 = pedirPunto()
                vector = construccionVector(punto, punto1)
            print("recta en su forma parametrica")
            mostrarRecta(punto,vector)
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu== "2":
            print("datos recta 1")
            punto1 = pedirPunto()
            vector1 = pedirVector()
            print("datos recta 2")
            punto2 = pedirPunto()
            vector2 = pedirVector()
            rectayrecta(punto1, vector1, punto2, vector2)
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu== "3":
            print("Construccion de la recta...")
            punto = [1,1,1]
            opcionMenu = str(raw_input("1 para vector y punto o 2 para punto y punto"))
            if opcionMenu == "1":
                punto = pedirPunto()
                vector = pedirVector()
            else:
                punto = pedirPunto()
                punto1 = pedirPunto()
                vector = construccionVector(punto, punto1)
            print("Ingrese el punto al sacar la distancia")
            puntoP = pedirPunto()
            vectorP = crearVector(punto,puntoP)
            d = (magnitud(multiplicacionVectorial(vector, vectorP)) / (magnitud(vector)))
            print("La distancia entre la recta:")
            print(mostrarRecta(punto,vector));
            print("Y el punto {} es: {}".format(puntoP, d))
            opcionMenu = str(raw_input("Pulse una tecla"))
        elif opcionMenu == "9":
            print ("")
            break
        else:
            print("opcion incorrecta")


def menu():
    """
    Funcion que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('clear')
    print ("Selecciona una opcion")
    print ("\t1 - Calculo con un vector y un escalar")
    print ("\t2 - Calculo con dos vectores")
    print ("\t3 - Calculos con un vector")
    print ("\t4 - Construccion de un vector")
    print ("\t5 - Planos")
    print ("\t6 - Rectas")
    print ("\t9 - salir")




while True:
    # Mostramos el menu
    menu()

    # solicituamos una opcion al usuario
    opcionMenu = str(raw_input("inserta un numero valor >> "))

    print(opcionMenu)

    if opcionMenu== "1":
        vector = [1,1,1]
        escalar = 2
        print("Calculo con un vector y un ecalar...")
        vector = pedirVector()
        print(vector)
        escalar = input("Inserte escalar: ")
        vectoryescalar()
        opcionMenu = str(raw_input("Pulse una tecla"))

    elif opcionMenu== "2":
        print("Calculo con dos vectores...")
        vector1 = [1,1,1]
        vector2 = [1,1,1]
        print("vector 1")
        vector1 = pedirVector()
        print(vector1)
        print("vector 2")
        vector2 = pedirVector()
        print(vector2)
        vectoryvector()

    elif opcionMenu== "3":
        print("Calculo con un vector..")
        vector = [1,1,1]
        vector = pedirVector()
        print(vector)
        vectorO(vector)

    elif opcionMenu== "5":
        print("Planos..")
        planos()

    elif opcionMenu == "4":
        print("Contruccion de un vector con dos puntos...")
        print("Punto 1")
        punto1 = pedirPunto()
        print("punto2")
        punto2 = pedirPunto()
        print("El vector resultante es:")
        print(construccionVector(punto1, punto2))
        opcionMenu = str(raw_input("Pulse 1 si quiere realizar una operacion con este vector"))
        if opcionMenu == "1" :
            vectorO(construccionVector(punto1, punto2))
        else:
            opcionMenu = str(raw_input("Pulse una tecla"))

    elif opcionMenu== "6":
        print("Planos..")
        rectas()
    else:
        print ("")
        break
