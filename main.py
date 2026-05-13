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