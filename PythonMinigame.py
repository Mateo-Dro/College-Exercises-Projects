#Mateo Diaz DNI: 44762094
#La finalidad de este programa es presentar un circuito de desafíos matemáticos, las operaciones son predeterminadas pero el orden de su realización es aleatorio. 
#Y los valores que se usan dentro de cada operación también lo son (a excepción de un solo desafío). 
#Se usa el módulo random para shuffle y randint. Y del módulo math se utiliza la función factorial, y técnicamente pow pero este es parte de la biblioteca estandar. 
#El usuario tiene 3 intentos para terminar el circuito, y los va perdiendo a medida que falla los desafíos. Para ganar necesita tener más del 80% de los desafíos completados, sino pierde. 
#Se utiliza un bucle while para ir moviéndome entre cada índice de la tupla randomizada (el cuál originalmente era una lista pero expliqué porqué lo pasé a tupla). Y se utiliza el match
#case (switch) para moverse entre todas las posibilidades que hay. Se podría utilizar elif pero el switch es más fácil de leer. 
#Hay un menu básico para permitir reintentar el circuito. En el final, si el usuario supera con éxito el circuito, se muestran los desafíos que completó y qué operaciones eran, utilizando
#el método de burbuja en una función llamada ordenar. 

#MODULOS
from math import factorial #Para operaciones más avanzadas como factorial, potenciación, etc.
from random import randint, shuffle #Para el shuffle de los retos, y para randomizar los valores dentro de cada reto.

#CIRCUITO DE DESAFIOS
def desafios():
    retos = ["Reto 1 | Suma", "Reto 2 | Resta", "Reto 3 | Producto", "Reto 4 | Pi", "Reto 5 | Cuadrado", "Reto 6 | Cubo", "Reto 7 | Ecuacion", "Reto 8 | Factorial"] #Originalmente no iban a tener estos nombres, pero son necesarios para demostrar la función de ordenar.
    shuffle(retos) #Todos los intentos tendrán un orden distinto de operaciones
    return tuple(retos) #Paso a tupla porque los datos son inmutables, y es una estructura de datos más rápida. Es innecesario pero lo hago por buena práctica.

#ORDENAR LOS DESAFIOS SUPERADOS
def ordenar(superados):
    for i in range(len(superados)):
        for j in range(len(superados) - i - 1):
            if (superados[j] > superados[j + 1]):
                aux = superados[j]
                superados[j] = superados[j + 1]
                superados[j + 1] = aux
    return superados #Esto originalmente lo hacía con el sorted pero lo agrego para estar en el mismo tono que la cursada
#Esta función será llamada dentro de la función juego

