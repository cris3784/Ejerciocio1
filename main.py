print("Bienvenido, en este programa podra saber si aprobo o reprobo un estudiante")

opc1="si" #Añadimos una variable para controlar el ciclo del programa, esta variable se inicializa con "si" para que el programa se ejecute al menos una vez

while opc1 == "si": #Añadimos un ciclo para que el programa se repita hasta que el usuario decida no ingresar mas estudiantes

    nom1=input("Ingrese el nombre del estudiante: ")

    sum1=0 #Añadimos una variable para sumar las notas del estudiante y asi poder calcular el promedio al final del ciclo

    for i in range(5): #Añadimos un ciclo para que el usuario ingrese las notas del estudiante

        not1=input("Ingrese una nota: ")

        for let1 in not1:

            while let1 not in "0123456789.": #Añadimos validacion para que no se ingresen letras
                print("No se permiten letras")
                not1=input("Ingrese nuevamente la nota: ")
                let1=not1

        not1=float(not1) #Convertimos la nota a un numero decimal para poder realizar operaciones matematicas con ella

        while not1 < 1.0 or not1 > 5.0: #Añadimos validacion para que no se ingresen notas menores a 1.0 o mayores a 5.0
            print("Nota no válida")
            not1=float(input("Ingrese nuevamente la nota: "))

        sum1=sum1+not1 #Sumamos las notas para saber el total de las notas del estudiante

    prom1=sum1/5 #Calculamos el promedio del estudiante

    print("Estudiante:", nom1)
    print("Promedio final:", prom1)

    if prom1>=3.5: #Añadimos una condicion para saber si el estudiante aprobo o reprobo, en este caso se considera que un estudiante aprueba si su promedio es mayor o igual a 3.5
        print("Aprobó")

    else:
        print("Reprobado")

    opc1=input("¿Quiere ingresar las notas de otro estudiante? Ingrese 'si' o 'no': ") #Al final del ciclo preguntamos al usuario si desea ingresar las notas de otro estudiante, si el usuario ingresa "si" el ciclo se repetira, de lo contrario el programa terminara