#JUEGO PRINCIPAL 
def juego(retos):
    superados = [] #Inicializo lista de los retos que serán superados
    continues = 3 #Los intentos
    pos = 0 #Con esto se guiará el match case (switch)
    print("\nBienvenido al juego.")
    print(f"Tiene un total de {continues} intentos.")
    input("Ingrese cualquier cosa para comenzar: ")
    while (continues != 0) and (pos < 8):
        print(f"\nQuedan {continues} intentos.")
        match retos[pos]:
            case "Reto 1 | Suma": #Suma
                n1 = randint(1, 100)
                n2 = randint(1, 100)
                respuesta = int(input(f"Ingrese el resultado de: {n1} + {n2}: "))
                if (respuesta != n1 + n2):
                    print("Respuesta incorrecta.")
                    continues-=1
                    pos+=1
                else:
                    print("¡Respuestas correcta!")
                    superados.append(retos[pos])
                    pos+=1
            case "Reto 2 | Resta": #Resta
                n1 = randint(500, 1000)
                n2 = randint(300, 1000)
                respuesta = int(input(f"Ingrese el resultado de: {n1} - {n2}: "))
                if (respuesta != n1 - n2):
                    print("Respuesta incorrecta.") 
                    continues-=1
                    pos+=1
                else:
                    print("¡Respuesta correcta!")
                    superados.append(retos[pos])
                    pos+=1
            case "Reto 3 | Producto": #Producto
                n1 = randint(0, 100)
                n2 = randint(0, 100)
                respuesta = int(input(f"Ingrese el resultado de: {n1} * {n2}: "))
                if (respuesta != n1*n2):
                    print("Respuesta incorrecta.")
                    continues-=1
                    pos+=1
                else:
                    print("¡Respuesta correcta!")
                    superados.append(retos[pos])
                    pos+=1
            case "Reto 4 | Pi": #Digitos de Pi
                respuesta = input("Ingrese los primeros 15 dígitos de pi: ")
                if (respuesta != "141592653589793"):
                    print("Respuesta incorrecta.")
                    continues-=1
                    pos+=1
                else:
                    print("¡Respuesta correcta!")
                    superados.append(retos[pos])
                    pos+=1
            case "Reto 5 | Cuadrado": #Cuadrado
                n1 = randint(1, 100)
                respuesta = int(input(f"Ingrese el cuadrado de {n1}: "))
                if (respuesta != pow(n1, 2)):
                    print("Respuesta incorrecta.")
                    continues-=1
                    pos+=1
                else:
                    print("¡Respuesta correcta!")
                    superados.append(retos[pos])
                    pos+=1
            case "Reto 6 | Cubo": #Cubo
                n1 = randint(1, 100)
                respuesta = int(input(f"Ingrese el cubo de {n1}: "))
                if (respuesta != pow(n1, 3)):
                    print("Respuesta incorrecta.")
                    continues-=1
                    pos+=1
                else:
                    print("¡Respuesta correcta!")
                    superados.append(retos[pos])
                    pos+=1
            case "Reto 7 | Ecuacion": #Ecuacion
                n1 = randint(1, 100)
                n2 = randint(1, 100)
                n3 = randint(1, 100)
                respuesta = int(input(f"Ingrese el resultado de {n1} + {n2} * {n3}: "))
                if (respuesta != n1 + (n2 * n3)):
                    print("Respuesta incorrecta.")
                    continues-=1
                    pos+=1
                else:
                    print("¡Respuesta correcta!")
                    superados.append(retos[pos])
                    pos+=1
            case "Reto 8 | Factorial": #Factorial
                n1 = randint(1, 10)
                respuesta = int(input(f"Ingrese el factorial de {n1}: "))
                if (respuesta != factorial(n1)):
                    print("Respuesta incorrecta.")
                    continues-=1
                    pos+=1
                else:
                    print("¡Respuesta correcta!")
                    superados.append(retos[pos])
                    pos+=1
    if((len(superados)*100)/8 >= 80):
        print("¡Felicitaciones! ¡Has ganado el juego! Perdiste tu tiempo con éxito.")
        print(f"El porcentaje de retos completados es de {(len(superados)*100)/8}")
        print(f"Has completado los siguientes retos: {', '.join(map(str, ordenar(superados)))}") #Llamo a la función ordenar. Repito que un sorted hubiera sido mejor y es lo que hubiera usado.
    elif (continues == 0):
        print("Se te han acabado los intentos. Has perdido.")
    else:
        print("Has llegado a la meta, pero me temo que no has superado la cantidad necesaria de desafíos para ganar.")
        print(f"El porcentaje de retos completados es de {(len(superados)*100)/8}") #La gente que falle 2 intentos automáticamente perderá, pero los dejo ir al final en modo de burla (?)
        #Decidí no agregar los retos completados aquí porque: solo el ganador tiene derecho de saber qué retos completaron y cuál es cuál jaja.
    
#MAIN
yes = 1
while yes != 0:
    retos = desafios()
    juego(retos)
    val = "relleno" #Seguro hay otra manera de inicializarlo, pero no se me ocurre y tomar más café no me va a ayudar a que me venga una idea
    while (val != "s" and val!="n"):
        val = input("\n¿Quieres continuar jugando? [responde con S o N]: ")
        val.lower()
        if (val == "s"):
            yes = 1
        else:
            yes = 0